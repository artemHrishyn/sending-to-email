import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# отправка почты
def send_mail():
    login = "testartem1989@mail.ru"
    password = "artemida1artemida"
    url = "smtp.mail.ru"
    toaddr = "grishinartyomvladimirovich@gmail.com"
    topic = "Proba2"
    message = "Проба прошла"

    msg = MIMEMultipart()

    msg['Subject'] = topic
    msg['From:'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())


def main():
    send_mail()


if __name__ == '__main__':
    main()
