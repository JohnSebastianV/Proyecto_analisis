from math import sqrt

def calculate_solid(num_faces, num_vertices, num_edges, edge_length):
    if num_faces == 4 and num_vertices == 4 and num_edges == 6:
        area = sqrt(3) * edge_length**2
        volume = (edge_length**3) / (6 * sqrt(2))
        return "Tetraedro", area, volume
    elif num_faces == 6 and num_vertices == 8 and num_edges == 12:
        area = 6 * edge_length**2
        volume = edge_length**3
        return "Cubo", area, volume
    elif num_faces == 8 and num_vertices == 6 and num_edges == 12:
        area = 2 * sqrt(3) * edge_length**2
        volume = (sqrt(2) / 3) * edge_length**3
        return "Octaedro", area, volume
    elif num_faces == 12 and num_vertices == 20 and num_edges == 30:
        phi = (1 + sqrt(5)) / 2
        area = 3 * sqrt(25 + 10 * sqrt(5)) * edge_length**2
        volume = (15 + 7 * sqrt(5)) / 4 * edge_length**3
        return "Dodecaedro", area, volume
    elif num_faces == 20 and num_vertices == 12 and num_edges == 30:
        area = 5 * sqrt(3) * edge_length**2
        volume = (5 * (3 + sqrt(5)) / 12) * edge_length**3
        return "Icosaedro", area, volume
    else:
        return None, None, None
