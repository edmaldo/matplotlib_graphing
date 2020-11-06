import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x_values, squares, linewidth=3)

#Set chart title and lable axes.
ax.set_title("Plotting Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()