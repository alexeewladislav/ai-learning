models_config = {
    "Qwen-2.5-Coder": ["код", "phyton", "скрипт", "ошибк", "функц"],
    "DeepSeek-Math": ["посчитай", "математик", "уровнен", "сколько будет", "формул"],
    "Llama-3-Creative": ["придумай", "сказк", "стих", "идею", "напиши текст"],
    "YandexGPT-Translate": ["переведи", "перевод", "английский"]
}

def select_best_model(text):
    clean_text = text.strip().lower()

    for model_name, keywords in models_config.items():
        for word in keywords:
            if word in clean_text:
                return model_name

    return "Qwen-2.5-Base"

print("=== Мультимодельный роутер запущен ===")
print("Напишите 'выход' для завершения.\n")

while True:
    user_request = input("Вы: ")

    if user_request.strip().lower() == "выход":
        print("До связи!")
        break

    chosen_model = select_best_model(user_request)
    print(f"Запрос направлен на модель [{chosen_model}]\n")