from fractions import Fraction
import math
import turtle

size = 3  # Grösse des Dreiecks

hd = input("Gib mir die Länge in dm: ")  # Länge
vd = input("Gib mir die Höhe in dm: ")  # Höhe


def slope_ratio(height, length):  # Der Bruch von der Steigung zu bekommen
    result = float(height) / float(length)
    return Fraction(result).limit_denominator()  # limit_denominator macht, dass es nicht zu Lange Zahlen zu bekommen


def slope_percent(height, length):  # gibt mir die Prozent des Steigungs
    return (float(height) / float(length))*100


def slope_angle(height, length):  # gibt mir den Winkel des Dreiecks (Ich habe keine ahnung, was inverse tan bedeuted)
    return round(math.degrees(math.atan(float(height)/float(length))), 2)  # (vielleicht in 3-er kommt es)


def results():  # gibt die resultaten
    print(f"{slope_ratio(vd, hd)} ratio")
    print(f"{slope_percent(vd, hd)}%")
    print(f"{slope_angle(vd, hd)}° grad")


def triangle(length, height, angle):  # macht das Dreieck
    if float(length) >= 150 or float(height) >= 150:  # um das Dreieck nicht zu gross zu machen (wenn zu grossen zahlen)
        turtle.forward(float(length))
        turtle.left(90)
        turtle.forward(float(height))
        turtle.left(90 + angle)
        turtle.forward(math.sqrt(float(length)**2 + (float(height)**2)))  # macht die hypothenuse
        turtle.mainloop()
    else:
        turtle.forward(float(length)*size)
        turtle.left(90)
        turtle.forward(float(height)*size)
        turtle.left(90 + angle)
        turtle.forward(math.sqrt(float(length) ** 2 + (float(height) ** 2))*size)
        turtle.mainloop()


results()
turtle.goto(-125, 0)
triangle(hd, vd, slope_angle(vd, hd))
