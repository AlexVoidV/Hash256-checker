import hashlib as hsh


def calculate_file_hash(file_path, variant):
    if variant == "y":
        hash_obj = hsh.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    else:
        with open(file_path, "rb") as f:
            digest = hsh.file_digest(f, "sha256")
        return digest.hexdigest()


def check_hashes(hash1, hash2):
    if hash1.lower() == hash2.lower():
        return True
    else:
        return False


def main():
    variant = input("Ваш файл тяжелее 1 ГБ? (y / n): ").strip().lower()
    while True:
        try:
            # Путь к файлу
            file_path = input("Укажите путь к файлу: ").strip()
            # Преобразование в строку хэш файла
            file_hash = calculate_file_hash(file_path, variant)
            break
        except FileNotFoundError:
            print("Файл не найден!")
    # Получить хэш от пользователя
    user_hash = input("Введите предоставленный разработчиком хэш: ").strip()
    # Вывести для сравнения
    print(f"Хэш указанного файла: {file_hash}")
    print(f"Введённый хэш: {user_hash}")
    # Результат
    if check_hashes(file_hash, user_hash):  # == True
        print("Хэш совпадает")
    else:
        print("Хэш не совпал!")


if __name__ == "__main__":
    main()
