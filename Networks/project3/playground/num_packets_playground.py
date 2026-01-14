import math

msg = 'ORIGINAL'
def get_msg(name_of_file):
    global msg
    print(msg)
    with open(name_of_file, 'r') as f:
        msg = f.read()

get_msg('message.txt')
print(msg)
print(len(msg))

num_of_pkts = math.ceil(len(msg)/80)
print(num_of_pkts)

last_pkt_num_bytes = len(msg)%80
print(last_pkt_num_bytes)