# Django with postgres and elasticsearch

This project is a seed project/POC to implement Django with postgres and elasticsearch, which 
means we can use postgres as primary database and elasticsearch as secondary search db.

This implementation will update/index the data to the elasticsearch as data is changed


##Features:

- django with postgres
- elasticsearch implementation
- updating elasticsearch as we make changes in postgres db
- CRUD operations - using Restful webservices.



##

`http://localhost:9200/example_blog/_search`



## References:

- https://github.com/sabricot/django-elasticsearch-dsl
- https://github.com/barseghyanartur/django-elasticsearch-dsl-drf