##Багатопотоковий підхід (Threading):

- Поділяємо список файлів між різними потоками.
- Кожен потік виконує функцію process_files, яка обробляє свій піднабір файлів.
- Використовуємо метод join для очікування завершення всіх потоків перед завершенням основної програми.


##Багатопроцесорний підхід (Multiprocessing):

- Поділяємо список файлів між різними процесами.
- Кожен процес виконує функцію process_files, яка обробляє свій піднабір файлів.
- Використовуємо чергу (Queue) для збирання результатів пошуку з усіх процесів.
- Використовуємо метод join для очікування завершення всіх процесів перед збиранням та виведенням результатів з черги.