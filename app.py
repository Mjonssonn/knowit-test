import requests
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# Connection with sqlalchemy to work with Pandas to_sql
conn_string = "postgresql://postgres:postgres@localhost:5432/knowit"
engine = create_engine(conn_string)

# Connecting to the postgresql database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="knowit",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# Fetching the data and converting it to JSON
response = requests.get("https://swapi.dev/api/people").json()

# Creating a pandas dataframe which will store the JSON response
# Fetching the 'results' symbol and the contents in it with each header
df = pd.DataFrame(response['results'])

# Adding the data to a .csv file
data_to_csv = df.to_csv('people.csv')

# Reading the .csv file
data = pd.read_csv('people.csv')

data = data[["name", "height", "mass", "hair_color", "skin_color", "eye_color",
             "birth_year", "gender", "homeworld", "created", "edited", "url"]]

# Dataframe to SQL
data.to_sql('people', engine, if_exists='replace')

sql = '''SELECT * FROM people;'''
cur.execute(sql)

# Prints all the rows
for i in cur.fetchall():
    print(i)

conn.commit()
conn.close()
