import customtkinter
import tkinter
import random

# List to store all orders made
orders: list[str] = []
# Menu items with their respective prices
menuItems: list[list[str]] = [
    ["Whopper Classic", "$10"], [
        "Chicken Big King", "$8"], ["Double Whopper", "$12"],
    ["Bacon King Deluxe", "$14"], [
        "Crispy Chicken Sandwich", "$8"], ["Whopper Jr.", "$6"],
    ["Spicy Chicken Jr.", "$6"], ["BBQ Bacon King", "$14"], ["Rodeo Burger", "$5"],
    ["Chicken Fries", "$6"]
]
# List to store the current order being made
order: list[list[str]] = []


class Main(customtkinter.CTk):
    """Main window"""

    def __init__(self) -> None:
        """Initialize the main window"""
        super().__init__()
        # Set window size to full screen
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        # Display welcome message
        self.label = customtkinter.CTkLabel(
            self,
            text="Welcome to Burger Baron!",
            height=100,
            width=100,
            font=(0, 20)
        )

        # Button to go to order screen
        self.orderButton = customtkinter.CTkButton(
            self,
            text="Order",
            command=self.viewOrderScreen,
            font=customtkinter.CTkFont("Helvetica", size=15)
        )

        # Button to view cart
        self.viewCartButton = customtkinter.CTkButton(
            self, command=self.viewCartScreen, text="Cart", font=customtkinter.CTkFont("Helvetica", size=15))

        # Button to quit the program
        self.quitButton = customtkinter.CTkButton(
            self,
            text="Quit",
            command=self.exitProgram,
            font=customtkinter.CTkFont("Helvetica", size=15)
        )
        # Pack the widgets
        self.label.pack()
        self.orderButton.pack(pady=10)
        self.viewCartButton.pack(pady=10)
        self.quitButton.pack(pady=10)

    def viewOrderScreen(self) -> None:
        """Switch to the order screen"""
        self.destroy()
        Order()

    def viewCartScreen(self) -> None:
        """Switch to the cart screen"""
        self.destroy()
        Cart()

    def exitProgram(self) -> None:
        """Exit the program"""
        self.destroy()


class Order(customtkinter.CTk):
    """Order screen"""

    def __init__(self):
        """Initialize the order screen"""
        super().__init__()
        self.buttonList = []
        # Set window size to full screen
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        # Display menu items
        for index, item in enumerate(menuItems):
            menu_label = customtkinter.CTkLabel(self, text=item[0], font=customtkinter.CTkFont(
                "Helvetica", size=15))
            menu_label.grid(row=index, column=0, padx=10)
            price_label = customtkinter.CTkLabel(self, text=item[1], font=customtkinter.CTkFont(
                "Helvetica", size=15))
            price_label.grid(row=index, column=1, padx=10)
            # Button to add item to order
            add_button = customtkinter.CTkButton(
                self,
                text="Add to Order",
                font=customtkinter.CTkFont("Helvetica", size=15),
                command=lambda item=item: self.add_to_order(item)
            )
            add_button.grid(row=index, column=2, padx=10, pady=5)
            self.buttonList.append(add_button)
        # Button to view current order
        view_order_button = customtkinter.CTkButton(self, text="View Order", command=self.view_my_order, font=customtkinter.CTkFont(
            "Helvetica", size=15))
        view_order_button.grid(row=index+1, column=0, padx=10)

    def view_my_order(self):
        """Switch to the cart screen"""
        self.destroy()
        Cart()

    def add_to_order(self, item):
        """Add item to order"""
        order.append(item)
        tkinter.messagebox.showinfo(title="New Item Added To Cart",
                                    message=f"{item[0]} Added to order\n your total is now ${self.get_total()}")

    def get_total(self) -> int:
        """Calculate the total cost of the order"""
        total = 0
        for item in order:
            total += int(item[1][1:])
        return total


class Cart(customtkinter.CTk):
    """Cart screen"""

    def __init__(self):
        """Initialize the cart screen"""
        super().__init__()
        # Set window size to full screen
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.buttonList = []
        # Display items in current order
        for index, item in enumerate(order):
            item_label = customtkinter.CTkLabel(self, text=item[0], font=customtkinter.CTkFont(
                "Helvetica", size=15))
            item_label.grid(row=index, column=0, padx=10)
            price_label = customtkinter.CTkLabel(self, text=item[1], font=customtkinter.CTkFont(
                "Helvetica", size=15))
            price_label.grid(row=index, column=1, padx=10)
            # Button to remove item from order
            remove_button = customtkinter.CTkButton(
                self,
                text="Remove",
                font=customtkinter.CTkFont("Helvetica", size=15),
                fg_color="Red",
                command=lambda item=item: self.removeFromOrder(item[0])
            )
            remove_button.grid(row=index, column=2, padx=10, pady=5)
            self.buttonList.append(remove_button)
        # Button to order more items
        order_more_button = customtkinter.CTkButton(self, text="Order More", command=self.menu, font=customtkinter.CTkFont(
            "Helvetica", size=15))
        order_more_button.grid(row=99, column=0, padx=10, pady=5)
        # Button to complete sale
        pay_button = customtkinter.CTkButton(self, text="Pay", command=self.pay, font=customtkinter.CTkFont(
            "Helvetica", size=15))
        pay_button.grid(row=99, column=1, padx=10, pady=5)
        # Display total cost
        total_label = customtkinter.CTkLabel(self, text=f"Your total is ${getTotal(order)}", font=customtkinter.CTkFont(
            "Helvetica", size=15))
        total_label.grid(row=99, column=2, padx=10, pady=5)

    def pay(self):
        """Process payment and confirm the order"""
        global order
        tkinter.messagebox.showinfo(title="Order Confirmed",
                                    message=f"Your Order number is {random.randint(1, 1000)}")
        orders.append(order)
        order = []
        self.destroy()
        Main()

    def menu(self):
        self.destroy()
        Order()

    def removeFromOrder(self, item):
        """removes an item from the current order"""
        for index, i in enumerate(order):
            if i[0] == item:
                order.pop(index)
                self.destroy()
                self.__init__()
                break


def getTotal(currentOrder: list[list[str]]) -> int:
    """
    currentOrder: 2d list containing strings
    returns int type of total cost of order
    """
    total = 0
    for i in order:
        total += int(i[1][1:])
    return total


if __name__ == "__main__":
    app = Main()
    app.mainloop()
