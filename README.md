docker pull redis

docker run --name redis-server -d redis

docker run --rm -it --link redis-server:redis-server --name redis-cli redis /bin/bash

docker build -t muriloacs/pydocker .

docker run --rm --link redis-server:redis-server --name app muriloacs/pydocker
