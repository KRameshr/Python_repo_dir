
import matplotlib.pyplot as plt

x = range(1,15)
y = [1,4,6,5,3,2,1,5,6,8,7,4,5,4]

plt.stackplot(x,y, colors = 'red', alpha =1)
plt.title("area chart")
plt.plot(x,y, color="green")
plt.grid(True)
plt.show()
