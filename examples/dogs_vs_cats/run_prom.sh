docker run --rm --name prometheus -v $PWD/prom_config/:/etc/prometheus/ -d --network host prom/prometheus
docker run --rm --name pgw -d --network host prom/pushgateway
