import tkinter as tk
from tkinter import messagebox
from logic import calculate_solid
from graphics import draw_solid

def show_result():
    try:
        num_faces = int(entry_faces.get())
        num_vertices = int(entry_vertices.get())
        num_edges = int(entry_edges.get())
        edge_length = float(entry_edge_length.get())

        solid, area, volume = calculate_solid(num_faces, num_vertices, num_edges, edge_length)

        if solid:
            label_result.config(text=f"El sólido es un {solid}, su área superficial es {area:.2f}, su volumen es {volume:.2f}")
            draw_solid(solid, edge_length)
        else:
            messagebox.showerror("Error", "No se reconoce un sólido platónico con esos valores.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

root = tk.Tk()
root.title("Sólidos Platónicos")
root.geometry("450x400")
root.minsize(450, 400)

canvas_bg = tk.Canvas(root, width=450, height=400, bg="#EAEDED", highlightthickness=0)
canvas_bg.place(relwidth=1, relheight=1)
canvas_bg.create_oval(300, 20, 400, 120, fill="#9EECFF", outline="")
canvas_bg.create_oval(20, 250, 150, 380, fill="#9EECFF", outline="")

label_style = {"bg": "#EAEDED", "font": ("Arial", 12, "bold"), "fg": "#566573"}

tk.Label(root, text="Número de caras:", **label_style).place(x=30, y=30)
entry_faces = tk.Entry(root, font=("Arial", 10))
entry_faces.place(x=200, y=30, width=200)

tk.Label(root, text="Número de vértices:", **label_style).place(x=30, y=80)
entry_vertices = tk.Entry(root, font=("Arial", 10))
entry_vertices.place(x=200, y=80, width=200)

tk.Label(root, text="Número de aristas:", **label_style).place(x=30, y=130)
entry_edges = tk.Entry(root, font=("Arial", 10))
entry_edges.place(x=200, y=130, width=200)

tk.Label(root, text="Longitud de la arista:", **label_style).place(x=30, y=180)
entry_edge_length = tk.Entry(root, font=("Arial", 10))
entry_edge_length.place(x=200, y=180, width=200)

button_style = {"bg": "#85C1E9", "font": ("Arial", 12, "bold"), "fg": "#FFFFFF", "relief": "raised", "borderwidth": 2}
button_calculate = tk.Button(root, text="Calcular", command=show_result, **button_style)
button_calculate.place(x=160, y=240, width=120, height=30)

label_result = tk.Label(root, text="", font=("Arial", 9, "italic"), bg="#EAEDED", fg="#1C2833")
label_result.place(x=10, y=300, width=435, height=40)
