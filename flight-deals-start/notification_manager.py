import smtplib

from twilio.rest import Client
MYEMAIL = 'loooksoook@gmail.com'
MYPASSWORD = '143Muller'


class NotificationManager:

    def send_sms(self, message):
        account_sid = "ACbb1904b33ebaec888a6c6426deb8f29c"
        auth_token = "29072fa0f1580edbf3b90eee376d9acb"

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_="+16464614749",
            to="+9779866126473"
        )

        print(message.sid)

    def send_mail(self, emails, message, google_flight_link):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(MYEMAIL, MYPASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MYEMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

