import logging
from datetime import datetime

# Настройка логгера
logging.basicConfig(filename="test_log.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Логирует информационные сообщения.
def log_info(message):
    logging.info(message)

# Логирует сообщения об ошибках.
def log_error(message):
    logging.error(message)

# Читает тест из файла и возвращает список вопросов с ответами.
def read_test_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            questions = []
            num_questions = int(file.readline().strip())
            for _ in range(num_questions):
                question_text = file.readline().strip()
                num_answers = int(file.readline().strip())
                correct_answer_index = int(file.readline().strip())
                answers = [file.readline().strip() for _ in range(num_answers)]
                questions.append((question_text, correct_answer_index, answers))
            log_info("Тестовый файл успешно прочитан.")
            return questions
    except Exception as e:
        log_error(f"Ошибка чтения тестового файла: {e}")
        return None

# Запускает тест, задавая вопросы пользователю и проверяя ответы.
def run_test(questions):
    correct_count = 0
    for i, (question, correct_index, answers) in enumerate(questions, start=1):
        print(f"Вопрос {i}: {question}")
        log_info(f"Вопрос {i}: {question}")
        for idx, answer in enumerate(answers, start=1):
            print(f"{idx}. {answer}")
        try:
            user_answer = int(input("Ваш ответ (номер варианта): "))
            if user_answer == correct_index:
                print("Правильно!\n")
                log_info(f"Правильный ответ на вопрос {i}.")
                correct_count += 1
            else:
                print(f"Неправильно. Правильный ответ: {correct_index}\n")
                log_info(f"Неправильный ответ на вопрос {i}. Правильно было {correct_index}.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите номер ответа.\n")
            log_error(f"Неверный ввод для вопроса {i}.")
    return correct_count

# Главная функция, которая запускает процесс тестирования.
def main():
    filename = "test.txt"  # Имя файла с тестом
    questions = read_test_file(filename)  # Чтение теста из файла
    if questions:
        total_questions = len(questions)  # Общее количество вопросов
        correct_answers = run_test(questions)  # Запуск теста
        score_percent = (correct_answers / total_questions) * 100  # Рассчёт процента правильных ответов
        print(f"Ваш результат: {correct_answers} из {total_questions} ({score_percent:.2f}%)")
        log_info(f"Тест завершен. Результат: {score_percent:.2f}% ({correct_answers}/{total_questions})")


if __name__ == "__main__":
    main()
