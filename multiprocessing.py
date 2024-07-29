# Реалізація багатопроцесорного підходу
import os
import multiprocessing

# Функція для пошуку ключових слів у файлі
def search_keywords_in_file(filename, keywords, queue):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    results = []
    for keyword in keywords:
        if keyword in text:
            results.append(f"Keyword '{keyword}' found in file '{filename}'")
    queue.put(results)

# Функція для обробки файлів у процесі
def process_files(files, keywords, queue):
    for filename in files:
        search_keywords_in_file(filename, keywords, queue)

def main_multiprocessing():
    keywords = ['Lorem', 'dolore', 'veniam']
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    
    queue = multiprocessing.Queue()
    num_processes = 3
    processes = []
    for i in range(num_processes):
        process_files_part = files[i::num_processes]
        process = multiprocessing.Process(target=process_files, args=(process_files_part, keywords, queue))
        processes.append(process)
        process.start()

    # Очікуємо завершення роботи всіх процесів
    for process in processes:
        process.join()

    # Збираємо результати з черги
    while not queue.empty():
        results = queue.get()
        for result in results:
            print(result)

if __name__ == "__main__":
    main_multiprocessing()
