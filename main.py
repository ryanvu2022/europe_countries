import turtle
import pandas

screen = turtle.Screen()
screen.title("Europe Countries Game")

image = "europe_blank_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("europe_countries.csv")
europe_countries = data.country.to_list()
guessed_countries = []

z = turtle.Turtle()
z.hideturtle()
z.penup()

z.color("#1C6758")
z.goto(265, -190)
z.write("ASIA", font=('Arial', 14, 'bold'))
z.goto(220, -215)
z.write("TURKEY", font=('Arial', 12, 'normal'))
z.goto(-150, -288)
z.write("AFRICA", font=('Arial', 14, 'bold'))

z.color("blue")
z.goto(-305, 80)
z.write("Atlantic Ocean", font=('Arial', 10, 'normal'))
z.goto(-130, -250)
z.write("Mediterranean Sea", font=('Arial', 10, 'normal'))
z.goto(-120, 200)
z.write("Norwegian Sea", font=('Arial', 10, 'normal'))
z.goto(-115, 55)
z.write("North Sea", font=('Arial', 10, 'normal'))
z.goto(220, -140)
z.write("Black Sea", font=('Arial', 10, 'normal'))


while len(guessed_countries) < 41:
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/41 Countries Correct",
                                      prompt="What's another country's name?").title()
    if answer_country == "Exit":
        missing_countries = list(set(europe_countries) - set(guessed_countries))
        countries_to_learn = {
            "Country": missing_countries
        }
        df = pandas.DataFrame(countries_to_learn)
        df.to_csv("countries_to_learn.csv")
        break
    if answer_country in europe_countries:
        if answer_country not in guessed_countries:
            guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(int(country_data.x), int(country_data.y))
        t.color("#CF0A0A")
        t.write(answer_country, font=('Arial', 8, 'bold'))
    if len(guessed_countries) == 41:
        z = turtle.Turtle()
        z.hideturtle()
        z.penup()
        z.goto(-200, 250)
        z.color("#00005C")
        z.write("CONGRATULATIONS. YOU WIN", font=('Arial', 20, 'bold'))


screen.exitonclick()
