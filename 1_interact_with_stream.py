import twitch 
import socket 
import logging
from emoji import demojize
import re

#--------------- STREAM twitch using SOCKETS
# source: https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/

# parameters 
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'is1bela'
token = 'oauth:yb5y1pc3eeuncy1y5hjms04w7irew7'
channel = '#mr_krobe'

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
                # sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                if "PRIVMSG" in resp: 
                    username, channel_from, message = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', demojize(resp)).groups()
                    message = message.replace('\r', '')
                    print(message)


    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()