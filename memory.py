from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tap_count = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count
    
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    
    tap_count += 1

def check_game_status():
    "Detectar si todos los cuadros han sido destapados."
    if all(not h for h in hide):  # Si todos los elementos en hide son False
        display_message("¡Juego completo!", -200, -200)

def display_message(message, x, y):
    "Mostrar un mensaje en la pantalla."
    up()
    goto(x, y)
    color('black')
    write(message, font=('Arial', 20, 'normal'))


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 27, y)  
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    
    # Mostrar el número de taps
    up()
    goto(120, 180)
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 15, 'normal'))
    update()
    ontimer(draw, 100)

    # Checar si el juego ya terminó 
    check_game_status()


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
