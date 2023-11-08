import requests
import time
import random
from sense_hat import SenseHat
sense = SenseHat()


def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    c = sense.stick.get_events()
    if len(c) > 0:
        event = c[0].direction
        if event =='Left':
            send_vel = True
            d_long = -1
            d_la = 0
        elif event == 'Right':
            send_vel = True
            d_long = 1
            d_la = 0
        elif event =='Up':
            send_vel = True
            d_long = 0
            d_la = 1
        elif event == 'Down':
            send_vel = True
            d_long = 0
            d_la = -1
        else:
            d_long = 0
            d_la = 0
            send_vel = False
    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
