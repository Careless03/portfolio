# necessary libraries
import socket
import random

# optional library depending on implementation
import time

# ACKNOWLEDGEMENT OF ASSISTANCE
# CDT BECK helped by saying that my code wasn't working because I was on the virtual machine.
# As soon as I stopped using the virtual machine, my code started working fine.

""" 
REQUIREMENTS:

In this part of the project you need to accomplish a few things.
1. Setup a socket on the server and bind it to listen for a specific port (check the lesson 4 slides).

2. Listen for incoming messages (also in lesson 4 slides, don't forget to decode the message).

3. Modify the existing ping message to a pong message (check the PDF for specific instructions).
   There are a large variety of ways to do this, but please remember a string is an immutable object.

4. Implement some form of logic that ensures there is a 30% chance a message will not get a response.
   This is to replicate real world traffic issues that you likely won't encounter on EECSnet.

CONSIDERATIONS:
1. There are many ways to build this server, we recommend you keep it as simple as possible.

2. If you choose to implement a while loop architecture to listen for messages, please remember to end your
   program before you terminate your connection to your VM. Otherwise, you are potentially going to have to 
   learn how to find a specific process in Linux and terminate it. Ordinarily the program will stop running
   when you terminate your SSH connection, but there are no guarantees.

3. You do not need to have your server print anything out, but it is highly recommended that you do so while
   developing and testing your code so that you can determine what is working and what isn't.

4. We are not providing any skeleton code below, because you already have it in the client code and the lesson slides.
   Therefore you need to figure out the order necessary to make sure everything works. We recommend that before you
   begin coding you take the time to develop a plan and think through the necessary steps.

5. It is recommended that you ensure the socket connection is closed before your program ends. If you don't, you
   will be at the mercy of the operating system to release the bound port back to the system.

Good luck!
"""

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")
for i in range(10):
   message, clientAddress = serverSocket.recvfrom(2048)
   modifiedMessage = message.decode()
   random_number = random.randint(1,10) 
   final_message = "Pong" + modifiedMessage[4:]

   if random_number <= 3:
      continue
   else:
      serverSocket.sendto(final_message.encode(), clientAddress) 

serverSocket.close()