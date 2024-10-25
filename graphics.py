import pyvista as pv
from pyvistaqt import BackgroundPlotter

def draw_solid(solid, edge_length):
    plotter = BackgroundPlotter()
    if solid == "Tetraedro":
        plotter.add_mesh(pv.Tetrahedron().scale(edge_length), color="cyan", show_edges=True)
    elif solid == "Cubo":
        plotter.add_mesh(pv.Cube().scale(edge_length), color="yellow", show_edges=True)
    elif solid == "Octaedro":
        plotter.add_mesh(pv.Octahedron().scale(edge_length), color="purple", show_edges=True)
    elif solid == "Dodecaedro":
        plotter.add_mesh(pv.Dodecahedron().scale(edge_length), color="orange", show_edges=True)
    elif solid == "Icosaedro":
        plotter.add_mesh(pv.Icosahedron().scale(edge_length), color="green", show_edges=True)

    plotter.show()
