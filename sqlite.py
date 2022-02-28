import re
import sqlite3
import json
from pathlib import Path


movies = json.loads(Path("movies.json").read_text())
# with sqlite3 .connect("sqlitedb") as conn:
#     query = "INSERT INTO movies values(?,?,?)"
#     for movie in movies:
#         conn.execute(query, tuple(movie.values()))
#     conn.commit()
# read data
with sqlite3.connect("sqlitedb") as conn:
    query = "SELECT * FROM Movies"
    cursor = conn.execute(query)
 #   for row in cursor:
 #      print(row)
    # retrive all rows into memory
    results = cursor.fetchall()
    print(results)
    print(results[0][1])
