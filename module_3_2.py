def send_email(message, recipient, *, sender="university.help@gmail.com"):
    for j in range(1):
        is_prime = False
        for i in (recipient, sender):
            if '@' not in i:
                print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
                is_prime = True
                continue
            if  i.endswith('.ru') or i.endswith('.com') or i.endswith('.net'):
                continue
            else:
                print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
                is_prime = True
            continue
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com' and is_prime == False:
            print('Письмо успешно отправлено с адресаа', sender, 'на адрес', recipient)
        elif sender != 'university.help@gmail.com'and is_prime == False:
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
