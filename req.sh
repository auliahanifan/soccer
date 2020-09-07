docker container kill redis
docker container rm redis
docker run --name redis -p 6379:6379 -d redis:5-alpine
