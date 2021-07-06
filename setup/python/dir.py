#!/usr/bin/env python3

import pathlib
import glob 
import tkinter as tk
from tkinter import simpledialog
from time import sleep

ROOT = tk.Tk()
ROOT.withdraw()

# Search directory
print('Please wait, looking for a folder!')
currentDirectory = pathlib.Path(r'/home/')
currentPattern = "**/setup-aws-bastion-server/setup/"
for Dir in currentDirectory.glob(currentPattern):
    directory = Dir


# 1 Full Setup Bastion Server and Register Gitlab Runner
# -*- coding: utf-8 -*-
# Opening the file read-only
setup_server = str(directory) + str('/setup_server.yml')
file = open(setup_server, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/setup-server/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(setup_server, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()


# 2 Install Gitlab-Runner
# -*- coding: utf-8 -*-
# Opening the file read-only
gitlab_runner = str(directory) + str('/install_gitlab_runner.yml')
file = open(gitlab_runner, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/gitlab-runner-install/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(gitlab_runner, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()


# 3 Install Docker
# -*- coding: utf-8 -*-
# Opening the file read-only
docker = str(directory) + str('/install_docker.yml')
file = open(docker, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/docker-install/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(docker, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()


# 4 Install Docker Machine
# -*- coding: utf-8 -*-
# Opening the file read-only
docker_machine = str(directory) + str('/install_docker_machine.yml')
file = open(docker_machine, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/docker-machine-install/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(docker_machine, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()


# 5 Register Gitlab-Runner
# -*- coding: utf-8 -*-
# Opening the file read-only
register_gitlab_runner = str(directory) + str('/register_gitlab_runner.yml')
file = open(register_gitlab_runner, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/gitlab-runner-register/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(register_gitlab_runner, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()


# 6 AWS CLI
# -*- coding: utf-8 -*-
# Opening the file read-only
aws_cli = str(directory) + str('/aws-cli.yml')
file = open(aws_cli, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/aws-cli-install/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(aws_cli, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()


# 7 Cron AWS CLI
# -*- coding: utf-8 -*-
# Opening the file read-only
aws_cron = str(directory) + str('/aws-cron.yml')
file = open(aws_cron, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/aws-cron/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(aws_cron, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()


# 8 Only Setup Bastion
# -*- coding: utf-8 -*-
# Opening the file read-only
only_bastion = str(directory) + str('/only-setup-server.yml')
file = open(only_bastion, 'r')
lines = file.readlines()
lines[5] = '    - ' + str(directory) + '/roles/only-setup-server/vars/main.yml' + '\n'
# Close the file
file.close()
# Opening the file for writing
save_changes = open(only_bastion, 'w')
# Save the list of strings
save_changes.writelines(lines)
# Close the file
save_changes.close()
