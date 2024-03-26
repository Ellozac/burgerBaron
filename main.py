import customtkinter
from CTkMessagebox import CTkMessagebox
orders: list[str] = []
menuItems: list[list[str]] = [["Birgur", "$2"],
                              ["chicken biger", "$3"]]
order: list[list[str]] = []


class Main(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.label = customtkinter.CTkLabel(
            self, text="Welcome to Burger Baron!", height=100, width=100, font=(0, 20))
        self.orderButton = customtkinter.CTkButton(
            self, text="Order", command=self.viewOrderScreen)
        self.viewMenuButton = customtkinter.CTkButton(self, text="Cart")
        self.quitButton = customtkinter.CTkButton(
            self, text="Quit", command=self.exitProgram)
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
        self.buttonList = []
        super().__init__()
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        for index, i in enumerate(menuItems):
            customtkinter.CTkLabel(self, text=i[0]).grid(row=index, column=0)
            customtkinter.CTkLabel(self, text=i[1]).grid(row=index, column=1)
            self.buttonList.append(customtkinter.CTkButton(
                self, text="Add to Order", command=lambda i=i: self.addToOrder(i)))
            self.buttonList[index].grid(row=index, column=2)

    def addToOrder(self, item):
        order.append(item)
        if CTkMessagebox(message=f"{item[0]} Added to order\n your total is now ${getTotal(order)}",
                         icon="check", option_1="Pay Now", option_2="Add more").get() == "Pay Now":
            print("PAY NOW")
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
