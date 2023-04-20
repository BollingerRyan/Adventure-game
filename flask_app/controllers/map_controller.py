import os
import random
import string
import numpy as np
import pygame

def generate_map():
        # Define the parameters of the map
    map_width = 100
    map_height = 100
    tile_size = 32

# Get the absolute path to the directory containing the code and image files
    current_path = os.path.dirname(__file__)
    image_path = os.path.join(current_path, 'static_game', 'terrain')

# Define the minimum and maximum sizes of the water and mountain clusters
    min_size = 10
    max_size = 50

# Create an empty map array
    map_array = np.zeros((map_height, map_width), dtype=np.uint8)

# Define a function to perform flood fill
    def flood_fill(x, y, size, tile_type):
        if size <= 0 or x < 0 or x >= map_width or y < 0 or y >= map_height or map_array[y, x] == 1 or map_array[y, x] == 2:
            return
        map_array[y, x] = tile_type
        size -= 1
        if size <= 0:
            return
        flood_fill(x-1, y, size, tile_type)
        flood_fill(x+1, y, size, tile_type)
        flood_fill(x, y-1, size, tile_type)
        flood_fill(x, y+1, size, tile_type)

# Generate water and mountain clusters on the map
    for i in range(5):
        # Randomly select a starting position for the water or mountain cluster
        x = np.random.randint(map_width)
        y = np.random.randint(map_height)

    # Randomly select a size for the water or mountain cluster
        size = np.random.randint(min_size, max_size)

    # Randomly select whether to create a water or mountain cluster
        if np.random.rand() < 0.5:
            tile_type = 1  # water
        else:
            tile_type = 2  # mountain

    # Perform flood fill to create the cluster
        flood_fill(x, y, size, tile_type)

# Create a blank surface for the map
    map_surface = pygame.Surface((map_width * tile_size, map_height * tile_size))
    map_surface.fill(pygame.Color("black"))

# Fill the surface with tiles or objects
    for x in range(map_width):
        for y in range(map_height):
        # Check the type of the current tile
            tile_type = map_array[y, x]

        # Use a different image based on the tile type
            if tile_type == 1:
                terrain_type = "water"
            elif tile_type == 2:
                terrain_type = "mountain"
            else:
            # Use a random number generator to place different types of terrain on the map
                if random.random() < 0.2:
                    terrain_type = "grass"
                else:
                    continue

            tile_image = pygame.image.load(os.path.join(image_path, f"{terrain_type}.jpg"))
            map_surface.blit(tile_image, (x * tile_size, y * tile_size))

# Save the map as a PNG file with a random name
    filename = "".join(random.choices(string.ascii_letters, k=10)) + ".jpg"
    pygame.image.save(map_surface, os.path.join('flask_app', 'static', 'maps', filename))
    return filename