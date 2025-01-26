# 仓库

Docker Hub 是容器镜像的集合，使您能够公开或私下存储、管理和共享Docker镜像。

- [创建存储库](https://docs.docker.com/docker-hub/repos/create/)
- [归档存储库](https://docs.docker.com/docker-hub/repos/archive/)
- [删除存储库](https://docs.docker.com/docker-hub/repos/delete/)
- [管理个人设置](https://docs.docker.com/docker-hub/repos/settings/)

## 私有仓库

- [registry](https://hub.docker.com/_/registry)

```sh
# 运行本地仓库
docker run -d -p 5000:5000 --restart always --name registry registry:2

# 自定义仓库目录
# -v /mnt/registry:/var/lib/registry

# 使用本地仓库
docker pull ubuntu
docker tag ubuntu localhost:5000/ubuntu
docker push localhost:5000/ubuntu
```
