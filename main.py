import matplotlib.pyplot as plt

x_data = list(range(1,5001))
y_data = [x**3 for x in x_data]

fig,ax = plt.subplots()

plt.style.use('ggplot')

ax.set_xlabel("Normal", fontsize=14)
ax.set_ylabel("Cubic", fontsize=14)
ax.set_title("Cubic Numbers", fontsize=24)

ax.scatter(x_data, y_data, c=y_data, cmap=plt.cm.Blues, s = 5)

plt.show()