# import requests
# res = requests.get("https://www.google.co.in")
# print(res.text)

import requests

# A free API that returns JSON data
url = "https://jsonplaceholder.typicode.com/todos/1"
res = requests.get(url)

if res.status_code == 200:
    # .json() converts the string into a Python Dictionary
    data = res.json()
    print(f"Task Title: {data['title']}")
    print(f"Completed: {data['completed']}")
else:
    print("Error fetching data")