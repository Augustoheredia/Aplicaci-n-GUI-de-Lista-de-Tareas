import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tareas = []

        self.tarea_entry = tk.Entry(root, width=50)
        self.tarea_entry.pack(pady=10)

        self.agregar_button = tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea)
        self.agregar_button.pack()

        self.completar_button = tk.Button(root, text="Marcar como Completada", command=self.marcar_completada)
        self.completar_button.pack()

        self.eliminar_button = tk.Button(root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_button.pack()

        self.lista_tareas = tk.Listbox(root, width=50)
        self.lista_tareas.pack(pady=10)

        # Manejo del evento Enter para añadir tareas
        self.tarea_entry.bind("<Return>", lambda event: self.agregar_tarea())

    def agregar_tarea(self):
        tarea = self.tarea_entry.get()
        if tarea:
            self.tareas.append({"tarea": tarea, "completada": False})
            self.actualizar_lista_tareas()
            self.tarea_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista_tareas()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            del self.tareas[indice]
            self.actualizar_lista_tareas()

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "[Completada]" if tarea["completada"] else "[Pendiente]"
            self.lista_tareas.insert(tk.END, f"{estado} {tarea['tarea']}")

if _name_ == "_main_":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()