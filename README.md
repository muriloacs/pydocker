docker pull redis

docker run --name redis-server -d redis

docker build -t muriloacs/pydocker .

docker run --rm --link redis-server:redis-server --name app muriloacs/pydocker
