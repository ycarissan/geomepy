VERSION=1.0.0a7
python setup.py sdist
gpg --detach-sign -a dist/geomepy-${VERSION}.tar.gz 
twine upload -r internal dist/geomepy-${VERSION}.tar.gz dist/geomepy-${VERSION}.tar.gz.asc 
