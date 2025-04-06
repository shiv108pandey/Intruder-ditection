# Intruder Detection and Alert System using YOLOv3, OpenCV, and Email Notifications

This project is a real-time intruder detection and alert system built using YOLOv3 object detection, OpenCV for video streaming, and Python for automation. It detects human presence through a webcam, raises an alarm, captures an image, and sends it to the user via email as an alert.

 Features
 Real-time human detection using pre-trained YOLOv3 model

 Automatic snapshot capture of the intruder

 Email notification with image attachment sent to the user

 Buzzer/alarm sound triggered when intruder is detected

 Live security camera feed using OpenCV

 Project Structure
bash
Copy
Edit
Intruder-Detection/
│
├── yolov3.cfg               # YOLOv3 configuration file
├── yolov3.weights           # YOLOv3 pre-trained weights
├── intruder.jpg             # Captured image of intruder (created at runtime)
├── main.py                  # Main script for detection and alert
├── README.md                # Project documentation
└── .env (optional)          # Store sensitive info like email credentials
 Requirements
Install the following dependencies before running the project:

bash
Copy
Edit
pip install opencv-python numpy
You also need:

yolov3.weights: Download from here

yolov3.cfg: Download from here

Python 3.7+

Windows OS (for winsound module)

 Installation & Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/Intruder-Detection.git
cd Intruder-Detection
Download YOLOv3 model files and place them in the same directory:

yolov3.cfg

yolov3.weights

Update your email credentials in the script (main.py), or use .env for better security.

Run the script

bash
Copy
Edit
python main.py
 How It Works
Webcam feed is captured using OpenCV.

Each frame is passed to YOLOv3 for object detection.

If a human (person class ID = 0) is detected:

A rectangle is drawn.

Frame is saved as intruder.jpg.

Alarm is played using winsound.Beep().

An email is sent to the user with the image attachment.

The loop continues until the user presses 'q'.

 Security Note
Avoid hardcoding your email and password in the script. Use environment variables or a .env file like:

env
Copy
Edit
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
EMAIL_SEND=recipient_email@gmail.com
 Future Improvements
Add motion detection using OpenCV background subtraction.

Add support for multiple cameras or IP camera feeds.

Deploy the system on Raspberry Pi for portability.

Store captured images and timestamps in a local database.

Send alerts via WhatsApp/Telegram in addition to email.

 Developed By
Shiv Swaroop Pandey
Email: shivswarooppandey68@gmail.com
GitHub: github.com/shivswarooppandey (https://github.com/shiv108pandey)

