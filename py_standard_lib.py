import json
from pathlib import Path
import csv
# copy
import shutil

# create a path
p = Path(r"c:/programm files/microsoft")
p2 = Path()/"images"/Path.home()
print(p)
print(p2)

path = Path()
print(path)
path.exists()
path.is_dir()
path.is_file()

# get all content in a directory
# limitation of iterdir(generator) cannot search or recurs
print([p for p in path.iterdir()])

# Better than open() method as it takes care of
# opening and closing file
pathF = Path()/"text.txt"
print(pathF.is_file())
# print(pathF.read_bytes())
# overwrites does not append
pathF.write_text(" added content from program")
print(pathF.read_text())
destPath = Path("C:/Users/The Scientist/Desktop/coding files/")
# when use copyfile()=> permission issues
delPath = Path("C:/Users/The Scientist/Desktop/coding files/")/"text.txt"
# delPath.unlink()
shutil.copy(pathF, destPath)

# csv cannot use path

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "age"])
    writer.writerow([1, "samuel", "30"])
    writer.writerow([2, "john", "20"])

# read csv
with open("data.csv") as file:
    read = csv.reader(file)  # why we cannot use path except file object
    for r in read:
        print(r)

# Json

data = [{"id": 1, "title": "terminator", "year": 1992},
        {"id": 2, "title": "Hard Target", "year": 1990}]
jsonData = json.dumps(data)
print(jsonData)

# write to file
movie = Path("movies.json")
movie.write_text(jsonData)

# read
movies_read = Path("movies.json").read_text()
resultData = json.loads(movies_read)
print(resultData[1]["title"])
