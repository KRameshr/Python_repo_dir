import matplotlib.pyplot as plt


#define the dataset
group_names = ["GroupA","GroupB","GroupC"]
group_size = [20,30,50]
size_centre = [5]
a,b,c = [plt.cm.Blues,plt.cm.Reds,plt.cm.Greens]
#Creating the doughnut chart
pie1 = plt.pie(group_size,labels = group_names, radius = 1.5,colors = [a(0.5),b(1.5),c(1.0)])
pie2 = plt.pie(size_centre,radius = 1.0,colors = 'w')
plt.show()