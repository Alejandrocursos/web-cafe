### IMPORTANTE CAMBIAR VARIABLES DE ENTORNO Y NOMBRE DEL PROYECTO


## Pausar contenedores activos
docker-compose down -v

docker-compose down --remove-orphans -v

#

## Build en Desarrollo
docker-compose up -d --build

#

## Build Producción
docker-compose -f docker-compose.prod.yml up -d --build

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear