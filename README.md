# Django with postgres and elasticsearch

This project is a seed project/POC to implement Django with postgres and elasticsearch, which 
means we can use postgres as primary database and elasticsearch as secondary search db.

This implementation will update/index the data to the elasticsearch as data is changed


##Features:

- [*] django with postgres
- [*] CRUD operations - using Restful webservices.
- [*] elasticsearch implementation
- [*] updating elasticsearch as we make changes in postgres db
- [*] Django style search API with elasticsearch backend. 


## Projects Uses

- Django 1.11
- Elasticsearch 5.6
- Postgres 9.6
- [django-elasticsearch-dsl](https://github.com/sabricot/django-elasticsearch-dsl)
- [django-elasticsearch-dsl-drf](https://github.com/barseghyanartur/django-elasticsearch-dsl-drf)



##

`http://localhost:9200/example_blog/_search`



## References:

- https://github.com/sabricot/django-elasticsearch-dsl
- https://github.com/barseghyanartur/django-elasticsearch-dsl-drf