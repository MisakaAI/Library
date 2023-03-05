# 删除右键菜单 在 Visual Studio 中打开

使用快捷键 `Win+R` 打开 `regedit` 注册表编辑器。

打开`计算机\HKEY_CLASSES_ROOT\Directory\Background\shell\AnyCode`

右键新建 **DWORD（32位）值**，名称：`HideBasedOnVelocityId`，值：`639bc8`

