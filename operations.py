from os import getcwd, makedirs
from random import randint
import time
import threading


class FileCreator:
    """
    Класс для ежеминутного создания файлов на диске
    """
    def __init__(self):
        self.execution = False
        self.cur_dir = getcwd()

    def create_file(self):
        """
        создать файл в директории
        """
        num = str(randint(0, 10 ** 10 - 1))
        directory = self.cur_dir + '\\' + '\\'.join(list(num))

        try:
            makedirs(directory)
        except OSError:
            pass

        with open(directory + '\\' + num + '.txt', 'w') as file:
            file.write(num)
            file.close()

    def create_files_process(self):
        """
        создание файлов пока взведен флаг выполнения потока
        """
        while self.execution:
            self.create_file()
            time.sleep(1)

    def start_thread(self):
        """
        запустить выполнение потока
        :return: логический результат выполнения операции
        """
        if self.execution:
            return False

        self.execution = True
        thread = threading.Thread(target=self.create_files_process)
        thread.start()

        return True

    def stop_thread(self):
        """
        завершить выполнение потока
        :return: логический результат выполнения операции
        """
        if not self.execution:
            return False

        self.execution = False

        return True
