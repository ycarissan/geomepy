sudo systemctl start docker
docker network create reseau
docker create --name client2 --network reseau -it client_2 /bin/bash
docker create --name client3 --network reseau -it client_3 /bin/bash
docker create --name pypi    --network reseau -it --rm -h pypi.local -v /srv/pypi:/srv/pypi:rw -p 8080:80 codekoala/pypi:1.2.1
docker start pypi
docker start client2
docker start client3
firefox http://localhost:8080
echo "Dans le client :"
echo "pip install --trusted-host pypi --extra-index-url http://pypi geomepy==1.0.0a7"
echo ""
echo "docker attach client2"
echo "docker attach client3"
echo "docker attach pypi"
