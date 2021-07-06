#!/usr/bin/env python3

import pathlib
import tkinter as tk
from tkinter import simpledialog
from time import sleep
#import subprocess

ROOT = tk.Tk()
ROOT.withdraw()

print('Please wait, looking for a folder!')

def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

for i in range(101):
    progress(i)
    sleep(0.1)

# Search directory
currentDirectory = pathlib.Path(r'/home/')
currentPattern = "**/setup-aws-bastion-server/"
for Dir in currentDirectory.glob(currentPattern):
    directory = Dir
#paths = [line[2:] for line in subprocess.check_output("find / -name '**/setup-aws-bastion-server/'", shell=True).splitlines()]
#print(paths)

# Edit Hosts File
# Requests new parameters
gitlab_runner_amazonec2_access_key = simpledialog.askstring(title="Enter the parameters you need",
prompt="Amazaon Access Key (example: 825WLSv2vJcsaCMwHO2z): ")
#if not gitlab_runner_amazonec2_access_key:
while bool(gitlab_runner_amazonec2_access_key) == False:
     gitlab_runner_amazonec2_access_key = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Amazaon Access Key (example: 825WLSv2vJcsaCMwHO2z): ")

#
gitlab_runner_amazonec2_secret_key = simpledialog.askstring(title="Enter the parameters you need",
prompt="Amazon Secret Key (example: lFCIzKGoD0zHJsEcmVnge04miFLKzhTnHQ9l): ")
while bool(gitlab_runner_amazonec2_secret_key) == False:
     gitlab_runner_amazonec2_secret_key = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Amazon Secret Key (example: lFCIzKGoD0zHJsEcmVnge04miFLKzhTnHQ9l): ")

gitlab_runner_amazonec2_region = simpledialog.askstring(title="Enter the parameters you need",
prompt="Just click OK to use the default options\nAmazon Region (example/default: eu-central-1): ") or "eu-central-1"
# 1
# -*- coding: utf-8 -*-
# Opening the file read-only
aws_cli_defaults = str(directory) + str('/setup/roles/aws-cli-install/defaults/main.yml')
file = open(aws_cli_defaults, 'r')
lines = file.readlines()
lines[2] = 'aws_access_key: ' + gitlab_runner_amazonec2_access_key + '\n'
lines[3] = 'aws_secret_key: ' + gitlab_runner_amazonec2_secret_key + '\n'
lines[4] = 'aws_region: ' + gitlab_runner_amazonec2_region + '\n'
# Close the file
file.close()

# Opening the file for writing
save_changes = open(aws_cli_defaults, 'w')
 
# Save the list of strings
save_changes.writelines(lines)
 
# Close the file
save_changes.close()

# 2
# -*- coding: utf-8 -*-
# Opening the file read-only
aws_cron_defaults = str(directory) + str('/setup/roles/aws-cron/defaults/main.yml')
file = open(aws_cron_defaults, 'r')
lines = file.readlines()
lines[2] = 'aws_access_key: ' + gitlab_runner_amazonec2_access_key + '\n'
lines[3] = 'aws_secret_key: ' + gitlab_runner_amazonec2_secret_key + '\n'
lines[4] = 'aws_region: ' + gitlab_runner_amazonec2_region + '\n'
# Close the file
file.close()

# Opening the file for writing
save_changes = open(aws_cron_defaults, 'w')
 
# Save the list of strings
save_changes.writelines(lines)
 
# Close the file
save_changes.close()

# 3
# -*- coding: utf-8 -*-
# Opening the file read-only
only_setup_server_defaults = str(directory) + str('/setup/roles/only-setup-server/defaults/main.yml')
file = open(only_setup_server_defaults, 'r')
lines = file.readlines()
lines[6] = 'aws_access_key: ' + gitlab_runner_amazonec2_access_key + '\n'
lines[7] = 'aws_secret_key: ' + gitlab_runner_amazonec2_secret_key + '\n'
lines[8] = 'aws_region: ' + gitlab_runner_amazonec2_region + '\n'
# Close the file
file.close()

# Opening the file for writing
save_changes = open(only_setup_server_defaults, 'w')
 
# Save the list of strings
save_changes.writelines(lines)
 
# Close the file
save_changes.close()
