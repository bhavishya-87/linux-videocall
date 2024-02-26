# Video Call Application
![Running GIF](https://camo.githubusercontent.com/1140a4f2ffe1d7d5432df78421909e56c97909423568e609983ec3d4fbcb0b22/68747470733a2f2f726561646d652d747970696e672d7376672e6865726f6b756170702e636f6d3f666f6e743d4f72626974726f6e2673697a653d343026636f6c6f723d253233373941353030266865696768743d3637266475726174696f6e3d333030302663656e7465723d74727565266c696e65733d254630253946253835254236254630253946253836253831254630253946253835254234254630253946253835254234254630253946253836253833254630253946253835254238254630253946253835254244254630253946253835254236254630253946253836253832)


This script implements a simple video call application using OpenCV and Tkinter. It provides the ability to either send live video from your webcam to a specified directory on a web server or receive and display video from a specified IP address.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Functionality](#functionality)
    - [Send Video](#send-video)
    - [Receive Video](#receive-video)
- [Requirements](#requirements)
    - [Running Environment](#running-environment)
    - [Firewall and SELinux](#firewall-and-selinux)

## Prerequisites

- Python 3.x
- OpenCV (`cv2` library)
- Tkinter (usually included with Python)
- `wget` command-line tool

## Usage

1. Install the required packages using `pip install opencv-python-headless`.
2. Install the required packages using `pip install yum install python3-tkinter`.
3. Copy the provided code into your Python script or file.
4. Run the script using `python finalcode.py`.

## Functionality

### Send Video

The script captures video from the webcam and continuously saves frames as images in the specified directory on the web server. Press the Enter key to stop sending video.

### Receive Video

The script downloads images from the specified IP address and displays them as a video stream. Press the Enter key to stop receiving video.

To receive video, you need to enter the IP address of the machine where the video is being sent from.

## Requirements

### Running Environment

- This script has been designed to run on Red Hat Enterprise Linux (RHEL) systems.
- It is recommended to use a RHEL virtual machine (e.g., RHEL 9) for testing purposes.

### Firewall and SELinux

- To ensure the application runs smoothly, it's recommended to disable both the firewall and SELinux on your RHEL system. You can do this by running the following commands:
    ```
    systemctl stop firewalld
    setenforce 0
    ```

## Advantages

- Simplifies the process of sending and receiving live video streams.
- Provides a user-friendly interface using Tkinter.
- Easy-to-understand code structure allows customization and extension.

---

Feel free to explore and modify the code to suit your needs. This video call application can be a starting point for building more complex video communication systems or for learning how video streaming works in Python.
![Running GIF](  https://raw.githubusercontent.com/trinib/trinib/82213791fa9ff58d3ca768ddd6de2489ec23ffca/images/footer.svg)
