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


