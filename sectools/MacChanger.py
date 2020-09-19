#!/usr/bin/env python3
import optparse
import subprocess
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest="interface",help="the interface to change its mac")
    parser.add_option("-m","--mac",dest="new_mac",help="New MAC address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[*] Specify an interface, check --help")
    elif not options.new_mac:
        parser.error("[*] Specify a  MAC address, check --help")
    return options

def mac_changer(interface, new_mac):
    print("[+] Changing MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subporcess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w:", str(ifconfig_result))
    if mac_address_search_result:
        print(mac_address_search_result.group(0))
    else:
        print("[*] Could not read MAC address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("your current MAC address is " + str(current_mac))

mac_changer(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if options.new_mac == current_mac:
    print("[*] MAC address was changed successfuly to " + current_mac)
else:
    print("[*] Somthing went wrong your MAC has not changed")