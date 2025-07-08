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


### More example
#To store your PostgreSQL data outside the container:

docker volume create pgdata

docker run --name pg15 \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin123 \
  -e POSTGRES_DB=mydb \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  -d postgres:15
  
#This way, your database data will persist even if the container is removed.

#Connect to PostgreSQL From the host machine:

psql -h localhost -U admin -d mydb
#(Default port is 5432, password: admin123)

#From inside the container:

docker exec -it pg15 psql -U admin -d mydb
