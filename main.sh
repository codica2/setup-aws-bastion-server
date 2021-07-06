#!/bin/bash

# installation of basic programs 
# Name
if (whiptail --title "____ 'Welcome to Setup Bastion Server' ____" --yesno "This is the basic setup for Ubuntu, would you like to continue?" 10 60) then
echo -e "\e[32mWe continue to configure!\e[0m" 
else
echo -e "\e[32mBye!\e[0m" && exit; fi

# Password
PASS=$(whiptail --passwordbox "Please enter your secret password" 8 78 --title "password dialog" 3>&1 1>&2 2>&3)
exitstatus=$?

# Check Exit Status
if [ $exitstatus = 0 ]; then 
echo -e "\e[32mStart\e[0m" 
else
echo -e "\e[32mBye!\e[0m" && exit; fi

# Search directory
directory="$(echo $PASS | sudo -S find /home/ -name 'setup-aws-bastion-server')"
{
    for ((i = 0 ; i <= 100 ; i+=20)); do
        sleep 1
        echo $i
	directory="$(echo $PASS | sudo -S find /home/ -name 'setup-aws-bastion-server')"
    done
} | whiptail --gauge "Please wait, looking for a folder!" 6 60 0

# Menu
OPTION=$(whiptail --title "Welcome to Setup Bastion Server" --menu "Select the desired action:" 20 78 8 \
"1" "Full Setup Bastion Server and Register Gitlab Runner" \
"2" "Only Install Gitalb Runner" \
"3" "Only Install Docker and Docker Compose" \
"4" "Only Install Docker Machine" \
"5" "Only Register Gitlab Runner" \
"6" "Only Install AWS CLI and AWS Login" \
"7" "Only Add Cron AWS Login" \
"8" "Only Setup Bastion Server" 3>&1 1>&2 2>&3)
exitstatus=$?

# Check Exit Status
if [ $exitstatus = 0 ]; then 
echo -e "\e[32mYou choosed:\e[0m" $OPTION
else
echo -e "\e[32mBye!\e[0m" && exit; fi

# selection of menu items
case "$OPTION" in
1) python3 $directory/setup/python/dir.py && echo -e '\e[4mJust Enter to use default parameters\e[0m' && python3 $directory/setup/python/info.py && python3 $directory/setup/python/defaults.py && ansible-playbook -i $directory/setup/hosts/hosts $directory/setup/setup_server.yml;;
2) python3 $directory/setup/python/dir.py && python3 $directory/setup/python/info.py && ansible-playbook  -i $directory/setup/hosts/hosts $directory/setup/install_gitlab_runner.yml;;
3) python3 $directory/setup/python/dir.py && python3 $directory/setup/python/info.py && ansible-playbook -i $directory/setup/hosts/hosts $directory/setup/install_docker.yml;;
4) python3 $directory/setup/python/dir.py && python3 $directory/setup/python/info.py && ansible-playbook -i $directory/setup/hosts/hosts $directory/setup/install_docker_machine.yml;;
5) python3 $directory/setup/python/dir.py && echo -e '\e[4mJust Enter to use default parameters\e[0m' && python3 $directory/setup/python/info.py && python3 $directory/setup/python/defaults.py && ansible-playbook -i $directory/setup/hosts/hosts $directory/setup/register_gitlab_runner.yml;;
6) python3 $directory/setup/python/dir.py && echo -e '\e[4mJust Enter to use default parameters\e[0m' && python3 $directory/setup/python/info.py && python3 $directory/setup/python/aws.py && ansible-playbook -i $directory/setup/hosts/hosts $directory/setup/aws-cli.yml;;
7) python3 $directory/setup/python/dir.py && echo -e '\e[4mJust Enter to use default parameters\e[0m' && python3 $directory/setup/python/info.py && python3 $directory/setup/python/aws.py && ansible-playbook -i $directory/setup/hosts/hosts $directory/setup/aws-cron.yml;;
8) python3 $directory/setup/python/dir.py && echo -e '\e[4mJust Enter to use default parameters\e[0m' && python3 $directory/setup/python/info.py && python3 $directory/setup/python/aws.py && ansible-playbook -i $directory/setup/hosts/hosts $directory/setup/only-setup-server.yml;;
esac 
   
echo -e "\e[1;32m!!!Ready!!!\e[0m" || echo -e "\e[31mError...\e[0m"
