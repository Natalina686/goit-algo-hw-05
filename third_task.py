import timeit

# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0 or n == 0 or m > n:
        return []

    # Створення таблиці зсувів
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    shifts = []
    s = 0  # зсув
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            shifts.append(s)
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

    return shifts

# Алгоритм Кнута-Морріса-Пратта
def kmp(text, pattern):
    m = len(pattern)
    n = len(text)
    
    # Створення таблиці префіксів
    lps = [0] * m
    j = 0  # індекс для pattern
    i = 1  # індекс для lps

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    # Пошук підрядка
    i = 0  # індекс для text
    j = 0  # індекс для pattern
    shifts = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            shifts.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return shifts

# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    m = len(pattern)
    n = len(text)
    d = 256  # кількість символів в алфавіті
    q = 101  # просте число
    p = 0  # хеш для pattern
    t = 0  # хеш для text
    h = 1
    shifts = []

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                shifts.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            t = (t + q) % q  # Необхідно, щоб t був додатнім

    return shifts

def measure_time(algorithm, text, pattern):
    stmt = f"{algorithm.__name__}(text, pattern)"
    setup = f"from __main__ import {algorithm.__name__}; text={repr(text)}; pattern={repr(pattern)}"
    
    return timeit.timeit(stmt, setup, number=100)

# Функція для читання тексту з файлу
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Тексти для тестування
text1 = read_file("/Users/nata/Projects24/repository/goit-algo-hw-05/text1.txt")
text2 = read_file("/Users/nata/Projects24/repository/goit-algo-hw-05/text2.txt")

# Підрядки для тестування
existing_substring = "в бібліотеках популярних мов програмування"
existing_substring2 = "рекомендаційної системи є важливим з точки зору якості її роботи"
non_existing_substring = "вигаданий підрядок"

# Вимірювання часу для тексту 1
print("Текст 1:")
for algorithm in [boyer_moore, kmp, rabin_karp]:
    time_existing = measure_time(algorithm, text1, existing_substring)
    time_non_existing = measure_time(algorithm, text1, non_existing_substring)
    print(f"{algorithm.__name__}: існуючий - {time_existing:.6f}, вигаданий - {time_non_existing:.6f}")

# Вимірювання часу для тексту 2
print("Текст 2:")
for algorithm in [boyer_moore, kmp, rabin_karp]:
    time_existing = measure_time(algorithm, text2, existing_substring2)
    time_non_existing = measure_time(algorithm, text2, non_existing_substring)
    print(f"{algorithm.__name__}: існуючий - {time_existing:.6f}, вигаданий - {time_non_existing:.6f}")