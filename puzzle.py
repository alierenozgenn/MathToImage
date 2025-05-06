import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import os
import random


image = imread("output/rgb_advanced.png")


height, width, _ = image.shape
assert height == width, "Görsel kare olmalı!"


n = 3
piece_size = height // n


pieces = []

for i in range(n):
    for j in range(n):
        piece = image[i*piece_size:(i+1)*piece_size, j*piece_size:(j+1)*piece_size, :]
        pieces.append(piece)


os.makedirs("output", exist_ok=True)

for k in range(1, 5):
    random.shuffle(pieces)

    puzzle = np.zeros_like(image)

    index = 0
    for i in range(n):
        for j in range(n):
            puzzle[i*piece_size:(i+1)*piece_size, j*piece_size:(j+1)*piece_size, :] = pieces[index]
            index += 1

    plt.imsave(f"output/puzzle_{k}.png", puzzle)
