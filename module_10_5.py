import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            string = file.readline()
            if string.strip():
                all_data.append(string.strip())
            else:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':


    # Линейный вызов
    print('Линейный способ:')
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    total_time_linetype = time.time() - start_time
    print(f'Время выполнения: {total_time_linetype} секунд\n')





    # Многопроцессный
    print('Многопроцессный подход:')
    start_time = time.time()
    with multiprocessing.Pool() as p:
        p.map(read_info, filenames)
    total_time_multitype = time.time() - start_time
    print(f'Время выполнения: {total_time_multitype} секунд')





