#create ct with pgdb image 
docker run -d \
  --name postgres_db_15 \
  -e POSTGRES_USER=dbsuser \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=pgdb \
  -p 5433:5432 \
  postgres:15
  
#connet to the pgdb  
docker exec -it postgres_db_15 psql -U dbsuser -d pgdb
#restore pgdb to ct
cat postgres_backup.sql | docker exec -i postgres_db_15 psql -U dbsuser -d pgdb
