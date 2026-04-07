import matplotlib.pyplot as plt

# This one line turns your graph into a "cartoon" style!
plt.xkcd()

labels = ["Dog", "Cat", "Wolf", "Lion"]
sizes = [50, 40, 50, 60]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Cartoon Style Stats")
plt.show()