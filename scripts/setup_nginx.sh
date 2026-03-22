#!/bin/bash

# check if script is run with sudo / root is running it
if [ "$(id -u)" != "0" ]; then
	echo "This script must be run as root or with sudo!"
    read ""
	exit 1
else
	if ! command -v nginx &> /dev/null; then # if nginx isnt installed
		
		echo "Updating package list..."
		if ! apt-get update -y > /dev/null; then
			echo "*** Error with updating apt. ***"
			exit 2
            read ""
		fi
		
        echo ""
		echo "Starting installation of nginx..." 	
        if ! apt-get install -y nginx > /dev/null; then
			echo "*** Error with the installation of nginx. *** "
			exit 3 
            read ""
		fi
		
		echo ""
		echo "completed installation of nginx!"
		echo ""

	else
		echo "nginx already installed!" 	
	fi
	echo "Setting up nginx service and enableing it..."
	systemctl start nginx
	systemctl enable nginx
	
	echo "nginx service is up and running!"
    read ""
fi