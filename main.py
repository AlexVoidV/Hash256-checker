import hashlib as hsh


# Путь к файлу
while True:
    try:
        file_path = input("Укажите путь к файлу: ").strip()
        with open(file_path, "rb") as f:
            digest = hsh.file_digest(f, "sha256")
        break
    except FileNotFoundError:
        print("Файл не найден!")

# Преобразование в строку
file_hash = digest.hexdigest()

# Получить хэш от пользователя
user_hash = input("Введите предоставленный разработчиком хэш: ").strip()

# Сравнить
print(f"Хэш указанного файла: {file_hash}")
print(f"Введённый хэш: {user_hash}")

# Результат
if file_hash.lower() == user_hash.lower():
    print("Хэш совпадает")
else:
    print("Хэш не совпал!")
