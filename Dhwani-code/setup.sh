#!/bin/sh

DEPS="libatlas-base-dev"

echo "Do you have a wit.ai API token? [Y/n]"
read ans;
if [ $ans = "n" ]; then
	echo "Make it then"
	xdg-open https://www.wit.ai/
	exit 1
else
	echo "What is it?"
	read API_TOKEN;
fi


if [[ -z "${WIT}" ]]; then
	export WIT=$API_TOKEN
	echo "Added by Dhwani" >> ~/.$(echo $0)rc
	echo "WIT=$API_TOKEN" >> ~/.$(echo $0)rc
else
	echo "Skipping env var setup"
fi


echo Installing Wit...
pip3 install wit
if (( $? )); then
	echo "Please fix pip. Exiting"
	exit 1
else
	echo "Wit installed"
fi

if [ -f /etc/os-release ]; then
	. /etc/os-release
	OS=$NAME;
	VER=$VERSION_ID
fi

sudo apt install $DEPS

echo $OS $VER
