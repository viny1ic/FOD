# FOD detection system for runways
## required software/ hardware
- python3.x
- arduino uno or similar
- arduino IDE
- 2 servos (SG90 in my case, more accurate servos like MG995 recommended)
- mount to mount camera (3D printed mount using servos to rotate the camera in X and Y axes used in my case)
# SETUP AND RUN
## install required libraries using:
```
pip install opencv-python numpy pyserial playsound
```
## Setup hardware for prototyping
1. connect servos to the arduino (x servo to digital pin 6, y servo to digital pin 9)
2. upload the code of phone.ino to the arduino using the arduino IDE
3. configure camera input
3.1 set the IP and port of camera feed into try1.py (if we are using an IP camera)
3.2 set the corresponding camera input if using wired USB camera
4. make sure the camera is set on a stable, non vibrational surface and is free from disturbances.
5. run the program
```
python try1.py
```
6. throw a small FOD in the camera's field of vision
