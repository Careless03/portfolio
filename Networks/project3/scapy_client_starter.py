import scapy.all as scapy               # used to create packets
from cryptography.fernet import Fernet  # you must use this to encrypt the message body
import json                             # a useful library for reading json files
from pathlib import Path                # our friend from project 2


"""
Installing scapy (on your VM):
Connect to EECSNet and log into VM
Open a terminal and run the following commands:
sudo apt install pip
sudo pip install scapy
"""

# You must use this class when creating your packets. The autograder is looking
# for messages that contain this specific header format, anything else will be
# ignored.
class CovertHeader(scapy.Packet):
    '''This class defines a header for use with your encrypted message.
    The seqNum field is used to help reorder messages, and len is the length
    of data following this header. 

    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    |       ID      |      LEN      |F|            SEQNUM           |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

                            Fig. CovertHeader
    '''
    name = "Covert Comms Channel Header"
    fields_desc = [scapy.ByteField("ID", 0), # ID used to pair packets
                   scapy.ByteField("len", 0), # length of data 
                   scapy.BitField("final", 0, 1), # bit set to 1 for final packet
                   scapy.BitField("seqNum", 0, 15) ] # sequence number of current message


# This is the class that the autograder will instantiate and use to send messages.
class ICMP_Client():

    """
    Every class created in python has an __init__(sel) method that is used
    to specify attributes about the class. This method is automatically called
    whenever an instance of the class is created, so you don't need to call it
    in your own code. You must have this when you submit to the autograder.
    """
    def __init__(self):
        # Our old friend from project 2. You can use it or not.
        self.base_path = Path(__file__).parent.absolute()
        # You must use this to encrypt your messages.
        # You can use it by saying self.encryption_object.encrypt(thing you want to encrypt)
        self.encryption_object = Fernet("SHARED KEY GOES HERE!!!")

        # TODO: Figure out what the ??? values should be in the configs.json file.
        # TODO: Use the configs.json file to initialize the remaining attributes.
    

    # This optional method will create a scapy socket for you to use.
    # You can feel free to use it or solve it your own way.
    def establish_socket(self):
        scapy.conf.L3socket = scapy.L3RawSocket
        self.sendSock = scapy.conf.L3socket()

    
    # This method will be called by the autograder to send the messages to the
    # server. It must exist, and calling it must result in all messages 
    # being sent to the listening server. How you handle that is up to you and 
    # your imagination / ingenuity.
    def transmit_messages(self):
        pass


    # Here are a series of things you need to figure out how to do. There may
    # be additional implied steps you need to add in when you make your plan.

    # TODO: Read in messages.
    # TODO: Break them into subsections based on max_size.
    # TODO: Figure out how many packets will be needed.
    # TODO: Figure out how to make pseudo-random padding.
    # TODO: Make sure that any packet without the max_size bytes is padded to size.
    # TODO: Figure out how to make the packets.
        # TODO: HINT!!! What layer does ICMP sit at? Do we need to encapsulate this packet?
        # TODO: Set the header information correctly.
    # TODO: Encrypt the packet bodies (DO AFTER EVERYTHING ELSE WORKS!)
    # TODO: Transmit the packets using self.sendSock or whatever method you
          # choose to implement.
    # TODO: Make sure everything runs by calling transmit messages.


# This code will allow you to run the file with the following command:
# sudo python3 scapy_client_starter.py
if __name__ == "__main__":
    # These are the same 2 steps that the autograder will take with your code.
    client = ICMP_Client()
    client.transmit_messages()
