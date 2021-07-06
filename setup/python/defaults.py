#!/usr/bin/env python3

import pathlib
import tkinter as tk
from tkinter import simpledialog
from time import sleep

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

# Edit Hosts File
# Requests new parameters
gitlab_runner_name = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Name (example: test-runner): ")
while bool(gitlab_runner_name) == False:
     gitlab_runner_name = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Gitlab Runner Name (example: test-runner): ")
gitlab_runner_coordinator_url = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner URL (example/default: https://gitlab.com/): ") or "https://gitlab.com/"
gitlab_runner_registration_token = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Registory Token (example: 7s6kFUKUx0iwFiTb5YYu): ")
while bool(gitlab_runner_coordinator_url) == False:
    gitlab_runner_registration_token = simpledialog.askstring(title="Enter the parameters you need",
    prompt="Gitlab Runner Registory Token (example: 7s6kFUKUx0iwFiTb5YYu): ")
gitlab_runner_executor = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Executor (example/default: docker+machine): ") or "docker+machine"
gitlab_runner_docker_image = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Docker Images (example/default: alpine:latest): ") or "alpine:latest"
gitlab_runner_limit = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runners Limits (example/default: 2): ") or "2"
gitlab_runner_s3_server_address = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner S3 Address (example/default: s3.amazonaws.com): ") or "s3.amazonaws.com"
gitlab_runner_s3_access_key = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner S3 Accees Key (example: 825WLSv2vJcsaCMwHO2z): ")
while bool(gitlab_runner_s3_access_key) == False:
    gitlab_runner_s3_access_key = simpledialog.askstring(title="Enter the parameters you need",
    prompt="Gitlab Runner S3 Accees Key (example: 825WLSv2vJcsaCMwHO2z): ")
gitlab_runner_s3_secret_key = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitalb Runner S3 Secret Key (example: lFCIzKGoD0zHJsEcmVnge04miFLKzhTnHQ9l): ")
while bool(gitlab_runner_s3_access_key) == False:
    gitlab_runner_s3_secret_key = simpledialog.askstring(title="Enter the parameters you need",
    prompt="Gitalb Runner S3 Secret Key (example: lFCIzKGoD0zHJsEcmVnge04miFLKzhTnHQ9l): ")
gitlab_runner_s3_bucket_name = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner S3 Bucket Name (example: test-runner): ")
while bool(gitlab_runner_s3_bucket_name) == False:
    gitlab_runner_s3_bucket_name = simpledialog.askstring(title="Enter the parameters you need",
    prompt="Gitlab Runner S3 Bucket Name (example: test-runner): ")
gitlab_runner_s3_bucket_location = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner S3 Region (example/default: eu-central-1): ") or "eu-central-1"
gitlab_runner_docker_volume = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Docker Volume (example/default: /var/run/docker.sock:/var/run/docker.sock): ") or '/var/run/docker.sock:/var/run/docker.sock'
gitlab_runner_docker_cache = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Docker Volume2 (example/default: /cache): ") or '/cache'
gitlab_runner_docker_cache = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Docker Cache (example/default: true): ") or "true"
gitlab_runner_docker_privileged = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Docker Priveleged (example/defaeult: true): ") or "true"
gitlab_runner_idle_nodes = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Idle Nodes (example/default: 1): ") or "1"
gitlab_runner_idle_time = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Idle Time (example/default: 1800): ") or "1800"
gitlab_runner_max_builds = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Max Builds (example/default: 100): ") or "100"
gitlab_runner_driver = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Driver (example/default: amazonec2): ") or "amazonec2"
gitlab_runner_machine_name = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Machine Name (example/default: gitlab-docker-machine-%s): ") or "gitlab-docker-machine-%s"
gitlab_runner_amazonec2_access_key = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Amazaon Access Key (example: 825WLSv2vJcsaCMwHO2z): ")
while bool(gitlab_runner_amazonec2_access_key) == False:
     gitlab_runner_amazonec2_access_key = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Gitlab Runner Amazaon Access Key (example: 825WLSv2vJcsaCMwHO2z): ")
gitlab_runner_amazonec2_secret_key = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitalb Runner Amazon Secret Key (example: lFCIzKGoD0zHJsEcmVnge04miFLKzhTnHQ9l): ")
while bool(gitlab_runner_amazonec2_secret_key) == False:
     gitlab_runner_amazonec2_secret_key = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Gitalb Runner Amazon Secret Key (example: lFCIzKGoD0zHJsEcmVnge04miFLKzhTnHQ9l): ")
gitlab_runner_amazonec2_region = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gtilab Runner Amazon Region (example/default: eu-central-1): ") or "eu-central-1"
gitlab_runner_amazonec2_vpc = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Amazon VPC ID (example: vpc-123123123123): ")
while bool(gitlab_runner_amazonec2_vpc) == False:
     gitlab_runner_amazonec2_vpc = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Gitlab Runner Amazon VPC ID (example: vpc-123123123123): ")  
gitlab_runner_amazonec2_subnet = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Amazon Subnet ID (example: subnet-123123123123): ")
while bool(gitlab_runner_amazonec2_subnet) == False:
     gitlab_runner_amazonec2_subnet = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Gitlab Runner Amazon Subnet ID (example: subnet-123123123123): ")
gitlab_runner_amazonec2_zone = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Amazon Region Zone (example/default: a): ") or "a"
gitlab_runner_amazonec2_tags = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Amazon Machine Tag (example/default: runner-manager-name,gitlab-aws-autoscaler,gitlab,true,gitlab-runner-autoscale,true): ") or "runner-manager-name,gitlab-aws-autoscaler,gitlab,true,gitlab-runner-autoscale,true"
gitlab_runner_amazonec2_security_group = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Amazon Security Group (example: Runner-SG): ")
while bool(gitlab_runner_amazonec2_security_group) == False:
     gitlab_runner_amazonec2_security_group = simpledialog.askstring(title="Enter the parameters you need",
     prompt="Gitlab Runner Amazon Security Group (example: Runner-SG): ")
gitlab_runner_amazonec2_instance_type = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Amazon Spot Instance Type (example/default: t3.medium): ") or "t3.medium"
gitlab_runner_amazonec2_spot_instance = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Use Spot Instance (example/default: true): ") or "true"
gitlab_runner_amazonec2_spot_price = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Spot Price Limit (example/default: 0.04): ") or "0.04"
gitlab_runner_off_peak_periods = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Off Peak Periods (example/default: '* * 0-8,22-23 * * mon-fri *, * * * * * sat,sun *'): ") or '* * 0-8,22-23 * * mon-fri *, * * * * * sat,sun *'
gitlab_runner_off_peak_timezone = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Time Zone (example/default: Europe/Kiev): ") or "Europe/Kiev"
gitlab_runner_off_peak_idlecount = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Off Peak Idle Count (example/default: 0): ") or "0"
gitlab_runner_off_peak_idletime = simpledialog.askstring(title="Enter the parameters you need",
prompt="Gitlab Runner Off Peak Idle Time (example/default: 1200): ") or "1200"


# Edit Varibles File
# 3
# -*- coding: utf-8 -*-
# Opening the file read-only
setup_server_defaults = str(directory) + str('/setup/roles/setup-server/defaults/main.yml')
file = open(setup_server_defaults, 'r')
lines = file.readlines()
lines[7] = 'gitlab_runner_name: ' + gitlab_runner_name + '\n'
lines[9] = 'gitlab_runner_coordinator_url: ' + gitlab_runner_coordinator_url + '\n'
lines[10] = 'gitlab_runner_registration_token: ' + gitlab_runner_registration_token + '\n'
lines[11] = 'gitlab_runner_executor: ' + gitlab_runner_executor + '\n'
lines[12] = 'gitlab_runner_docker_image: ' + gitlab_runner_docker_image + '\n'
lines[13] = 'gitlab_runner_limit: ' + gitlab_runner_limit + '\n'
lines[14] = 'gitlab_runner_s3_server_address: ' + gitlab_runner_s3_server_address + '\n'
lines[15] = 'gitlab_runner_s3_access_key: ' + gitlab_runner_s3_access_key + '\n'
lines[16] = 'gitlab_runner_s3_secret_key: ' + gitlab_runner_s3_secret_key + '\n'
lines[17] = 'gitlab_runner_s3_bucket_name: ' + gitlab_runner_s3_bucket_name + '\n'
lines[18] = 'gitlab_runner_s3_bucket_location: ' + '"' + gitlab_runner_s3_bucket_location + '"' + '\n'
lines[19] = 'gitlab_runner_docker_volume: ' + gitlab_runner_docker_volume + '\n'
lines[20] = 'gitlab_runner_docker_volume2: ' + gitlab_runner_docker_volume + '\n'
lines[21] = 'gitlab_runner_docker_cache: ' + gitlab_runner_docker_cache + '\n'
lines[22] = 'gitlab_runner_docker_privileged: ' + gitlab_runner_docker_privileged + '\n'
lines[23] = 'gitlab_runner_idle_nodes: ' + gitlab_runner_idle_nodes + '\n'
lines[24] = 'gitlab_runner_idle_time: ' + gitlab_runner_idle_time + '\n'
lines[25] = 'gitlab_runner_max_builds: ' + gitlab_runner_max_builds + '\n'
lines[26] = 'gitlab_runner_driver: ' + '"' + gitlab_runner_driver + '"' + '\n'
lines[27] = 'gitlab_runner_machine_name: ' + '"' + gitlab_runner_machine_name + '"' + '\n'
lines[28] = 'gitlab_runner_amazonec2_access_key: amazonec2-access-key=' + gitlab_runner_amazonec2_access_key + '\n'
lines[29] = 'gitlab_runner_amazonec2_secret_key: amazonec2-secret-key=' + gitlab_runner_amazonec2_secret_key + '\n'
lines[30] = 'gitlab_runner_amazonec2_region: amazonec2-region=' + gitlab_runner_amazonec2_region + '\n'
lines[31] = 'gitlab_runner_amazonec2_vpc: amazonec2-vpc-id=' + gitlab_runner_amazonec2_vpc + '\n'
lines[32] = 'gitlab_runner_amazonec2_subnet: amazonec2-subnet-id=' + gitlab_runner_amazonec2_subnet + '\n'
lines[33] = 'gitlab_runner_amazonec2_zone: amazonec2-zone=' + gitlab_runner_amazonec2_zone + '\n'
lines[34] = 'gitlab_runner_amazonec2_tags: amazonec2-tags=' + gitlab_runner_amazonec2_tags + '\n'
lines[35] = 'gitlab_runner_amazonec2_security_group: amazonec2-security-group=' + gitlab_runner_amazonec2_security_group + '\n'
lines[36] = 'gitlab_runner_amazonec2_instance_type: amazonec2-instance-type=' + gitlab_runner_amazonec2_instance_type + '\n'
lines[37] = 'gitlab_runner_amazonec2_spot_instance: amazonec2-request-spot-instance=' + gitlab_runner_amazonec2_spot_instance + '\n'
lines[38] = 'gitlab_runner_amazonec2_spot_price: amazonec2-spot-price=' + gitlab_runner_amazonec2_spot_price + '\n'
lines[39] = 'gitlab_runner_off_peak_periods: ' + '"' + gitlab_runner_off_peak_periods + '"' + '\n'
lines[40] = 'gitlab_runner_off_peak_timezone: ' + '"' + gitlab_runner_off_peak_timezone + '"' + '\n'
lines[41] = 'gitlab_runner_off_peak_idlecount: ' + '"' + gitlab_runner_off_peak_idlecount + '"' + '\n'
lines[42] = 'gitlab_runner_off_peak_idletime: ' + '"' + gitlab_runner_off_peak_idletime + '"' + '\n'
lines[43] = 'aws_access_key: ' + gitlab_runner_amazonec2_access_key + '\n'
lines[44] = 'aws_secret_key: ' + gitlab_runner_amazonec2_secret_key + '\n'
lines[45] = 'aws_region: ' + gitlab_runner_amazonec2_region + '\n'


# Close the file
file.close()

# Opening the file for writing
save_changes = open(setup_server_defaults, 'w')
 
# Save the list of strings
save_changes.writelines(lines)
 
# Close the file
save_changes.close()

# Edit Varibles File
# 3
# -*- coding: utf-8 -*-
# Opening the file read-only
gitlab_runner_defaults = str(directory) + str('/setup/roles/gitlab-runner-register/defaults/main.yml')
file = open(gitlab_runner_defaults, 'r')
lines = file.readlines()
lines[7] = 'gitlab_runner_name: ' + gitlab_runner_name + '\n'
lines[9] = 'gitlab_runner_coordinator_url: ' + gitlab_runner_coordinator_url + '\n'
lines[10] = 'gitlab_runner_registration_token: ' + gitlab_runner_registration_token + '\n'
lines[11] = 'gitlab_runner_executor: ' + gitlab_runner_executor + '\n'
lines[12] = 'gitlab_runner_docker_image: ' + gitlab_runner_docker_image + '\n'
lines[13] = 'gitlab_runner_limit: ' + gitlab_runner_limit + '\n'
lines[14] = 'gitlab_runner_s3_server_address: ' + gitlab_runner_s3_server_address + '\n'
lines[15] = 'gitlab_runner_s3_access_key: ' + gitlab_runner_s3_access_key + '\n'
lines[16] = 'gitlab_runner_s3_secret_key: ' + gitlab_runner_s3_secret_key + '\n'
lines[17] = 'gitlab_runner_s3_bucket_name: ' + gitlab_runner_s3_bucket_name + '\n'
lines[18] = 'gitlab_runner_s3_bucket_location: ' + '"' + gitlab_runner_s3_bucket_location + '"' + '\n'
lines[19] = 'gitlab_runner_docker_volume: ' + gitlab_runner_docker_volume + '\n'
lines[20] = 'gitlab_runner_docker_volume2: ' + gitlab_runner_docker_volume + '\n'
lines[21] = 'gitlab_runner_docker_cache: ' + gitlab_runner_docker_cache + '\n'
lines[22] = 'gitlab_runner_docker_privileged: ' + gitlab_runner_docker_privileged + '\n'
lines[23] = 'gitlab_runner_idle_nodes: ' + gitlab_runner_idle_nodes + '\n'
lines[24] = 'gitlab_runner_idle_time: ' + gitlab_runner_idle_time + '\n'
lines[25] = 'gitlab_runner_max_builds: ' + gitlab_runner_max_builds + '\n'
lines[26] = 'gitlab_runner_driver: ' + '"' + gitlab_runner_driver + '"' + '\n'
lines[27] = 'gitlab_runner_machine_name: ' + '"' + gitlab_runner_machine_name + '"' + '\n'
lines[28] = 'gitlab_runner_amazonec2_access_key: amazonec2-access-key=' + gitlab_runner_amazonec2_access_key + '\n'
lines[29] = 'gitlab_runner_amazonec2_secret_key: amazonec2-secret-key=' + gitlab_runner_amazonec2_secret_key + '\n'
lines[30] = 'gitlab_runner_amazonec2_region: amazonec2-region=' + gitlab_runner_amazonec2_region + '\n'
lines[31] = 'gitlab_runner_amazonec2_vpc: amazonec2-vpc-id=' + gitlab_runner_amazonec2_vpc + '\n'
lines[32] = 'gitlab_runner_amazonec2_subnet: amazonec2-subnet-id=' + gitlab_runner_amazonec2_subnet + '\n'
lines[33] = 'gitlab_runner_amazonec2_zone: amazonec2-zone=' + gitlab_runner_amazonec2_zone + '\n'
lines[34] = 'gitlab_runner_amazonec2_tags: amazonec2-tags=' + gitlab_runner_amazonec2_tags + '\n'
lines[35] = 'gitlab_runner_amazonec2_security_group: amazonec2-security-group=' + gitlab_runner_amazonec2_security_group + '\n'
lines[36] = 'gitlab_runner_amazonec2_instance_type: amazonec2-instance-type=' + gitlab_runner_amazonec2_instance_type + '\n'
lines[37] = 'gitlab_runner_amazonec2_spot_instance: amazonec2-request-spot-instance=' + gitlab_runner_amazonec2_spot_instance + '\n'
lines[38] = 'gitlab_runner_amazonec2_spot_price: amazonec2-spot-price=' + gitlab_runner_amazonec2_spot_price + '\n'
lines[39] = 'gitlab_runner_off_peak_periods: ' + '"' + gitlab_runner_off_peak_periods + '"' + '\n'
lines[40] = 'gitlab_runner_off_peak_timezone: ' + '"' + gitlab_runner_off_peak_timezone + '"' + '\n'
lines[41] = 'gitlab_runner_off_peak_idlecount: ' + '"' + gitlab_runner_off_peak_idlecount + '"' + '\n'
lines[42] = 'gitlab_runner_off_peak_idletime: ' + '"' + gitlab_runner_off_peak_idletime + '"' + '\n'
lines[43] = 'aws_access_key: ' + gitlab_runner_amazonec2_access_key + '\n'
lines[44] = 'aws_secret_key: ' + gitlab_runner_amazonec2_secret_key + '\n'
lines[45] = 'aws_region: ' + gitlab_runner_amazonec2_region + '\n'


# Close the file
file.close()

# Opening the file for writing
save_changes = open(gitlab_runner_defaults, 'w')
 
# Save the list of strings
save_changes.writelines(lines)
 
# Close the file
save_changes.close()
