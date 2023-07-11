import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class LoginForm:
    def __init__(self):
        self.base = tk.Tk()
        self.base.geometry("500x300")
        self.base.resizable(False, False)
        self.base.title("Login Form")
        self.base.configure(background="Black")

        self.lb0 = tk.Label(self.base, text="Login Form", width=15, background="Black", foreground="White",
                            font=("arial", 15))
        self.lb0.place(x=150, y=45)

        self.lb1 = tk.Label(self.base, text="USERNAME", width=15, background="Black", foreground="White",
                            font=("algerian", 12))
        self.lb1.place(x=50, y=120)
        self.user_name = tk.Entry(self.base, width=29)
        self.user_name.place(x=200, y=120)

        self.lb2 = tk.Label(self.base, text="PASSWORD", width=15, background="Black", foreground="White",
                            font=("algerian", 12))
        self.lb2.place(x=50, y=150)
        self.password = tk.Entry(self.base, show="*", width=29)
        self.password.place(x=200, y=150)

        self.login_button = tk.Button(self.base, text="Login", width=15, background="#FF3399", foreground="white",
                                      font=("arial", 12), command=self.login)
        self.login_button.place(x=160, y=220)

    def login(self):
        if len(self.user_name.get()) == 0 and len(self.password.get()) == 0 or (
                len(self.user_name.get()) == 0 or len(self.password.get()) == 0):
            pass
        elif len(self.user_name.get()) > 0 and len(self.password.get()) > 0:
            self.open_library()

    def open_library(self):
        # Logic to open the library or perform any other action
        lib = LibraryWindow()

    def run(self):
        self.base.mainloop()


class LibraryWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("LIBRARY")
        self.window.geometry("1000x400")

        self.window.resizable(False, False)
        self.make_tables()
        self.window.mainloop()

    def make_tables(self):
        # Create a Main Frame
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=1)

        # Create a Canvas
        my_canvas = tk.Canvas(main_frame)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the Canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the Canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        # Create another Frame INSIDE the Canvas
        second_frame = ttk.Frame(my_canvas)

        # Add the new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # Make the first table with the number of books

        # Make the second table with the number of the book
        for x in range(10):
            Button(second_frame, text=f"Book Number \n{x + 1}", height=5, width=30, background="#FF3399",
                   foreground="white").grid(row=x, column=0, pady=10, padx=10)

            # Make second Table with name of the book
        Button(second_frame, text="The name of the book \n Dune", height=5, width=30, background="#FF3399",
                      foreground="white").grid(row=0, column=1, pady=10, padx=10)

        Button(second_frame, text="The name of the book \n Martin Iden", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=1, column=1, pady=10,
                                                                     padx=10)

        Button(second_frame, text="The name of the book \n IT", height=5, width=30, background="#FF3399",
                      foreground="white").grid(row=2, column=1, pady=10, padx=10)

        Button(second_frame, text="The name of the book \n Carrie", height=5, width=30, background="#FF3399",
                      foreground="white").grid(row=3, column=1, pady=10, padx=10)

        Button(second_frame, text="The name of the book \n Sherlock Holmes", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=4, column=1, pady=10,
                                                                     padx=10)

        Button(second_frame, text="The name of the book \n Mumintroll", height=5, width=30, background="#FF3399",
                      foreground="white").grid(row=5, column=1, pady=10,
                                               padx=10)

        Button(second_frame, text="The name of the book \n The Great Gatsby", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=6, column=1, pady=10,
                                                                     padx=10)

        Button(second_frame, text="The name of the book \n  The Divine Comedy", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=7, column=1, pady=10,
                                                                     padx=10)

        Button(second_frame, text="The name of the book \n The Metomorphosis", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=8, column=1, pady=10,
                                                                     padx=10)

        Button(second_frame, text="The name of the book \n  Harry Potter and the Sorcerer's Stone", height=5,
                       width=30, background="#FF3399", foreground="white"
                       ).grid(
            row=9,
            column=1,
            pady=10,
            padx=10)

        # Author table
        Button(second_frame, text="Author : Frank Herbert \n Year of release : 1965 ", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=0, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : Jack London \n Year of release : 1909 ", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=1, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : Stiven King \n  Year of release : 1986 ", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=2, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : Stiven King  \n Year of release : 1974 ", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=3, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : Arthur Conan Doyle \n  Year of release : 1887", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=4, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : Tove Jansson  \n Year of release : 1952 ", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=5, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : F. Scott Fitzgerald \n  Year of release : 1925", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=6,
                                                                     column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : Dante Alighieri  \n  Year of release : 1472", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=7, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : Franz Kafka  \n Year of release : 1915", height=5, width=30,
                      background="#FF3399", foreground="white").grid(row=8, column=2,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Author : J. K. Rowling \n  Year of release : 1997", height=5, width=30,
                       background="#FF3399", foreground="white"
                       ).grid(
            row=9,
            column=2,
            pady=10,
            padx=10)

        # price table
        Button(second_frame, text="Price : 165$  ", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=0, column=3, pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 125$ ", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=1, column=3, pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 230$ ", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=2, column=3, pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 450$ ", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=3, column=3, pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 340$ ", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=4, column=3, pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 560$", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=5, column=3, pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 564$ ", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=6, column=3,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 72$ ", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=7, column=3,
                                                                     pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 69$", height=5, width=30, command=self.open_order,
                      background="#FF3399", foreground="white").grid(row=8, column=3, pady=10,
                                                                     padx=10)

        Button(second_frame, text="Price : 456$", height=5, width=30, command=self.open_order,
                       background="#FF3399", foreground="white"
                       ).grid(
            row=9,
            column=3,
            pady=10,
            padx=10)

    def open_order(self):
        order = OrderFormWindow()


class OrderFormWindow:
    def __init__(self):
        self.order = tk.Tk()
        self.order.geometry("500x500")
        self.order.resizable(False, False)
        self.order.title("Order Form")
        self.order.configure(background="Black")
        self.create_widgets()
        self.order.mainloop()

    def create_widgets(self):
        lb0 = tk.Label(self.order, text="Order Form ", width=15, background="Black", foreground="White",
                       font=("arial", 15))
        lb0.place(x=150, y=45)

        lab1 = Label(self.order, text="Enter Name", width=15, background="Black", foreground="White",
                     font=("algerian", 12))
        lab1.place(x=20, y=100)
        self.user_name_order = Entry(self.order, width=29)
        self.user_name_order.place(x=200, y=100)

        lab2 = Label(self.order, text="Enter Surname", width=15, background="Black", foreground="White",
                     font=("algerian", 12))
        lab2.place(x=17, y=140)
        self.user_surname_order = Entry(self.order, width=29)
        self.user_surname_order.place(x=200, y=140)

        lab3 = Label(self.order, text="Enter Email", width=15, background="Black", foreground="White",
                     font=("algerian", 12))
        lab3.place(x=19, y=180)
        self.user_email_order = Entry(self.order, width=29)
        self.user_email_order.place(x=200, y=180)

        lab4 = Label(self.order, text="Contact Number", width=15, background="Black", foreground="White",
                     font=("algerian", 12))
        lab4.place(x=19, y=220)
        self.user_number_order = Entry(self.order, width=29)
        self.user_number_order.place(x=200, y=220)

        list_of_cntry = ("United States", "Germany", "Ukraine", "Poland", "France")
        self.cv = StringVar()
        drplist = OptionMenu(self.order, self.cv, *list_of_cntry)
        drplist.config(width=15)
        self.cv.set("United States")
        lab5 = Label(self.order, text="Select Country", width=13, background="Black", foreground="White",
                     font=("algerian", 12))
        lab5.place(x=14, y=280)
        drplist.place(x=200, y=275)

        lab6 = Label(self.order, text="City", width=15, background="Black", foreground="White",
                     font=("algerian", 12))
        lab6.place(x=19, y=320)
        self.user_city_order = Entry(self.order, width=29)
        self.user_city_order.place(x=200, y=320)

        lab7 = Label(self.order, text="Street", width=15, background="Black", foreground="White",
                     font=("algerian", 12))
        lab7.place(x=19, y=360)
        self.user_street_order = Entry(self.order, width=29)
        self.user_street_order.place(x=200, y=360)

        button_order = Button(self.order, text="Order", width=10, background="#FF3399", foreground="White",
                              font=("algerian", 12), command=self.complete_order)
        button_order.place(x=200, y=400)

    def complete_order(self):
        if (
                len(self.user_name_order.get()) > 0
                and len(self.user_surname_order.get()) > 0
                and len(self.user_email_order.get()) > 0
                and len(self.user_number_order.get()) > 0
                and len(self.user_city_order.get()) > 0
                and len(self.user_street_order.get()) > 0
        ):
            messagebox.showinfo("Hooray", "Order Completed")
        else:
            pass


if __name__ == "__main__":
    login_form = LoginForm()
    login_form.run()