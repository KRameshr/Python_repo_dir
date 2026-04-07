import matplotlib.pyplot as plt

# 1. Dataset
label = ["Dog", "Cat", "Wolf", "Lion"]
sizes = [50, 40, 50, 60]

# 2. Advanced Styling
# Adding 'explode' to highlight one specific slice
# Adding 'shadow' for a 3D effect
explode = (0.05, 0, 0, 0)  # Only "explode" the Dog slice slightly

plt.figure(figsize=(7, 7))
plt.pie(sizes, 
        labels=label, 
        autopct='%1.1f%%', 
        startangle=90,
        explode=explode,
        colors=['red','blue','green','yellow'],
        textprops={'fontsize': 12, 'fontweight': 'bold'})

# 3. The "Circle" Fix
# This ensures the pie is a perfect circle and not an oval
plt.axis('equal') 

plt.title("Animal Population Distribution", pad=20)
plt.show()