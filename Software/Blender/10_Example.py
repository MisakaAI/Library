import bpy
import math
import os
from mathutils import Vector


def get_node_tree(data_block):
    """返回材质或 World 的节点树，并兼容 Blender 4.x/5.x。"""
    # Blender 5.0 起材质和 World 默认使用节点；use_nodes 已弃用，
    # 继续对它赋值会产生 DeprecationWarning，并将在 Blender 6.0 被移除。
    if bpy.app.version < (5, 0, 0):
        data_block.use_nodes = True

    node_tree = data_block.node_tree
    if node_tree is None:
        raise RuntimeError(f"无法为 {data_block.name!r} 获取节点树")
    return node_tree


def clear_scene():
    """删除场景中的所有物体。"""
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def set_active(obj):
    """把指定物体设为当前活动对象。"""
    bpy.ops.object.select_all(action="DESELECT")
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def create_material():
    """创建带有细微表面起伏的白色釉面陶瓷材质。"""
    material = bpy.data.materials.new(name="White Glazed Ceramic")
    node_tree = get_node_tree(material)
    nodes = node_tree.nodes
    links = node_tree.links

    principled = nodes.get("Principled BSDF")
    ceramic_white = (0.82, 0.82, 0.82, 1.0)
    principled.inputs["Base Color"].default_value = ceramic_white
    principled.inputs["Roughness"].default_value = 0.22
    principled.inputs["IOR"].default_value = 1.46

    # 新旧 Blender 版本中清漆层输入的名字不同。
    coat_input = principled.inputs.get("Coat Weight") or principled.inputs.get("Clearcoat")
    if coat_input:
        coat_input.default_value = 0.35

    coat_roughness = (
        principled.inputs.get("Coat Roughness")
        or principled.inputs.get("Clearcoat Roughness")
    )
    if coat_roughness:
        coat_roughness.default_value = 0.08

    # 极轻的噪波凹凸避免表面看起来像完全光滑的塑料。
    noise = nodes.new("ShaderNodeTexNoise")
    noise.name = "Ceramic Micro Texture"
    noise.inputs["Scale"].default_value = 38.0
    noise.inputs["Detail"].default_value = 3.0
    noise.inputs["Roughness"].default_value = 0.7

    bump = nodes.new("ShaderNodeBump")
    bump.name = "Ceramic Micro Bump"
    bump.inputs["Strength"].default_value = 0.055
    bump.inputs["Distance"].default_value = 0.025

    links.new(noise.outputs["Fac"], bump.inputs["Height"])
    links.new(bump.outputs["Normal"], principled.inputs["Normal"])

    material.diffuse_color = ceramic_white

    return material


def create_print_material(image_path):
    """将外部图片制作成与白色釉面亮度一致的印花材质。"""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"找不到印花图片: {image_path}")

    material = bpy.data.materials.new(name="Mug Print")
    node_tree = get_node_tree(material)
    nodes = node_tree.nodes
    links = node_tree.links
    principled = nodes.get("Principled BSDF")
    principled.inputs["Roughness"].default_value = 0.24
    principled.inputs["IOR"].default_value = 1.46

    coat_input = principled.inputs.get("Coat Weight") or principled.inputs.get("Clearcoat")
    if coat_input:
        coat_input.default_value = 0.25

    image_texture = nodes.new("ShaderNodeTexImage")
    image_texture.name = "Print Image"
    image_texture.image = bpy.data.images.load(image_path, check_existing=True)
    image_texture.interpolation = "Linear"
    image_texture.extension = "CLIP"

    # PNG 的透明区域先与白色合成，避免透明像素的黑色 RGB 渗入印花。
    alpha_over_white = nodes.new("ShaderNodeMixRGB")
    alpha_over_white.name = "Print Over White"
    alpha_over_white.blend_type = "MIX"
    alpha_over_white.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)

    # 将图片乘以陶瓷白，令图片白底和杯身尽量自然地融为一体。
    multiply = nodes.new("ShaderNodeMixRGB")
    multiply.name = "Match Ceramic White"
    multiply.blend_type = "MULTIPLY"
    multiply.inputs[0].default_value = 1.0
    multiply.inputs[2].default_value = (0.82, 0.82, 0.82, 1.0)

    links.new(image_texture.outputs["Alpha"], alpha_over_white.inputs[0])
    links.new(image_texture.outputs["Color"], alpha_over_white.inputs[2])
    links.new(alpha_over_white.outputs["Color"], multiply.inputs[1])
    links.new(multiply.outputs["Color"], principled.inputs["Base Color"])

    return material


def create_mug_print(material):
    """创建紧贴杯壁的弧形贴花，并生成与图片对应的 UV。"""
    radius = 1.5015
    center_angle = math.radians(-62.0)
    angular_width = math.radians(55.0)
    bottom = -0.69
    top = 0.73
    segments = 40

    vertices = []
    faces = []

    for index in range(segments + 1):
        factor = index / segments
        angle = center_angle - angular_width / 2 + angular_width * factor
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.extend(((x, y, bottom), (x, y, top)))

    for index in range(segments):
        lower_left = index * 2
        faces.append(
            (
                lower_left,
                lower_left + 2,
                lower_left + 3,
                lower_left + 1,
            )
        )

    mesh = bpy.data.meshes.new(name="MugPrintMesh")
    mesh.from_pydata(vertices, [], faces)
    mesh.update()

    decal = bpy.data.objects.new(name="MugPrint", object_data=mesh)
    bpy.context.collection.objects.link(decal)

    uv_layer = mesh.uv_layers.new(name="PrintUV")
    for polygon in mesh.polygons:
        polygon.use_smooth = True
        for loop_index in polygon.loop_indices:
            vertex_index = mesh.loops[loop_index].vertex_index
            u = (vertex_index // 2) / segments
            v = float(vertex_index % 2)
            uv_layer.data[loop_index].uv = (u, v)

    mesh.materials.append(material)

    return decal


def create_ground():
    """创建用于承接柔和阴影的暖灰色地面。"""
    material = bpy.data.materials.new(name="Warm Gray Ground")
    node_tree = get_node_tree(material)
    principled = node_tree.nodes.get("Principled BSDF")
    principled.inputs["Base Color"].default_value = (0.18, 0.16, 0.14, 1.0)
    principled.inputs["Roughness"].default_value = 0.72

    bpy.ops.mesh.primitive_plane_add(
        size=200.0,
        location=(0.0, 0.0, -1.32),
    )
    ground = bpy.context.object
    ground.name = "Ground"
    ground.data.materials.append(material)

    return ground


def point_at(obj, target):
    """让相机或灯光的局部 -Z 轴指向目标。"""
    direction = Vector(target) - obj.location
    obj.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()


def create_area_light(name, location, energy, size, color, target=(0, 0, 0)):
    """创建并对准一盏面积灯。"""
    light_data = bpy.data.lights.new(name=name, type="AREA")
    light_data.energy = energy
    light_data.shape = "DISK"
    light_data.size = size
    light_data.color = color

    light = bpy.data.objects.new(name=name, object_data=light_data)
    bpy.context.collection.objects.link(light)
    light.location = location
    point_at(light, target)

    return light


def setup_lighting():
    """设置产品摄影风格的主光、补光和轮廓光。"""
    # 左前方的大面积主光形成柔和高光。
    create_area_light(
        "Key Light",
        location=(-4.5, -4.0, 6.0),
        energy=360.0,
        size=4.0,
        color=(1.0, 0.82, 0.67),
        target=(0.0, 0.0, 0.25),
    )

    # 右前方低强度冷色补光保留暗部细节。
    create_area_light(
        "Fill Light",
        location=(4.0, -2.5, 2.6),
        energy=140.0,
        size=3.5,
        color=(0.55, 0.72, 1.0),
        target=(0.3, 0.0, 0.1),
    )

    # 后上方窄一些的光勾勒杯口和杯把外缘。
    create_area_light(
        "Rim Light",
        location=(2.0, 3.5, 5.0),
        energy=280.0,
        size=2.2,
        color=(1.0, 0.9, 0.75),
        target=(0.5, 0.0, 0.3),
    )


def setup_camera():
    """创建略微俯视的三分之四产品镜头。"""
    camera_data = bpy.data.cameras.new(name="Product Camera")
    camera_data.lens = 58

    camera = bpy.data.objects.new(
        name="Product Camera",
        object_data=camera_data,
    )
    bpy.context.collection.objects.link(camera)
    camera.location = (5.8, -7.2, 4.4)
    point_at(camera, (0.35, 0.0, 0.05))

    bpy.context.scene.camera = camera

    return camera


def setup_world_and_render(output_path):
    """设置环境、色彩管理以及 PNG 渲染参数。"""
    scene = bpy.context.scene

    world = scene.world or bpy.data.worlds.new("Studio World")
    scene.world = world
    node_tree = get_node_tree(world)
    background = node_tree.nodes.get("Background")
    background.inputs["Color"].default_value = (0.035, 0.028, 0.024, 1.0)
    background.inputs["Strength"].default_value = 0.28

    # Blender 5.x 使用 BLENDER_EEVEE，4.x 使用 BLENDER_EEVEE_NEXT。
    render_engines = scene.render.bl_rna.properties["engine"].enum_items.keys()
    if "BLENDER_EEVEE" in render_engines:
        scene.render.engine = "BLENDER_EEVEE"
    else:
        scene.render.engine = "BLENDER_EEVEE_NEXT"
    scene.render.resolution_x = 720
    scene.render.resolution_y = 720
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.render.filepath = output_path

    # AgX 可以更好地保留釉面和灯光中的高光层次。
    scene.view_settings.look = "AgX - Medium High Contrast"
    scene.view_settings.exposure = -0.25

    return scene


def create_mug_body(material):
    """
    创建杯体。

    外圆柱 - 内圆柱
    通过 Boolean Difference 得到中空结构。
    """

    # --------------------------------------------------
    # 外部圆柱
    # --------------------------------------------------

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=96,
        radius=1.5,
        depth=2.6,
        location=(0, 0, 0),
    )

    body = bpy.context.object
    body.name = "MugBody"

    # --------------------------------------------------
    # 内部圆柱
    # --------------------------------------------------
    #
    # 内圆柱稍微向上移动。
    # 这样：
    #
    # 上面会完全穿出去 -> 杯口打开
    # 下面不会穿透 -> 留下杯底
    #

    bpy.ops.mesh.primitive_cylinder_add(
        vertices=96,
        radius=1.25,
        depth=2.4,
        location=(0, 0, 0.25),
    )

    inner = bpy.context.object
    inner.name = "MugInner"

    # --------------------------------------------------
    # Boolean Difference
    # --------------------------------------------------

    set_active(body)

    boolean = body.modifiers.new(
        name="HollowCup",
        type="BOOLEAN",
    )

    boolean.operation = "DIFFERENCE"
    boolean.solver = "EXACT"
    boolean.object = inner

    # 应用 Boolean
    bpy.ops.object.modifier_apply(
        modifier=boolean.name
    )

    # 删除作为切割器的内部圆柱
    bpy.data.objects.remove(
        inner,
        do_unlink=True,
    )

    # --------------------------------------------------
    # Bevel
    # --------------------------------------------------

    bevel = body.modifiers.new(
        name="RoundedEdges",
        type="BEVEL",
    )

    bevel.width = 0.08
    bevel.segments = 4
    bevel.limit_method = "ANGLE"

    # Smooth shading
    for polygon in body.data.polygons:
        polygon.use_smooth = True

    # 材质
    # Boolean 会为无材质的切割器留下一个空材质槽，先清除它，
    # 否则杯身多边形会继续引用空槽而显示为白色。
    body.data.materials.clear()
    body.data.materials.append(material)
    for polygon in body.data.polygons:
        polygon.material_index = 0

    return body


def create_handle(material):
    """
    使用 Bezier Curve 创建杯把。

    Curve 本身没有厚度，
    bevel_depth 可以给 Curve 增加圆形截面。
    """

    curve_data = bpy.data.curves.new(
        name="MugHandleCurve",
        type="CURVE",
    )

    curve_data.dimensions = "3D"

    # 曲线平滑度
    curve_data.resolution_u = 24

    # 管子的半径
    curve_data.bevel_depth = 0.18

    # 管子的圆滑程度
    curve_data.bevel_resolution = 6

    # 封闭管子两端
    curve_data.use_fill_caps = True

    # --------------------------------------------------
    # 创建 Bezier spline
    # --------------------------------------------------

    spline = curve_data.splines.new(
        type="BEZIER"
    )

    # 默认已有一个点
    # 再增加 4 个，一共 5 个点
    spline.bezier_points.add(4)

    points = [
        (1.38, 0.0,  0.75),
        (2.20, 0.0,  0.85),
        (2.45, 0.0,  0.00),
        (2.20, 0.0, -0.85),
        (1.38, 0.0, -0.75),
    ]

    for point, coordinate in zip(
        spline.bezier_points,
        points,
    ):
        point.co = coordinate

        # 自动计算平滑切线
        point.handle_left_type = "AUTO"
        point.handle_right_type = "AUTO"

    # --------------------------------------------------
    # 创建 Object
    # --------------------------------------------------

    handle = bpy.data.objects.new(
        name="MugHandle",
        object_data=curve_data,
    )

    bpy.context.collection.objects.link(handle)

    # 材质
    curve_data.materials.append(material)

    return handle


def main():

    print("Creating mug...")

    clear_scene()

    # mian.py 和 logo.webp 所在目录
    script_dir = os.path.dirname(
        os.path.abspath(__file__)
    )
    print_image_path = os.path.join(
        script_dir,
        "logo.webp",
    )

    material = create_material()
    print_material = create_print_material(print_image_path)

    body = create_mug_body(material)
    handle = create_handle(material)
    print_decal = create_mug_print(print_material)

    create_ground()
    setup_lighting()
    setup_camera()

    # --------------------------------------------------
    # 保存 Blend 文件
    # --------------------------------------------------

    output_path = os.path.join(
        script_dir,
        "mug.blend",
    )

    render_path = os.path.join(
        script_dir,
        "mug.png",
    )

    setup_world_and_render(render_path)

    # 先渲染，再保存。这样打开 Blend 文件时可以直接查看 Render Result。
    print(f"Rendering to: {render_path}")
    bpy.ops.render.render(write_still=True)

    bpy.ops.wm.save_as_mainfile(
        filepath=output_path
    )

    print("Mug created successfully.")
    print(f"Saved to: {output_path}")
    print(f"Rendered to: {render_path}")


if __name__ == "__main__":
    main()
