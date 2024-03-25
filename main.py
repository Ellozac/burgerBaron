import customtkinter
from ctkgridlayout import CTkGridLayout


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.label = customtkinter.CTkLabel(
            self, text="Welcome to Burger Baron!", height=100, width=100, font=(0, 20))
        self.orderButton = customtkinter.CTkButton(
            self, text="Order", command=self.orderScreen)
        self.viewMenuButton = customtkinter.CTkButton(self, text="Menu")
        self.quitButton = customtkinter.CTkButton(
            self, text="Quit", command=self.exitProgram)
        self.label.pack()
        self.orderButton.pack(pady=10)
        self.viewMenuButton.pack(pady=10)
        self.quitButton.pack(pady=10)

    def orderScreen(self):
        self.destroy()
        Order()

    def viewMenuScreen(self):
        pass

    def exitProgram(self):
        self.destroy()


class Order(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(
            f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.mainGrid = CTkGridLayout(
            master=self, column_count=2, spacing=15, padding=5)
        self.mainGrid.grid(row=0, column=0, sticky=customtkinter.BOTH)

    def addToOrder(self):
        pass

    def removeFromOrder(self):
        pass


if __name__ == "__main__":
    app = Main()
    app.mainloop()
