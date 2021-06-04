#!/usr/bin/env python3

# Filename: backup.py
# Author:   James Sanders
# Version:  1.0

# Import dependencies
import sys
import json
import os
from netmiko import ConnectHandler
from getpass import getpass

# Obtain device credentials
username = input('Username: ')
password = getpass(prompt='password: ')

BACKUP_DIR = "backups/"

# create backup directory
def create_backups_dir():
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)

# save config file
def save_config_to_file(hostname, config):
    filename =  f"{hostname}.cfg"
    with open(os.path.join(BACKUP_DIR, filename), "w") as f:
        f.write(config)

# connect to Cisco device
def connect_device(ip):
    device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': username,
            'password': password
            }
    return ConnectHandler(**device) 

# check we received correct argument.
if len(sys.argv) == 2:
	jsonfile = sys.argv[1]
	
elif len(sys.argv) == 1:
	sys.exit("Usage: {} <json file>".format(sys.argv[0]))	

elif len(sys.argv) > 2:
	print ("Too many arguments")
	sys.exit()

# Create backup folder if non-exist
create_backups_dir()

# gather device details from a JSON file
with open(jsonfile) as file:
    devices = json.load(file)

    # for each device, backup the running config
    for device in devices["devices"]:
        # connect to device
        net_connect = connect_device(device["ip"])
        # get output of "sh run" command
        config = net_connect.send_command("show run")
        # save output to file
        save_config_to_file(device["name"], config)
        # display message
        print("Successfully backed up: ", device["name"])

print("Task Completed.")