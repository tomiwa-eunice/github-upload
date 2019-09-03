import matplotlib.pyplot as plt
plt.plot([1,2,1,2,3,2,4,1])
plt.plot([1,2,3,4],[5,4,3,2])
plt.show()


import matplotlib.pyplot as plt
#some simple data
x=[1,2,3,4]
y=[5,4,3,2]
#divide subplots into 2 x 3
# create first chart
plt.subplot(231)
plt.plot(x,y)
plt.subplot(232)
plt.bar(x,y)
plt.subplot(233)
plt.barh(x,y)
#Create stacked bar chart
plt.subplot(234)
plt.bar(x,y)
#we need more data for stacked bar chart
y1=[7,8,5,3]
plt.bar(x,y1,bottom=y,color='r')
#box plot
plt.subplot(235)
plt.boxplot(x)
#scatter plot
plt.subplot(236)
plt.scatter(x,y)
plt.show()
