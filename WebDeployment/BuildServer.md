# Building server

Prefered to build a docker container.
Check:

- [This django-postgres-redis-celery tutorial](https://soshace.com/dockerizing-django-with-postgres-redis-and-celery/)

## Create a DigitalOcean droplet

Check [this Initial Server Setup with Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04) to login as root, create new user and ssh as new user.

## To keep the docker always running

Please check [this link](https://stackoverflow.com/questions/43671482/how-to-run-docker-compose-up-d-at-system-start-up).

> ## Notes
>
> - Never push `env` files to git.
