# app/ui/main_window.py
import tkinter as tk
from tkinter import ttk, messagebox
from app.core.task_manager import add_task, get_all_tasks

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("TaskFlow - Gestionnaire de tâches")
        self.root.geometry("800x600")

        # --- Titre ---
        ttk.Label(root, text="Gestionnaire de tâches 🗒️", font=("Segoe UI", 16)).pack(pady=15)

        # --- Formulaire ---
        form_frame = ttk.Frame(root)
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Titre :").grid(row=0, column=0, sticky="e")
        self.title_entry = ttk.Entry(form_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Description :").grid(row=1, column=0, sticky="e")
        self.desc_entry = ttk.Entry(form_frame, width=30)
        self.desc_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Priorité :").grid(row=2, column=0, sticky="e")
        self.priority_combo = ttk.Combobox(form_frame, values=["Basse", "Moyenne", "Haute"], width=27)
        self.priority_combo.current(1)
        self.priority_combo.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(form_frame, text="Date limite (AAAA-MM-JJ) :").grid(row=3, column=0, sticky="e")
        self.due_entry = ttk.Entry(form_frame, width=30)
        self.due_entry.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(form_frame, text="Ajouter la tâche", command=self.add_task_action).grid(row=4, columnspan=2, pady=10)
        ttk.Button(form_frame, text="Supprimer la tâche sélectionnée", command=self.delete_task_action).grid(row=5, columnspan=2, pady=5)

        # --- Liste des tâches ---
        self.tree = ttk.Treeview(root, columns=("Titre", "Priorité", "Date limite", "Statut"), show="headings", height=10)
        self.tree.pack(pady=15, fill="both", expand=True)

        for col in ("Titre", "Priorité", "Date limite", "Statut"):
            self.tree.heading(col, text=col)

        self.refresh_tasks()

    def add_task_action(self):
        title = self.title_entry.get()
        desc = self.desc_entry.get()
        priority = self.priority_combo.get()
        due_date = self.due_entry.get()

        if not title:
            messagebox.showwarning("Erreur", "Le titre est obligatoire.")
            return

        add_task(title, desc, priority, due_date)
        messagebox.showinfo("Succès", f"Tâche '{title}' ajoutée ✅")
        self.clear_form()
        self.refresh_tasks()

    def refresh_tasks(self):
        """Rafraîchit la liste des tâches dans le tableau."""
        for i in self.tree.get_children():
            self.tree.delete(i)

        for task in get_all_tasks():
            self.tree.insert("", "end", values=(task[1], task[3], task[4], task[5]))

    def clear_form(self):
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.priority_combo.current(1)
        self.due_entry.delete(0, tk.END)
    
    def delete_task_action(self):
        """Supprime la tâche sélectionnée dans le tableau."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une tâche à supprimer.")
            return

        task_values = self.tree.item(selected_item[0], "values")
        title = task_values[0]

        confirm = messagebox.askyesno("Confirmation", f"Supprimer la tâche '{title}' ?")
        if confirm:
            from app.core.task_manager import delete_task
            delete_task(title)
            self.tree.delete(selected_item[0])
            messagebox.showinfo("Supprimée", f"La tâche '{title}' a été supprimée.")

