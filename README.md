# flask-microblog

## How to install ElasticSearch

https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html


# How to build docker image

Use command --network=host to avoid errors while installing pip packages
Full command is `docker build --network=host -t microblog:latest .`


run with mysql, elasticsearch, redis and rq worker (use multiple terminals or `-d` docker option for background execution)

```
docker run --name mysql1 -e MYSQL_RANDOM_ROOT_PASSWORD=yes     -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog     -e MYSQL_PASSWORD=smith229     mysql/mysql-server:5.7

docker run --name elasticsearch -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:7.6.2

docker run --name redis -p 6379:6379 redis:3-alpine

docker run --name rq-worker --rm -e
    --link mysql:dbserver --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    -e REDIS_URL=redis://redis-server:6379/0 \
    --entrypoint venv/bin/rq \
    microblog:latest worker -u redis://redis-server:6379/0 microblog-tasks

docker run --name microblog -p 8000:5000 --rm \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    -e REDIS_URL=redis://redis-server:6379/0 \
    microblog:latest
```
