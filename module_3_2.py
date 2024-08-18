def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    # Провекрка на корректность
    elif "@" not in recipient:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif "@" not in sender:
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif not recipient.endswith((".com", ".ru", ".net",)):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    elif not sender.endswith((".com", ".ru", ".net",)):
        print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
    # Проверка на отпровителя по  умолчанию
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient)
        return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
