import tkinter as tk
from tkinter import ttk

from Database import MyDatabase


class TicketTable:
    def search_button(self):
        print(self.search_by_name.get())
        self.data = self.databaseObject.search_by_name(self.search_by_name.get())
        self.clear_table()
        self.add_data_to_table()
        if self.search_by_name.get() == "":
            print("1")
            self.data = self.databaseObject.get_data()
            self.add_data_to_table()


    def delete_button(self):
        self.databaseObject.delete_all_table_data()
        self.clear_table()

    def __init__(self, root):
        self.databaseObject = MyDatabase()
        self.databaseObject.create_db("ticket")
        self.root = root
        self.data = self.databaseObject.get_data()
        self.root.title("Ticket List")
        tk.Label(master=self.root, text="welcome to program").pack(pady=10)
        self.search_by_name = tk.Entry(master=self.root)
        self.search_by_name.pack(pady=10)
        self.search_btn = tk.Button(master=self.root, text="search", command=self.search_button)
        self.search_btn.pack(pady=10)
        self.delete_btn = tk.Button(master=self.root, text="Delete All", command=self.delete_button)
        self.delete_btn.pack(pady=10)
        self.search_by_name.get()

        self.tree = ttk.Treeview(root, columns=("id", "Name", "Destination", "date"), show="headings")
        self.tree.heading("id", text="id")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("date", text="date")

        self.tree.pack(pady=20)

        # افزودن داده به جدول
        self.add_data_to_table()

    def add_data_to_table(self):
        data = self.data

        for row in data:
            self.tree.insert("", "end", values=row)

    def clear_table(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicketTable(root)
    root.mainloop()
