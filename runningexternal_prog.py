import requests
import subprocess
from urllib import response

print("Running external programs")

completed = subprocess.run(
    ["ls", "-l"], capture_output=True, text=True, check=True)
print("args", completed.args)


response = requests.get("htpp://google.com")
print(response)
