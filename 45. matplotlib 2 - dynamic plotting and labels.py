# easiest to use: http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib


#importing pyplot
from matplotlib import pyplot as plt

x = [5,8,10]
y = [12,16,6]

plt.plot(x,y)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
