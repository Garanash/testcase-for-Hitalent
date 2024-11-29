import os

from src.module.render_tables import *


def main():
    mngr = TaskManager()
    render_start_table()
    choice = input('Введите номер команды которую вы хотите выполнить или нажмите q+enter: ')
    if choice == '1':
        mngr.load_tasks()
        print('База данных успешно загружена')
        input('Нажмите Enter для продолжения')
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        render_base_table()
        comm = input('Введите номер команды которую вы хотите выполнить или нажмите q+enter: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if comm == 'q':
            print('Всего доброго!')
            quit(1)
        else:
            render_task_table(comm, mngr)
        mngr.dump_db()


if __name__ == "__main__":
    main()
