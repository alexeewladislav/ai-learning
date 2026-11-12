ai_model = "Qwen-2.5-Coder"
coding_keywords = ["код", "python", "программирование", "скрипт", "ошибка"]

print("Привет")
print("для завершения напишите 'Выход'.\n")

while True:
    user_request = input("Вы:")

    if user_request.lower() == "выход":
        print("До связи!")
        break

    is_coding = False
    for word in coding_keywords:
        if word in user_request.lower():
            is_coding = True
            break

    if is_coding:
        print(f"Перенаправляю задачу на модель {ai_model}\n")
    else:
        print("Отправляю базовой модели Квен2.5\n")