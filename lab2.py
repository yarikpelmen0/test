import matplotlib.pyplot as plt
import numpy as np

#Задание 1
fig = plt.figure()

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.cos(x)
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, y)

x = np.linspace(-10, 10, 100)
y = x**2
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, y)

x = np.linspace(0, 10, 100)
y = np.sqrt(x)
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x, y)

plt.show()


#Задание 2, 3, 4
fig, axs = plt.subplots(2, 2,
    figsize=(10, 8),
    facecolor="c",
    num="Math plots"
)
x1 = np.linspace(-2*np.pi, 2*np.pi, 100)
axs[0, 0].plot(x1, np.sin(x1))
axs[0, 0].set_title("y=sin(x)")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("y")
axs[0, 0].grid(True)

x2 = np.linspace(-2*np.pi, 2*np.pi, 100)
axs[0, 1].plot(x2, np.cos(x2))
axs[0, 1].set_title("y=cos(x)")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("y")
axs[0, 1].grid(True)

x3 = np.linspace(-10, 10, 100)
axs[1, 0].plot(x3, x3**2)
axs[1, 0].set_title("y=x^2")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("y")
axs[1, 0].grid(True)

x4 = np.linspace(0, 10, 100)
axs[1, 1].plot(x4, np.sqrt(x4))
axs[1, 1].set_title("y=sqrt(x)")
axs[1, 1].set_xlabel("x")
axs[1, 1].set_ylabel("y")
axs[1, 1].grid(True)

plt.show()


#Задание 5, 6
fig4 = plt.figure()
ax1 = fig4.add_subplot(3, 1, 1)
ax1.grid(True)
ax1.plot(x1, np.sin(x1),
    color='blue',
    marker='D')

ax2 = fig4.add_subplot(3, 1, 2)
noise = np.random.normal(0, 0.2, size=100)
ax2.plot(x1, np.sin(x1),
    color='orange',
    linestyle='--')

ax2.scatter(x1, np.sin(x1) + noise)

arr1 = np.linspace(0, 10, 100)
arr2 = np.linspace(0, 10, 100)
arr3 = np.array([1, 2, 3])

ax3 = fig4.add_subplot(3, 1, 3)
ax3.scatter(arr1, arr2,
    s=arr3)

plt.show()


