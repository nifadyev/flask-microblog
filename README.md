# flask-microblog

## How to install ElasticSearch

https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html


# How to build docker image

Use command --network=host to avoid errors while installing pip packages
Full command is `docker build --network=host -t microblog:latest .`


run with mysql and elasticsearch (use 2 terminals or `-d` docker option for background execution)

```
docker run --name mysql1 -e MYSQL_RANDOM_ROOT_PASSWORD=yes     -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog     -e MYSQL_PASSWORD=smith229     mysql/mysql-server:5.7

docker run --name elasticsearch -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:7.6.2

docker run --name microblog -p 8000:5000 --rm \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    microblog:latest
```
