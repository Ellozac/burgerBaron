import customtkinter
from CTkMessagebox import CTkMessagebox
orders: list[str] = []
menuItems: list[list[str, str]] = [["Whopper Classic", "$10"], ["Chicken Big King", "$8"], ["Double Whopper", "$12"], ["Bacon King Deluxe", "$14"], [
    "Crispy Chicken Sandwich", "$8"], ["Whopper Jr.", "$6"], ["Spicy Chicken Jr.", "$6"], ["BBQ Bacon King", "$14"], ["Rodeo Burger", "$5"], ["Chicken Fries", "$6"]]
order: list[list[str]] = []


class Main(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.label = customtkinter.CTkLabel(
            self,
            text="Welcome to Burger Baron!",
            height=100,
            width=100,
            font=(0, 20)
        )

        self.orderButton = customtkinter.CTkButton(
            self,
            text="Order",
            command=self.viewOrderScreen,
            font=customtkinter.CTkFont("Helvetica", size=15)
        )
        self.viewMenuButton = customtkinter.CTkButton(
            self, text="Cart", font=customtkinter.CTkFont("Helvetica", size=15))
        self.quitButton = customtkinter.CTkButton(
            self,
            text="Quit",
            command=self.exitProgram,
            font=customtkinter.CTkFont("Helvetica", size=15)
        )
        self.label.pack()
        self.orderButton.pack(pady=10)
        self.viewMenuButton.pack(pady=10)
        self.quitButton.pack(pady=10)

    def viewOrderScreen(self) -> None:
        self.destroy()
        Order()

    def viewCartScreen(self) -> None:
        self.destroy()
        Cart()

    def exitProgram(self) -> None:
        self.destroy()


class Order(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.buttonList = []
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        for index, i in enumerate(menuItems):
            customtkinter.CTkLabel(self, text=i[0], font=customtkinter.CTkFont(
                "Helvetica", size=15)).grid(row=index, column=0, padx=10)
            customtkinter.CTkLabel(self, text=i[1], font=customtkinter.CTkFont(
                "Helvetica", size=15)).grid(row=index, column=1, padx=10)
            self.buttonList.append(customtkinter.CTkButton(
                self,
                text="Add to Order",
                font=customtkinter.CTkFont("Helvetica", size=15),
                command=lambda i=i: self.addToOrder(i)
            ))
            self.buttonList[index].grid(row=index, column=2, padx=10, pady=5)
        self.returnToOrder = customtkinter.CTkButton(self, text="View Order", command=self.viewMyOrder, font=customtkinter.CTkFont(
            "Helvetica", size=15)).grid(row=index+1, column=0, padx=10)
        self.returnToOrder.grid(row=999, column=999)

    def viewMyOrder(self):
        self.destroy()
        Cart()

    def addToOrder(self, item):
        order.append(item)
        if CTkMessagebox(message=f"{item[0]} Added to order\n your total is now ${getTotal(order)}", icon="check", option_1="Pay Now", option_2="Add more").get() == "Pay Now":
            self.destroy()
            Cart()

    def removeFromOrder(self):
        pass


class Cart():
    def __init__(self):
        print("cart screen")


def getTotal(currentOrder: list[list[str]]) -> int:
    total = 0
    for i in order:
        total += int(i[1][1:])
    return total


if __name__ == "__main__":
    app = Main()
    app.mainloop()
