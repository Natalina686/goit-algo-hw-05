class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        # Якщо корзина пуста, додаємо нову пару
        if not self.table[key_hash]:
            self.table[key_hash] = list([key_value])
            return True
        else:
            # Перевіряємо, чи існує вже такий ключ
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value  # Оновлюємо значення
                    return True
            # Додаємо нову пару, якщо ключ не знайдено
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash]:
            for index, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][index]  # Видаляємо пару
                    return True
        return False  # Якщо ключ не знайдено

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   #  10
print(H.get("orange"))  #  20
print(H.get("banana"))  #  30

# Тестуємо видалення
H.delete("orange")
print(H.get("orange"))  # None (оскільки "orange" було видалено)

H.delete("apple")
print(H.get("apple"))   # None (оскільки "apple" було видалено)

print(H.get("banana"))  # 30 (оскільки "banana" залишилось)