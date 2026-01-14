# libraries you will need for this project
import socket
import time
import random

######### Helper Functions #########
# It would probably be useful to have some helper functions to handle things that will be occurring frequently


# this function takes in a time in seconds and returns a string with the correctly formatted time
def format_time(time_in_seconds):
    # take a look at the project instructions for part 1 to see exactly how the time should be formatted
    #TODO: Figure out how to turn a time_in_seconds into the desired string
    # Hint1: Look up the time.localtime method
    # Hint2: Look up the time.strftime method
    current = time.localtime(time_in_seconds)
    formatted_time = time.strftime("%d %H:%M:%S %b %Y",current)

    return formatted_time


# This function takes in a list of times, computes and returns the 
# necessary stats on them.
def compute_stats(time_deltas: list):
    #TODO: Calculate these
    max_time = max(time_deltas)
    min_time = min(time_deltas)
    avg_time = sum(time_deltas)/len(time_deltas)

    return max_time, min_time, avg_time

### User Inputs ###
# TODO - Get server IPv4 address or name from user (either input() or read from file)
# TODO - Get server port number from user (either input() or read from file) 
# NOTE: What datatypes should these be?
ipAddress = input("Enter server number: ")
print(f"Server Name: {ipAddress}")
portNumber = input("Enter server port: ")
print(f"Server Port: {portNumber}")

# Create a socket object
# NOTE: Do not change this line. AF_INET means you are using IPv4 addresses and 
#       SOCK_DGRAM means your are using UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # <- socket object (clientSocket)


try: 
    # Now that you have a socket object, you need to try and connect to the server

    #TODO: Establish a connection to the server
    # Hint: Don't forget that you are supposed to wait a maximum of 1 second for 
    # a response then stop waiting. Configure the connection for timeout.
    clientSocket.connect((ipAddress,int(portNumber)))
    clientSocket.settimeout(1.0)

    #TODO: What variables do you need to keep track of information between ping 
    #      messages?
    # Hint: What are the helper functions expecting?
    failure = 0
    RTT = []
    # Send the ping message 10 times
    
    for sequence_number in range(10):
        # TODO: Create the ping message as specified in the Project 1 writeup.
        start_time = time.time()
        ping_message = f'ping {sequence_number+1} {format_time(start_time)}'
        # Send the message
        clientSocket.send(ping_message.encode()) # You need to encode messages 
                                                    # before you send them

        try: # <- EITHER The server responds with a "pong" message that you need to process.
            
            # the server responds
            server_message = clientSocket.recv(2048).decode() # You need to decode messages when you receive them

            # process received message
            # TODO: Update appropriate variables
            # TODO: Provide update message to user (reference Project 1 writeup)
            end_time = time.time()
            RTT.append((end_time-start_time)*1000)
            pong_message = f"Pong {sequence_number+1} {format_time(end_time)} RTT: {(end_time-start_time)*1000} ms"
            pong_message = server_message
            print(pong_message)
            
        except TimeoutError: # <- there is a specific exception you should be checking for related to timing out.
            # OR There is no response message from the server.
            failure += 1
            # there is no response, so notify user by sending output to the CLI (command-line-interface)
            print("No response received for packet", sequence_number)

    
    # what if you finish all 10 pings and even though you got a connection you got no responses?
    # TODO: Handle this corner case by alerting the user each message timed out.
    if failure == 10:
        print("No pings were ponged")
            
    # otherwise, you got some responses and you can generate stats
    # TODO: Use the helper function(s) and then print out the results
            # Make sure you match the instructions!
    maximum, minimum, average = compute_stats(RTT)
    print("Number of messages sent: 10")
    print(f"Number of messages recieved {10-failure}")
    print(f"Success rate: {(10-failure)*10}%")
    print(f"Max RTT: {maximum} ms")
    print(f"Min RTT: {minimum} ms")
    print(f"Average RTT: {average} ms")



except Exception as e:
    # Otherwise, the connection failed and you should probably let the user know
    print("Connection to server failed: ", e)

# make sure you close the connection before exiting the program
finally: # <- in the try-except-finally exception handling, finally is always executed

    #TODO: Close the connection
    clientSocket.close()

