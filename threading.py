#Реалізація багатопотокового підходу
import os
import threading

# Функція для пошуку ключових слів у файлі
def search_keywords_in_file(filename, keywords):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    for keyword in keywords:
        if keyword in text:
            print(f"Keyword '{keyword}' found in file '{filename}'")

# Функція для обробки файлів у потоці
def process_files(files, keywords):
    for filename in files:
        search_keywords_in_file(filename, keywords)

def main_threading():
    keywords = ['Lorem', 'dolore', 'veniam']
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    
    # Поділ файлів між потоками
    num_threads = 3
    threads = []
    for i in range(num_threads):
        thread_files = files[i::num_threads]
        thread = threading.Thread(target=process_files, args=(thread_files, keywords))
        threads.append(thread)
        thread.start()

    # Очікуємо завершення роботи всіх потоків
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main_threading()
