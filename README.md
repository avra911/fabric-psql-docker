# Fabric Bolt + PostgreSQL + Docker = &lt;3
Run:

```sh
docker-compose up -d
```


Create super-user:

```sh
docker-compose run --entrypoint fabric-bolt --rm fabric createsuperuser
```
