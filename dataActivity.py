import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, color = '#ff6347', linestyle = '--', linewidth = 2, marker = 'o', )
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot of Prime Numbers') 

plt.show()
