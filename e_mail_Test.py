import smtplib as root
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import random
import smtplib

# Начальный шаблон в Excel
import xlwt

e_mail = ["grishinartyomvladimirovich@gmail.com", "ilend1969@gmail.com", "krolikipravdino@gmail.com"]
# ввод своих фин остатков
cash = int(input("Введите пожалуйста сколько у вас налички \n"))
bez_nal = int(input("Введите пожалуйста сколько у вас карточки\n"))

# Стиль 1: Имя шрифта - Times New Roman, Цвет красный, Жирный, формат числа “1 000,00”
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
# Стиль 2: Формат Даты 01.05.1989
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
wb = xlwt.Workbook()
# Имя листа “A Test Sheet”
ws = wb.add_sheet('Лист 1')


# ws.write(0, 0, "Месяц", style0)
i = 0
namber = 1

ws.write(0, 0, "Месяца", style0)
ws.write(0, 1, "Налички", style0)
ws.write(0, 2, "На карте", style0)

ws.write(1, 0, "Январь")
ws.write(2, 0, "Февраль")
ws.write(3, 0, "Март")

ws.write(4, 0, "Апрель")
ws.write(5, 0, "Май")
ws.write(6, 0, "Июнь")

ws.write(7, 0, "Июль")
ws.write(8, 0, "Август")
ws.write(9, 0, "Сентябрь")

ws.write(10, 0, "Октябрь")
ws.write(11, 0, "Ноябрь")
ws.write(12, 0, "Декабрь")

x_cash = 1
y_bez_nal = 1

# Функция подсчета финансов
def test():
    global bez_nal, cash, x_cash, y_bez_nal
    counter = 0
    # цикл по месяцам
    while counter < 12:
        cash = int(cash)
        bez_nal = float(bez_nal)
        cash = round(cash, 2)
        bez_nal = round(bez_nal, 2)
        cash = cash + 2000
        bez_nal = bez_nal + bez_nal * 0.30
        ws.write(x_cash, 1, cash)
        ws.write(y_bez_nal, 2, bez_nal)
        x_cash += 1
        y_bez_nal += 1
        cash = str(cash)
        bez_nal = str(bez_nal)

        counter = counter + 1

    return cash, bez_nal



test()

wb.save('example.xls')
# сохранения Файла “example.xls”

filepath = 'example.xls'


e_maill = 'grishinartyomvladimirovich@gmail.com'

def send_mail():
    global filepath, e_maill
    me = 'From: My Name <testartem1989@mail.ru>'
    you = 'To: ' + ', '.join(e_maill)
    url = "smtp.mail.ru" # Сервер отпраитель
    login = "testartem1989@mail.ru" # Адрес отправителя
    password = "artemida1artemida" # Пароль отправителя
    topic = "Proba3"

    # Compose attachment
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filepath, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(filepath))


    # Формируем заголовок письма
    msg = MIMEMultipart('mixed')
    msg['Subject'] = topic
    msg['From:'] = login
    msg['To'] = ', '.join(e_maill[0:2])  # отправка 2-м адресаиам
    msg['cc'] = ', '.join([e_maill[2]])  # отправка копии 1-му адресату

    msg.attach(part)


    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, e_maill, msg.as_string())

"""
mas = random.choice([1, 2, 3])

def mas_prov():
    if mas < 1:
        toaddr = "grishinartyomvladimirovich@gmail.com"
        send_mail()
        print("e-mail ", toaddr)
    elif mas > 1:
        toaddr = "hencerartem@gmail.com"
        send_mail()
        print("e-mail ", toaddr)
    else:
        toaddr = "hrishinartem@gmail.com"
        send_mail()
        print("e-mail ", toaddr)
"""

def main():
    send_mail()


if __name__ == '__main__':
    main()
