# Wekan

- [Wekan](https://wekan.team/)
- [github](https://github.com/wekan/wekan)

docker run -d --restart=always --name wekan-db mongo:5

docker run -d --restart=always --name wekan \
    --link "wekan-db:db" \
    -e "WITH_API=true" \
    -e "MONGO_URL=mongodb://wekan-db:27017/wekan" \
    -e "ROOT_URL=http://10.0.200.136:2000" \
    -p 2000:8080 \
    quay.io/wekan/wekan