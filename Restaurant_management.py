import tkinter as tk
from tkinter import *
from tkinter import messagebox
class ROM:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")
        self.menu={
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }
        self.exchange_rate=26190
        frame=tk.Frame(root,bg="white")

        frame.place(relx=0.5,rely=0.5, anchor=tk.CENTER)

        tk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="blue"
            ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities = {}

        for i, (item, price) in enumerate(self.menu.items(), start=1):

            label = tk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12),
                bg="white",
                fg="black"
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = tk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry
        self.currency_var = tk.StringVar()
        self.currency_var.set("USD")
        tk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12),
            bg="white",
            fg="black"
        ).grid(row=len(self.menu)+1, column=0, padx=10, pady=5)

        currency_dropdown = tk.OptionMenu(frame, self.currency_var, "USD", "VND")
        currency_dropdown.grid(
            row=len(self.menu)+1,
            column=1,
            padx=10,
            pady=5
        )

        self.currency_var.trace("w", self.update_menu_prices)

        order_button = tk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu)+2,
            columnspan=3,
            padx=10,
            pady=10
        )

    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₫" if currency == "VND" else "$"
        rate = self.exchange_rate if currency == "VND" else 1

        for item, label in self.menu_labels.items():
            price = self.menu[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"

        currency = self.currency_var.get()
        symbol = "₫" if currency == "VND" else "$"
        rate = self.exchange_rate if currency == "VND" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()

            if quantity.isdigit():
                quantity = int(quantity)

                price = self.menu[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ROM(root)
    root.mainloop()