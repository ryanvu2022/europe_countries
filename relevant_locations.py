from turtle import Turtle


class RelevantLocations(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def add_continents(self):
        self.color("#1C6758")
        self.goto(265, -190)
        self.write("ASIA", font=('Arial', 14, 'bold'))
        self.goto(220, -215)
        self.write("TURKEY", font=('Arial', 12, 'normal'))
        self.goto(-150, -288)
        self.write("AFRICA", font=('Arial', 14, 'bold'))

    def add_seas(self):
        self.color("#0008C1")
        self.goto(-305, 80)
        self.write("Atlantic Ocean", font=('Arial', 10, 'normal'))
        self.goto(-130, -250)
        self.write("Mediterranean Sea", font=('Arial', 10, 'normal'))
        self.goto(-120, 200)
        self.write("Norwegian Sea", font=('Arial', 10, 'normal'))
        self.goto(-115, 55)
        self.write("North Sea", font=('Arial', 10, 'normal'))
        self.goto(220, -140)
        self.write("Black Sea", font=('Arial', 10, 'normal'))

    def add_exit_instruction(self):
        self.color("#711A75")
        self.goto(-330, -310)
        self.write("Type 'exit' to quit the game", font=('Arial', 10, 'italic'))
