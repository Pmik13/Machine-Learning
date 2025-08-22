import numpy as np

def jpeg_ls_prediction(image):
    height, width = image.shape
    predicted = np.zeros((height, width), dtype=int)
    residual = np.zeros((height, width), dtype=int)

    for y in range(height):
        for x in range(width):
            if x == 0:
                predicted[y, x] = 0  # Brak lewego piksela, domyślnie 0
            else:
                predicted[y, x] = image[y, x - 1]  # Predykcja X' = W
            
            residual[y, x] = image[y, x] - predicted[y, x]  # Różnica

    return residual

# Przykładowy obraz (8x8), gdzie 1 to czarny piksel, 0 to biały
image = np.array([
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
])

residual_image = jpeg_ls_prediction(image)
print(residual_image)
