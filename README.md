# flask-microblog


![](https://img.shields.io/badge/python-v3.8-blue) ![](https://img.shields.io/badge/flask-1.1.2-blue) ![](https://img.shields.io/badge/platform-windows%20%7C%20linux-lightgrey) ![](https://img.shields.io/badge/license-MIT-green)

Microblog for communicating with users.

## Description

Microblog allows to:

- post messages
- follow users
- set avatar
- search by keywords
- export all posts
- explore users feed

## Requirements

- python3.8+
- pip
- virtualenv
- Flask+
- Redis
- Redis Queue (RQ)
- MySQL
- Elasticsearch

### Pip packages
Install required packages using `virtualenv`

```bash
python -m virtualenv env && source env/bin/activate
python -m pip install -r requirements.txt
```

## Docker

Another option is to use docker: `docker build --network=host -t microblog:latest .`

`--network=host` helps to avoid errors while installing pip packages


Run the following containers in separate terminals or in the background before running `microblog`:

- MySQL

(Optional) Use `-d` docker option for background execution
```bash
docker run --name mysql -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=microblog -e MYSQL_USER=microblog \
    -e MYSQL_PASSWORD=<password> mysql/mysql-server:5.7
```
- Elasticsearch

```bash
docker run --name elasticsearch -p 9200:9200 -p 9300:9300 --rm \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch-oss:7.6.2
```

- Redis

```bash
docker run --name redis -p 6379:6379 redis:3-alpine
```

- Redis Queue

```bash
docker run --name rq-worker --rm -e
    --link mysql:dbserver --link redis:redis-server \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    -e REDIS_URL=redis://redis-server:6379/0 \
    --entrypoint venv/bin/rq \
    microblog:latest worker -u redis://redis-server:6379/0 microblog-tasks
```

Then run `microblog` container:

```bash
docker run --name microblog -p 8000:5000 --rm \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://microblog:<database-password>@dbserver/microblog \
    --link elasticsearch:elasticsearch \
    -e ELASTICSEARCH_URL=http://elasticsearch:9200 \
    -e REDIS_URL=redis://redis-server:6379/0 \
    microblog:latest
```
