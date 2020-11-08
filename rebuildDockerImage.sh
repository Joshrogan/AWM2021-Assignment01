#!/bin/bash
docker stop geodjango
docker rm geodjango
docker container rm geodjango
docker image rm geodjango
docker build --no-cache -t geodjango .

docker create --name geodjango --network awm2021 --network-alias my_geodjango -t -v html_data:/usr/src/app/static geodjango

docker container commit geodjango joshrogan/geodjango:latest
docker push joshrogan/geodjango:latest