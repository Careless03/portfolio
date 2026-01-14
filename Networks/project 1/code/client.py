import socket
import time

def format_time(time_in_seconds):
    t_no_format = time.localtime(time_in_seconds)
    formatted_time = time.strftime('%d %H:%M:%S %b %Y', t_no_format)
    return formatted_time


def compute_stats(time_deltas):
    max_time = max(time_deltas)
    min_time = min(time_deltas)
    avg_time = sum(time_deltas) / len(time_deltas) 
    return max_time, min_time, avg_time


def pretty_rtt(time_rcvd):
    return "RTT:" + str("%.4f" % (time_rcvd * 1000)) + "ms"

serverName = input("Enter server name: ") or 'localhost' 
print('Server Name: ', serverName)
serverPort = int(input("Enter server port: ") or 12000)
print('Server Port: ', serverPort)


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # <- socket object
(clientSocket)
try:

    timeout_float = 1.0
    clientSocket.connect((serverName, serverPort))
    clientSocket.settimeout(timeout_float) 
    
    time_deltas = []
    msg_count_sent = 0

    for sequence_number in range(10):
        time_sent = time.time()
        ping_message = 'ping ' + str(sequence_number + 1) + " " + format_time(time_sent)
        clientSocket.send(ping_message.encode()) 
        try: # <- EITHER The server responds with a "pong" message that you need to
        # the server responds
            server_message = clientSocket.recv(2048).decode() 
            time_rcvd = time.time() - time_sent
            time_deltas.append(time_rcvd)
            print(server_message, pretty_rtt(time_rcvd))
        except TimeoutError: 
            print("No response received for packet", sequence_number + 1)
        finally:
            msg_count_sent += 1
    if len(time_deltas) == 0:
        print("Connection to server failed.")
    else:
        max_time, min_time, avg_time = compute_stats(time_deltas)
        print("Pings sent:", msg_count_sent)
        print("Ping received:", len(time_deltas))
        print("Success rate:", str((len(time_deltas) / msg_count_sent *100))+"%")
        print("Maximum round trip time:", str(max_time), "ms")
        print("Minimum round trip time:", str(min_time), "ms")
        print("Average round trip time:", str(avg_time), "ms")
        print()
except Exception as e:
    print("Connection to server failed: ", e)
finally: 
    clientSocket.close()
    