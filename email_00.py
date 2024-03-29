# https://www.youtube.com/watch?v=JRCJ6RtE3xU

import smtplib
import imghdr
from email.message import EmailMessage


email_address = "kekesi.att@gmail.com"
email_password = ""
email_to = ["kekesi.att@gmail.com", "kekkencs@gmail.com", "kekesati@schaeffler.com"]
files_image = ["email_image1.jpg", "email_image2.jpg"]
files_pdf = ["email_protocol.pdf"]

msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = email_address
msg["To"] = ", ".join(email_to)
msg.set_content("Hi,\n\nThis is a test mail sent by python")

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype="html")

for file in files_image:
    with open(file, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

for file in files_pdf:
    with open(file, "rb") as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
