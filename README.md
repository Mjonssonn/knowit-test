# knowit-test

#####

```
Installs required:

pip install pandas
pip install sqlalchemy
pip install requests
pip install psycopg2
```

### Run the docker container

```
docker run -p 5432:5432 -d -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=knowit -v pgdata:/var/lib/postgresql/data postgres
```

#### Connect to container

```
docker exec -it 820cac5fb96f psql -U postgres knowit
```

###### SQL queries

```
sql = '''INSERT INTO people(
name varchar(45) PRIMARY KEY,
height int,
mass int,
hair_color varchar(15),
skin_color varchar(10),
eye_color varchar(10),
birth_year varchar(25),
gender varchar(10),
homeworld varchar(100),
created varchar(45),
edited varchar(45),
url varchar(45)
);
'''
```

### To schedule (windows)

https://datatofish.com/python-script-windows-scheduler/
