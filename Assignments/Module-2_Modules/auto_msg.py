import pyautogui
import time
import webbrowser

# Replace with your friend's phone number (in international format)
phone_number = "+919724799469"  # Replace with real number

# Your message
message = "Hello! This is an automated message using PyAutoGUI 😎"

# Open WhatsApp Web chat in browser
webbrowser.open(f"https://web.whatsapp.com/send?phone={phone_number}&text={message}")
time.sleep(15)  # Wait for WhatsApp Web to load and QR scan (adjust if needed)

# Hit ENTER to send message
pyautogui.press("enter")


for i in range(10):  # Send 100 times
    pyautogui.write(message)
    pyautogui.press("enter")
    time.sleep(0.5)
