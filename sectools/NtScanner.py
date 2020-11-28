#! /usr/bin/env python
import scapy.all as scapy
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--targert", dest = "targer", help="target IP / IP range")
    options =parser.parse_args()
    return options
    




def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    
    #this line for the macaddress broadcast
    broadcast = scapy.Ether(dst= "put the mac address here")

    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

    #this line to send and capture the ansewerd ip address in var
    
    ansewerd_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose=False)[0]
    print("IP\t\t\tMAC Adress\n---------------------------")
    client_list = []
    for element in ansewerd_list:
        client_dic = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        client_list.append(client_dic)
    return client_list
       
def print_data(result_list):
    print("IP\t\t\tMAC Adress\n---------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

    #this line is to know what field you want to set
    #scapy.ls()

result_list = scan('192.168.0.1/24')
print_data(result_list)