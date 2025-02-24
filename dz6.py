def validate_input(text):
    try:
        if not text.isalpha():
            raise ValueError("Строка должна содержать только буквы!")
        print("Ввод корректен.")
    except ValueError as e:
        print(f"Ошибка: {e}")

user_input = input("Введите строку: ")
validate_input(user_input)