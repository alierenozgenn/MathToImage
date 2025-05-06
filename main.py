import numpy as np
import matplotlib.pyplot as plt
import os

# Görüntü boyutu
width, height = 500, 500
x = np.linspace(-3, 3, width)
y = np.linspace(-3, 3, height)
X, Y = np.meshgrid(x, y)

# RGB Kanallarını tanımlıyoruz
mu = 0
sigma = 1

R = np.exp(-((X - mu)**2 + (Y - mu)**2) / (2 * sigma**2)) 
G = (np.sin(2 * X) + 1) / 2 
B = (np.cos(X + Y) + 1) / 2 


rgb_image = np.stack([R, G, B], axis=-1)


os.makedirs("output", exist_ok=True)

plt.imsave("output/rgb_advanced.png", rgb_image)


fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax1.plot_surface(X, Y, R, cmap='Reds')
ax1.set_title("Red: Gaussian")

ax2 = fig.add_subplot(132, projection='3d')
ax2.plot_surface(X, Y, G, cmap='Greens')
ax2.set_title("Green: sin(2X)")

ax3 = fig.add_subplot(133, projection='3d')
ax3.plot_surface(X, Y, B, cmap='Blues')
ax3.set_title("Blue: cos(X+Y)")

plt.tight_layout()
plt.savefig("output/mesh_advanced.png")
plt.show()
