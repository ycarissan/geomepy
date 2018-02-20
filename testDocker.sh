sudo systemctl start docker
docker network create reseau
docker create --name client --network reseau -it python:3 /bin/bash
docker create --name pypi   --network reseau -it --rm -h pypi.local -v /srv/pypi:/srv/pypi:rw -p 8080:80 codekoala/pypi:1.2.1
docker start pypi
docker start client
firefox http://localhost:8080
echo "Dans le client :"
echo "pip install --trusted-host pypi --extra-index-url http://pypi geomepy==1.0.0a7"
echo ""
echo "docker attach client"
echo "docker attach pypi"
