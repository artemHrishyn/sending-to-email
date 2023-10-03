# ввод своих фин остатков
cash = int(input("Введите пожалуйста сколько у вас налички \n"))
bez_nal = int(input("Введите пожалуйста сколько у вас карточки\n"))
y = ["Январе", "Феврале", "Марте", "Апреле", "Мае", "Июне", "Июле", "Августе", "Сентябре", "Октябре", "Ноябре",
     "Декабре"]

masiv = []
# Функция подсчета финансов
def test():
    global bez_nal, cash, masiv
    counter = 0
    # цикл по месяцам
    while counter < 12:
        cash = int(cash)
        bez_nal = float(bez_nal)
        cash = 2000 + cash
        bez_nal = bez_nal + bez_nal * 0.1
        cash = round(cash, 2)
        bez_nal = round(bez_nal, 2)
        cash = str(cash)
        bez_nal = str(bez_nal)
        masiv = [f'У вас в {y[counter]} будет. Налички: {cash} На карточке: {bez_nal}']
        print(masiv)
        #print(f"\nУ вас в {y[counter]} будет: \n Налички:{cash}\n На карточке: {bez_nal}")
        counter = counter + 1
    return cash, bez_nal


# Проверка если у вас деньги, или нет
if (cash > 0) or (bez_nal > 0):
    # вызов функции
    test()
else:
    print("Вы бедные :(")