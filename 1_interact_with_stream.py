import twitch 
import socket 
import logging
from emoji import demojize
import re
from sendToArduino import *
from config import *

#--------------- STREAM twitch using SOCKETS
# source: https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/

planets = {"mercury": "100,28",
            "venus": "124,34", 
            "mars": "90,32",
            "jupiter": "40,50",
            "saturn": "130,60",
            "uranus": "112,70",
            "neptune": "123,80"}


def main():
    # socket initialization 
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\r\n".encode('utf-8'))

    try:
        while True:
            resp = sock.recv(2048).decode('utf-8')

            if resp.startswith('PING'):
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                if "PRIVMSG" in resp: 
                    username, channel_from, message = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', demojize(resp)).groups()
                    message = message.replace('\r', '')
                    #print(message)
                    message = message.lower()
                    
                    if "telescope" in message: 
                        if "move" in message: 
                            #telescope move x y
                            #send_to_arduino("move")

                            coor = message.lstrip("telescope move")
                            x_end = coor.find(",")
                            x_coor = coor[0:x_end]
                            #send_to_arduino(x_coor)

                            y_coor = coor[x_end+1:]
                            y_coor = y_coor.strip()
                            #send_to_arduino(x_coor)
                            s = "move;"+ x_coor + ";" + y_coor + ";"
                            print(s)
                            send_to_arduino(s)


                        
                        elif "planet"in message:
                            #send_to_arduino("planet")

                            planet = message.lstrip("telescope planet")
                            planet_arduino_coors = planets[planet]
                            planet_arduino_coors= planet_arduino_coors.replace('(', '').replace(')', '')
                            x_end = planet_arduino_coors.find(",")
                            x_coor = planet_arduino_coors[0:x_end]
                            #send_to_arduino(x_coor)

                            y_coor = planet_arduino_coors[x_end+1:]
                            y_coor = y_coor.strip()
                            #send_to_arduino(x_coor)
                            s = "planet;"+ x_coor + ";" + y_coor + ";"
                            print(s)
                            send_to_arduino(s)

                           

                        #print(message)
                    #send_to_arduino(message)
                    #sending it to the arduino 



    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()