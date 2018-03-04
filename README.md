# Django with postgres and elasticsearch

This project is a seed project/POC to implement Django with postgres and elasticsearch, which 
means we can use postgres as primary database and elasticsearch as secondary search db. This implementation 
will update/index the data to the elasticsearch as data is changed and create 
django sytle api with pagination using elasticsearch backend.

The code uses `example_blog` as postgres db name and `example_blog` as index name in elasticsearch.

## Why postgres + elasticsearch stack !

- **postgres** - "The world's most advanced open source database" as their website claims is 
very well supported by Django and has `jsonfield` support by django which is awesome. Its suits 
very well for any application because most of the user facing applications are expected to have a 
structured data.

- **elasticsearch** - Elasticsearch is a search engine based on Lucene. It provides a distributed,
 multitenant-capable full-text search engine. It is very good when the data is huge and you want to 
 have a search API/functionality  in your application. You can build a searchengine with it, because 
 it have search tons of data with ease.

## How to run 


1. create the infrastructure needed and start the machines using `cd webapp && docker-compose up`.

2. Run the Postgres migrations needed  `cd webapp && docker-compose run web python manage.py migrate`.

3. Create index in elasticsearch  `cd webapp && docker-compose run web python manage.py search_index --create`. This step will 
be ignored. elasticsearch will create an index when needed anyways.

4. Now the web application is accessible at `http://location:8000` 

5. You should be able to see CRUD operation APIs at `http://localhost:8000/blogs/` pointing to the  postgres backend 

6. You should be able to see List/Search API at `http://localhost:8000/blogs-es`
  





## Features and todo:

- [*] django with postgres
- [*] CRUD operations - using Restful webservices.
- [*] elasticsearch implementation
- [*] updating elasticsearch as we make changes in postgres db
- [*] Django style search API with elasticsearch backend. 
- [*] Dockerfile and docker-compose.yaml

## Projects Uses

- Django 1.11
- Elasticsearch 5.6
- Postgres 9.6
- [django-elasticsearch-dsl](https://github.com/sabricot/django-elasticsearch-dsl)
- [django-elasticsearch-dsl-drf](https://github.com/barseghyanartur/django-elasticsearch-dsl-drf)



## References:

- https://github.com/sabricot/django-elasticsearch-dsl
- https://github.com/barseghyanartur/django-elasticsearch-dsl-drf