
import numpy as np
import matplotlib.pyplot as plt


data = {
    "apple":20,
    "lemon":30,
    "orange":40,
    "mango":20,
    "graps":10,

}

names = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10,5))
plt.bar(names,values,color="blue")
plt.title("datails of fruits")
plt.xlabel("fruits")
plt.ylabel("qutity")
plt.show()

plt.barh(names,values,color="red")
plt.title("datails of fruits")
plt.xlabel("fruits")
plt.ylabel("qutity")
plt.show()
