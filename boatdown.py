from microbit import *
while True:
    boat1 = Image("09090:" "09090:" "09090:" "99999:" "09990")
    boat2 = Image("00000:" "09090:" "09090:" "09090:" "99999")
    boat3 = Image("00000:" "00000:" "09090:" "09090:" "09090")
    boat4 = Image("00000:" "00000:" "00000:" "09090:" "09090")
    boat5 = Image("00000:" "00000:" "00000:" "00000:" "09090")
    boat6 = Image("00000:" "00000:" "00000:" "00000:" "00000")
    a = (1, 2, 3)
    all_boats = [
        boat1, boat2, boat3, boat4, boat5, boat6, boat5, boat4, boat3, boat2,
        boat1
    ]
    display.show(all_boats, delay=300, loop=True)
