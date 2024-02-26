import cv2
import os
import tkinter as tk
from tkinter import messagebox

def send_video():
    cap = cv2.VideoCapture(0)
    while True:
        status, photo = cap.read()
        cv2.imwrite("/var/www/html/bhanu.png", photo)
        cv2.imshow("photo1.png", photo)
        keypressed = cv2.waitKey(100)
        if keypressed == 13:
            break
    cv2.destroyAllWindows()
    cv2.release()

def receive_video():
    ip_address = ip_entry.get()
    while True:
        os.system(f"wget -r -np -nH --cut-dirs=1 http://{ip_address}/bhanu.png")
        image = cv2.imread("/root/Desktop/vc_ss/bhanu.png")
        if image is not None:
          cv2.imshow("Image", image)
          keypressed = cv2.waitKey(100)
          if keypressed == 13:
              break
    cv2.destroyAllWindows()

def handle_selection():
    choice = var.get()
    if choice == 1:
        send_video()
    elif choice == 2:
        if len(ip_entry.get()) == 0:
            messagebox.showerror("Error", "Please enter the IP address.")
            return
        receive_video()

# Create the GUI
window = tk.Tk()
window.title("Video Call Application")
window.geometry("400x200")

# Create a label for the instructions
instructions_label = tk.Label(window, text="Select an option:")
instructions_label.pack()

# Create a radio button for sending video
var = tk.IntVar()
send_radio = tk.Radiobutton(window, text="Send Video", variable=var, value=1)
send_radio.pack()

# Create a radio button for receiving video
receive_radio = tk.Radiobutton(window, text="Receive Video", variable=var, value=2)
receive_radio.pack()

# Create an entry field for IP address
ip_label = tk.Label(window, text="Enter IP Address:")
ip_entry = tk.Entry(window)

def show_ip_entry():
    if var.get() == 2:
        ip_label.pack()
        ip_entry.pack()
    else:
        ip_label.pack_forget()
        ip_entry.pack_forget()

var.trace("w", lambda *args: show_ip_entry())

# Create a button to start the selected action
start_button = tk.Button(window, text="Start", command=handle_selection)
start_button.pack()

# Start the GUI event loop
window.mainloop()
