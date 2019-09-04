#!/usr/bin/env python3.6
#created 2019/9/4 for WiFi connection tolerance. This is useful when you have 2 WiFi networks such as WiFi A and WiFi B. You loose all connection when you failed to join WiFi. This was a big problem when you don't have physical access to RaspberryPi. This python script set back to previous setting if connecting another WiFi fails. So you don't have to go setup raspberry pi physically just for WiFi.
import time
import os


#set Hyper-WARPSTAR

# interfaces for static ip address settings for wlan0.
os.system("sudo cp /home/pi/backup/Hyper-WARPSTAR/interfaces /etc/network/interfaces")
# wpa_supplicant.conf for WiFi network SSID and keyphrase.
os.system("sudo cp /home/pi/backup/Hyper-WARPSTAR/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf")
# restart network in oder to take chages effect without reboot.
os.system("sudo ip addr flush wlan0")
os.system("sudo systemctl restart networking")
os.system("sudo ifdown wlan0 && sudo ifup wlan0")
#ping host to make sure you are in another WiFi network.
hostname = "192.168.1.1"
response = os.system("ping -c 5 " + hostname)
if response == 0:
    time.sleep(0.2)
    print(hostname, 'Successed. You are in Hyper-WARPSTAR')
else:
# back to previos settings
    time.sleep(0.2)
    print('back to previous settings now')
    os.system("sudo cp /home/pi/backup/WARPSTAR/interfaces /etc/network/interfaces")
    os.system("sudo cp /home/pi/backup/WARPSTAR/wpa_supplicant.conf /etc/wpa_supplicant/wpa_supplicant.conf")
    os.system("sudo ip addr flush wlan0")
    os.system("sudo systemctl restart networking")
    os.system("sudo ifdown wlan0 && sudo ifup wlan0")
    print('You are now connceted to WARPSTAR')
