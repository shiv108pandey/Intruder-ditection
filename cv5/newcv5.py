import cv2
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import winsound
import os

# Setup email parameters
email_user = 'shivswarooppandey68@gmail.com'
email_password = 'abhhbjhbhgggjhhhgg'  # This should be an app-specific password, not your regular password
email_send = 'shivswarooppandey940@gmail.com'

subject = 'Intruder Alert'


def send_email_with_attachment(image_path):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'An intruder has been detected by your security system. See the attached image.'
    msg.attach(MIMEText(body, 'plain'))

    # Attach the image file
    attachment = open(image_path, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(image_path)}")

    msg.attach(part)

    # Use Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    text = msg.as_string()
    server.sendmail(email_user, email_send, text)
    server.quit()

    attachment.close()


def play_alarm():
    
    frequency = 500  # Set frequency
    duration = 10000  # Set duration to 1000 ms (1 second)
    winsound.Beep(frequency, duration)


def detect_human():
    # Load the pre-trained model for human detection
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    # Access the camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        height, width, channels = frame.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Showing information on the screen
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = int(detection[0])  
                confidence = scores[class_id]

                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    # Draw bounding box around the person
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    text = "Human detected"

                    # Save the captured image
                    img_name = "intruder.jpg"
                    cv2.imwrite(img_name, frame)

                    # Trigger alarm and send email with the image
                    play_alarm()
                    send_email_with_attachment(img_name)
                    time.sleep(10)  # Delay to avoid sending multiple emails

        # Display the resulting frame
        cv2.imshow("Security Feed", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_human()
