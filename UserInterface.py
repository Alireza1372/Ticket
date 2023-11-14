from Database import MyDatabase
import tkinter as tk
from tkinter import messagebox
from searchsreen import TicketTable

options = ["tehran", "london", "paris", "dubai", "new york"]


class GraphicUserInterface:

    def __init__(self):

        self.databaseObject = MyDatabase()
        self.databaseObject.create_db("ticket")
        self.databaseObject.create_table("user")
        self.user_name = ""
        self.user_destination = ""
        self.user_trip_time = ""

    def main_screen(self):
        main_window = tk.Tk()
        main_frame = tk.Frame(master=main_window, width=400, height=300)
        main_frame.pack()

        def submit_button():
            self.user_name = costumer_name.get()
            self.user_destination = selected_option.get()
            self.user_trip_time = costumer_date.get()
            username = costumer_name.get()
            destination = selected_option.get()
            time = costumer_date.get()
            if (username != "" and destination != "" and time != " "):
                messagebox.showinfo("success", "the ticket has been added")
                self.databaseObject.insert_data(username, destination, time)
            self.databaseObject.get_data()


        def close_button():
            main_window.destroy()

        def ticket_button():
            root = tk.Tk()
            search_screen = TicketTable(root)
            #app = TicketTable(root)




        tk.Label(master=main_frame, text="welcome to program").place(x=150, y=0)

        tk.Label(master=main_frame, text="Please Enter Your first name:").place(x=8, y=32)
        costumer_name = tk.Entry(master=main_frame, width=30)
        costumer_name.place(x=170, y=32)
        tk.Label(master=main_frame, text="Please Enter Your destination City:").place(x=8, y=64)
        selected_option = tk.StringVar(main_frame)
        selected_option.set(options[0])
        costumer_destination = tk.OptionMenu(main_frame, selected_option, *options)
        costumer_destination.place(x=198, y=60)
        tk.Label(master=main_frame, text="Trip date yyyy/mm/dd :").place(x=8, y=96)
        costumer_date = tk.Entry(master=main_frame, width=30)
        costumer_date.place(x=170, y=96)

        tk.Button(master=main_frame, text="GO TO THE TICKET LIST SCREEN", command=ticket_button).place(x=100, y=150)


        submit_btn = tk.Button(master=main_frame, text="Submit", command=submit_button)
        submit_btn.place(x=100,y=250)
        close_btn = tk.Button(master=main_frame, text="Exit", command=close_button)
        close_btn.place(x=200, y=250)
        main_window.mainloop()


main_screen = GraphicUserInterface()
main_screen.main_screen()
