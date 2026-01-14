# required library imports
import scapy.all as scapy
from cryptography.fernet import Fernet
import json
from pathlib import Path
import signal

# potentially useful libraries
import time
import collections
from cryptography.fernet import InvalidToken

    ########################################################################
    ###################### DO NOT ALTER COVERT HEADER ######################
    ######################################################################## 
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
    

class ICMP_Server():
    # This is the constructor method for the ICMP_Server() class. It will be
    # automatically called when you create the class. Just like in part 1 you 
    # can use this to create / store any attributes you believe will be needed
    # in your later methods. Some of them have already been provided for you,
    # but you may add whatever else you desire to them.
    def __init__(self):


        ########################################################################
        ###################### DO NOT ALTER THESE ##############################
        ######################################################################## 
        
        # used with CTRL-C and the provided signal_handler to shut the server down
        self.listening = True

        # use self.store_message(id, message) to put your re-assembled message
        # into this dictionary attribute. DO NOT DIRECTLY ACCESS THIS!
        self.compiled_messages = {}

        self.base_path = Path(__file__).parent.absolute()

        # read in the configs file
        with open(self.base_path / 'configs.json','r') as f:
            configs = json.load(f)
        
        self.key = configs['shared_key']
        self.destination = configs["destination_address"]
        self.output_path = configs["output_path"]
        # use self.encryption_object.decrypt() to decrypt the sent messages
        self.encryption_object = Fernet(self.key)

        ################## MAKE ANY NEW ATTRIBUTES HERE ########################




    ########################################################################
    #                         Provided Helper Methods                      #
    #                   You Don't Need To Modify Any Of These              #
    #                    But You Do Need to Use Some Of Them               #
    ########################################################################

    # DO NOT MODIFY THIS: It shuts your server down with CTRL-C. You don't need
    # to do anything with this method.
    def signal_handler(self, signal, frame):
        print("\nCtrl+C captured, stopping the server...")
        print("Please ignore any remaining messages.")
        self.listening = False
        # final packet sent to prevent scapy's sniff function from blocking
        shutdown_pkt = scapy.IP(dst="127.0.0.1")/scapy.ICMP()/scapy.Raw(load=b'shutdown')
        scapy.send(shutdown_pkt)

    # This is the same socket object that was provided in part 1.
    # We have already implemented its use below in self.sniff_for_packets
    def build_socket(self):
        scapy.conf.L3socket = scapy.L3RawSocket
        self.receive_sock = scapy.conf.L3socket()

    # This helper method is for those who choose to implement the bonus portion
    # of the project. You should call it if a packet does not arrive to update the
    # message for the autograder. See the project specification for more details.
    def missing_msg(self, pkt_num):
        filler = f" ... missing data from packet {pkt_num} ... "
        return filler
    
    # This helper method is used to store the fully re-assembled message into
    # self.compiled_messages. This is to avoid you making a simple mistake like
    # changing the name of the attribute.
    def store_message(self, id, message):
        self.compiled_messages[id] = message


    # This helper method will take your self.compiled_messages dictionary and
    # write the contents to a JSON file. The compiled_messages.json will be
    # used by the autograder to determine if you have properly handled all messages.
    # Please DO NOT attempt to hard code the messages into this. The autograder has
    # different messages than what we have given you.
    def write_json(self):
        with open(Path(self.output_path),'w') as f:
            json.dump(self.compiled_messages, f)


    # This method serves to setup the server and start listening for packets.
    # You don't need to change anything here.
    def run_server(self):
        self.build_socket()
        self.sniff_for_packets()

    ########################################################################
    #                           Main Logic Methods                         #
    #    See The Project Specification and Comments for More Information   #
    ########################################################################
    
    # This method is called by the self.start_server method and will cause 
    # Scapy to actively listen for new packets arriving. We have provided the
    # code to get you started here, but it is up to you to figure out what to do
    # when a new packet arrives. See the project specification for more details.
    def sniff_for_packets(self):
        print("Server is listening for messages...")
        while self.listening:
            try:
                # this line of code will wait for a single packet to arrive
                # and then call the self.process_icmp_only method.
                self.receive_sock.sniff(count= 1, prn=self.process_icmp_only)
                #### YOUR CODE GOES HERE ####


            except Exception as e:
                print("Error at sniff try/except.")
                print(e)
                continue
            
        # The server will listen forever until you press CTRL-C.
        print("Server stopped.")

    # This method will be called whenever a packet arrives and is sniffed in the
    # self.sniff_for_packets method. You should implement your logic to process
    # a packet here. See the project specification and recommended approach below
    # for more details.
    def process_icmp_only(self, pkt):
        #### YOUR CODE GOES HERE ####
        pass

    #################### Put Any Additional Methods Here ######################
 





########################## Recommended Approach ################################

#TODO: Make a plan before you start coding!

#TODO: Make sure any values you need to initialize (in addition to those already
     # provided) have been initialized.
#TODO: Inside self.process_icmp_only(self, pkt) do the following things:
    #TODO: Determine if the packet is the correct type / code
    #TODO: Determine if there is a CovertHeader
        #TODO: If no, skip the packet
        #TODO: If yes, decrypt the packet and extract all relevant information
        #       in order to put the message back together.
        #TODO: Figure out how to store that information so you can retreive it later
#TODO: Figure out how to determine you have all of the packets (or how to handle
    #  not having all of the packets if you choose to do the bonus).
#TODO: Once you have all of the packets, reassemble the message in the correct order.
#TODO: Save the message using self.store_message(id, message)
#TODO: Write the information to a json file using self.write_json()
#TODO: Make sure you are ready to process the next packet.

###################### DON'T CHANGE ANYTHING BELOW THIS ########################
if __name__ == "__main__":
    # this line instantiates (fancy word for allocating memory) the server
    server = ICMP_Server()
    # Register the signal handler so that you can use CTRL-C to stop it.
    signal.signal(signal.SIGINT, server.signal_handler)
    # start the server running
    server.run_server()