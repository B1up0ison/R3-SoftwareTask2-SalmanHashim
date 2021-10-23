from pynput import keyboard
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 1337

s.connect((host, port))

speed = 0
print("Please make sure to use keys W,A,S,D only! \nPlease enter a value from 0-5 to change speed value:")


def on_press(key):
    global speed
    realspeed = speed * 51
    if key.char == '0':
        speed = 0
        zero = "Speed has been set to 0"
        s.send(zero.encode())
        print(zero)
    elif key.char == '1':
        speed = 1
        one = "Speed has been set to 1"
        s.send(one.encode())
        print(one)
    elif key.char == '2':
        speed = 2
        two = "Speed has been set to 2"
        s.send(two.encode())
        print(two)
    elif key.char == '3':
        speed = 3
        three = "Speed has been set to 3"
        s.send(three.encode())
        print(three)
    elif key.char == '4':
        speed = 4
        four = "Speed has been set to 4"
        s.send(four.encode())
        print(four)
    elif key.char == '5':
        speed = 5
        five = "Speed has been set to 5"
        s.send(five.encode())
        print(five)

    elif key.char == 'w':
        doubleu = "[f" + str(realspeed) + "][f" + str(realspeed) + "][f" + str(realspeed) + "][f" + str(realspeed) + "]"
        print(doubleu)
        s.send(doubleu.encode())
    elif key.char == 'a':
        ay = "[r" + str(realspeed) + "][r" + str(realspeed) + "][f" + str(realspeed) + "][f" + str(realspeed) + "]"
        print(ay)
        s.send(ay.encode())
    elif key.char == 's':
        es = "[r" + str(realspeed) + "][r" + str(realspeed) + "][r" + str(realspeed) + "][r" + str(realspeed) + "]"
        print(es)
        s.send(es.encode())
    elif key.char == 'd':
        de = "[f" + str(realspeed) + "][f" + str(realspeed) + "][r" + str(realspeed) + "][r" + str(realspeed) + "]"
        print(de)
        s.send(de.encode())
    else:
        print('You entered: {0} \nPlease enter W,A,S,D for movement and 0-5 for speed values'.format(key.char))


with keyboard.Listener(
        on_press=on_press, ) as listener:
    listener.join()