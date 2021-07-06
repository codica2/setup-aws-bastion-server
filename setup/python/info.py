#!/usr/bin/env python3

import pathlib
from os import path
from pathlib import Path
import tkinter as tk
from tkinter import simpledialog
from time import sleep

ROOT = tk.Tk()
ROOT.withdraw()

# Search directory
print('Please wait, looking for a folder!')
currentDirectory = pathlib.Path(r'/home/')
currentPattern = "**/setup-aws-bastion-server/"
for Dir in currentDirectory.glob(currentPattern):
    directory = Dir
print(directory)
# Edit Hosts File
# Requests new parameters
inventory_group_name = simpledialog.askstring(title="Enter the parameters you need",
prompt="Group inventory name (example: webservers): ")
while bool(inventory_group_name) == False:
     inventory_group_name = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Group inventory name (example: webservers): ")

ansible_hostname = simpledialog.askstring(title="Enter the parameters you need",
prompt="Server HostName (example: test_server): ")
while bool(ansible_hostname) == False:
     ansible_hostname = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Server HostName (example: test_server): ")

host = simpledialog.askstring(title="Enter the parameters you need",
prompt="Server Host IP (example: 1.1.1.1): ")
while bool(host) == False:
     host = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Server Host IP (example: 1.1.1.1): ")

user = simpledialog.askstring(title="Enter the parameters you need",
prompt="Server User (example: ubuntu): ")
while bool(user) == False:
     user = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Server User (example: ubuntu): ")

pemkey = simpledialog.askstring(title="Enter the parameters you need",
prompt="Server Pem Key (example: /home/user/.ssh/'key'.pem): ")
while bool(pemkey) == False:
     pemkey = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Server Pem Key (example: /home/user/.ssh/'key'.pem): ")

port = simpledialog.askstring(title="Enter the parameters you need",
prompt="Ansible port (example/default: 22): ") or '22'
# 1
# -*- coding: utf-8 -*-
# Opening the file read-only
Check = path.exists(str(directory) + str('/setup/hosts/hosts'))
if Check == True:
    print('Hosts file exists')
hosts = str(directory) + str('/setup/hosts/hosts')
file = open(hosts, 'r')
lines = file.readlines()
lines[0] = '[' + inventory_group_name + ']' + "\n"
lines[1] = ansible_hostname + ' ' + 'ansible_host=' + host +  "\n"
lines[2] = '[' + inventory_group_name + ':vars' + ']' + "\n"
lines[3] = 'ansible_port=' + port + "\n"
lines[4] = 'ansible_user=' + user + "\n"
lines[5] = 'ansible_ssh_private_key_file=' + pemkey + "\n"
print('Settings were written to file')
# Close the file
file.close()

# Opening the file for writing
save_changes = open(hosts, 'w')
 
# Save the list of strings
save_changes.writelines(lines)
 
# Close the file
save_changes.close()


# 2
# -*- coding: utf-8 -*-
# Opening the file read-only
#group_vars = str(directory) + str('/setup/hosts/group_vars/setup_bastion_server.yml')
#file = open(group_vars, 'r')
#lines = file.readlines()
#lines[1] = 'ansible_user: ' + user + '\n'
#lines[2] = 'ansible_ssh_private_key_file: ' + pemkey + '\n'
# Close the file
#file.close()

# Opening the file for writing
#save_changes = open(group_vars, 'w')
 
# Save the list of strings
#save_changes.writelines(lines)
 
# Close the file
#save_changes.close()
