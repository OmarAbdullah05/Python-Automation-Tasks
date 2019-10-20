#! python3
import smtplib
#start program
server = smtplib.SMTP('smtp.gmail.com', $key)
server.ehlo()
server.starttls()
server.ehlo()

server.login('$email', '$key')

msg = "Something"

server.sendmail(
    '$From_Email',
    '$To_Email',
    msg
)
print('HEY EMAIL HAS BEEN SENT')

server.quit()
