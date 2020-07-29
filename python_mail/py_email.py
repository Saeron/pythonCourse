import smtplib
import ssl
from email.utils import make_msgid
from email.message import EmailMessage
import base64
import imghdr

sender_email = "antdcs@gmail.com"
receiver_email = "antdcs@gmail.com"
password = input("Type your password and press enter:")

message = EmailMessage()
message["Subject"] = "multipart test"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
message.set_content("""\
You need a new email app to suport multipart emails.
""")

asparagus_cid = make_msgid()
asparagus_cid2 = make_msgid()

message.add_alternative("""\
<html>
  <body style=\"text-align: center\">
    <p>Hi, Saeron<br>
      <h1>Your ticket</h1><br>
       <img src="cid:{asparagus_cid}" />
    </p>
  </body>
</html>
""".format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

img = b'iVBORw0KGgoAAAANSUhEUgAAASIAAAEiAQAAAAB1xeIbAAABoElEQVR4nO3YQW6cMBjF8f8rSF16JA6Qo5gb9EhRj9QbwFFygEh4GcnodWHItFGlZjNAwF4wDPpJPHmYj8+W+f8Yv30CQVVVVVVVVUdXWkaL+iSVgySp3zXXuVVbPuIAkDpMApOaDID2ynUllZZnXHoqs46kdv9cF1ON1W97x6rKiNMsD1ve8bJqLSvBQAKPAsVf8Oei66jpv7Za5n4sL9UGxanLgln75rqCKnN/f8YNb1r+BnvmuoLCtr2cTc065cEGGhNtezhq+jMoDyGX9nJ5zSbVmrOR0vNLC/GlBUIuP4XtN/2lts91bvXe5+QWQkYEIE4zIryuL4Kjpj+N8k+1EKfG6tN3L2f75zqteu9zGhMNjLfX1uNTBlKXd8t1BVXmfq3rTfb4A1SuhFxrziPV0mNG2/bULIchrB1P7TEfr9Z9TMYb6Ll0+o2XlvPo6b+maj98F9yXubNqzdlSxQmk2yzifZl7gFwnVsFrfQkZD6lFfcio3znXmdXHfUxIXVacbpjU5VpzHqj+sY+ZcbkS1vb+sOmrqqqqqqr6rPoNh3Wh25ponPEAAAAASUVORK5CYII='

message.get_payload()[1].add_related(base64.decodebytes(img), 'image', 'png', cid=asparagus_cid)
message.add_attachment(base64.decodebytes(img), maintype='image',
                                 subtype=imghdr.what(None , base64.decodebytes(img)), filename="qrcode.png")


# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
