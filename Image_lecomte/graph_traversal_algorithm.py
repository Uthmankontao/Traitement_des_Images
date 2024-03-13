
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Définition de la fonction de conversion d'image en niveaux de gris et en matrice binaire
def convert_to_binary_map(image_array, threshold=128):
    binary_map = (image_array > threshold).astype(np.int_)
    return binary_map

# Fonction pour le parcours de graphe
def graph_traversal(start, end, map_array):
    distance_map = np.full(map_array.shape, np.inf)
    distance_map[start] = 0
    list_points = [start]
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    while list_points:
        current_point = list_points.pop(0)
        current_distance = distance_map[current_point]
        
        for dx, dy in directions:
            neighbor = (current_point[0] + dx, current_point[1] + dy)
            if (0 <= neighbor[0] < map_array.shape[0] and
                0 <= neighbor[1] < map_array.shape[1] and
                map_array[neighbor] == 0):
                if current_distance + 1 < distance_map[neighbor]:
                    distance_map[neighbor] = current_distance + 1
                    list_points.append(neighbor)
    
    return distance_map

# Charger l'image de la carte
image_path = 'chemin/vers/votre/carte.png'
outdoor_map_img = Image.open(image_path).convert("L")
outdoor_map_array = np.array(outdoor_map_img)

# Convertir l'image de la carte en matrice binaire
binary_outdoor_map = convert_to_binary_map(outdoor_map_array)

# Sélectionner les points de départ et d'arrivée
point_start = (0, 0)
point_end = (binary_outdoor_map.shape[0] - 1, binary_outdoor_map.shape[1] - 1)

# Effectuer le parcours de graphe
distance_map = graph_traversal(point_start, point_end, binary_outdoor_map)

# Afficher la carte des distances
plt.imshow(distance_map, cmap='hot')
plt.colorbar(label='Distance from start')
plt.scatter([point_start[1], point_end[1]], [point_start[0], point_end[0]], c=['blue', 'red'])
plt.title("Distance Map with Start (Blue) and End (Red) Points")
plt.show()
