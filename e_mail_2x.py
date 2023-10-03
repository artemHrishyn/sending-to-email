# coding: utf8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

toaddr = ['<user@mail.ru>', '<user2@mail.ru>', '<user3@mail.ru>']
me = 'From: My Name <user@gmail.com>'
you = 'To: ' + ', '.join(toaddr)

server = 'smtp.gmail.com' # Сервер отпраитель
port = 25 # возможные порты: 587, 465
user_name = 'user@gmail.com' # Адрес отправителя
user_passwd = 'password' # Пароль отправителя

# Формируем заголовок письма
msg = MIMEMultipart('mixed')
msg['Subject'] = 'Заголовок письма'
msg['From'] = me
msg['To'] = ', '.join(toaddr[0:2]) # отправка 2-м адресаиам
msg['cc'] = ', '.join([ toaddr[2] ]) # отправка копии 1-му адресату

# Формируем письмо
part1 = MIMEText('Содержимое письма', 'plain')
part2 = MIMEText('Содержимое приложенного файла', 'text/html;name="tasks.htm"', 'utf-8')
msg.attach(part1)
msg.attach(part2)

# Подключение
s = smtplib.SMTP(server, port)
s.ehlo()
s.starttls()
s.ehlo()
# Авторизация
s.login(user_name, user_passwd)
# Отправка пиьма
s.sendmail(me, toaddr, msg.as_string())
s.quit()