from prettytable import PrettyTable

from src.module.clases import Task, TaskManager
from src.module.validation import *


def render_start_table():
    table_change = PrettyTable()
    table_change.align = "l"
    table_change.padding_width = 1
    table_change.field_names = ['#', 'Выберите действие']
    table_change.add_row(['1', 'загрузить задачи'], divider=True)
    table_change.add_row(['2', 'создать новый менеджер задач'], divider=True)
    print(table_change)


def render_base_table():
    table_change = PrettyTable()
    table_change.align = "l"
    table_change.padding_width = 1
    table_change.field_names = ['#', 'Выберите действие']
    table_change.add_row(['1', 'Показать все задачи'], divider=True)
    table_change.add_row(['2', 'Показать задачи по приоритету'], divider=True)
    table_change.add_row(['3', 'Добавить задачу'], divider=True)
    table_change.add_row(['4', 'Изменить задачу по id'], divider=True)
    table_change.add_row(['5', 'Изменить статус задачи'], divider=True)
    table_change.add_row(['6', 'Удалить задачу по id'], divider=True)
    table_change.add_row(['7', 'Удалить категорию задач'], divider=True)
    table_change.add_row(['8', 'Поиск задачи по ключевым словам, категории или статусу выполнения'], divider=True)
    print(table_change)


def render_task_table(choice: str, mngr: TaskManager) -> None:
    if choice == '3':
        print('Окей давайте добавим новую задачу')
        title_task = input('Введите название задачи: ')
        discription_task = input('Введите описание задачи: ')
        category_task = input('Введите категорию задачи: ')
        due_date_task = input('Введите дату до которой нужно выполнить задачу: ')
        priority_task = input('Введите приоритет: ')
        data = [title_task, discription_task, category_task, due_date_task, priority_task]
        if check_data(data):
            new_task = Task(title=title_task, discription=discription_task, category=category_task,
                            due_date=due_date_task, priority=priority_task)
            mngr.new_task(new_task)
            print('Данные корректны, задача добавлена')
        else:
            print('Задача не добавлена, введены не корректные данные')
        table_task = PrettyTable()
        table_task.field_names = (['id', 'title', 'discription', 'category', 'due_date', 'priority', 'status'])
        table_task.add_row(mngr.task_list[-1].__dict__.values())
        print(table_task)
        input('Нажмите Enter для продолжения')
    elif choice == '1':
        table_task = PrettyTable()
        table_task.field_names = (['id', 'title', 'discription', 'category', 'due_date', 'priority', 'status'])
        for task in mngr.task_list:
            table_task.add_row(task.__dict__.values(), divider=True)
        print(table_task)
        input('Нажмите Enter для продолжения')
    elif choice == '2':
        next_choice = input('Введите приоритет (Высокий, Средний, Низкий)')
        while not is_valid_priority(next_choice):
            print('Введен не корректный приоритет')
            next_choice = input('Введите приоритет (Высокий, Средний, Низкий)')
        table_task = PrettyTable()
        table_task.field_names = (['id', 'title', 'discription', 'category', 'due_date', 'priority', 'status'])
        for task in mngr.search_task(next_choice, 'priority'):
            table_task.add_row(task.__dict__.values(), divider=True)
        print(table_task)
        input('Нажмите Enter для продолжения')
    elif choice == '4':
        print('Окей давайте изменим задачу:')
        choice_id = input('Введите id задачи которую хотим поменять')
        flag = False
        try:
            new_choice = input(
                'Введите параметр который хотите поменять\n(id,title,discription,category,due_date,priority,status): ')
            new_data = input('Введите данные которые нужно поставить')
            needed_task = mngr.search_task_id(int(choice_id))
            if len(needed_task) == 1:
                if new_choice == 'due_data':
                    if is_valid_date(new_data):
                        mngr.change_task(mngr.task_list[mngr.task_list.index(needed_task[0])].id, new_choice, new_data)
                        flag = True
                    else:
                        print('Введенная дата не корректна')
                        input('Нажмите Enter для продолжения')
                elif new_choice == 'priority':
                    if is_valid_priority(new_data):
                        mngr.change_task(mngr.task_list[mngr.task_list.index(needed_task[0])].id, new_choice, new_data)
                        flag = True
                    else:
                        print('Введенный приоритет не корректен')
                        input('Нажмите Enter для продолжения')
                else:
                    if is_not_none(new_data):
                        mngr.change_task(mngr.task_list[mngr.task_list.index(needed_task[0])].id, new_choice, new_data)
                        flag = True
                    else:
                        print('Вы ввели пустую строку, такое изменение данных не корректно')
                        input('Нажмите Enter для продолжения')
                if flag:
                    table_task = PrettyTable()
                    table_task.field_names = (
                        ['id', 'title', 'discription', 'category', 'due_date', 'priority', 'status'])
                    table_task.add_row(mngr.task_list[mngr.task_list.index(needed_task[0])].__dict__.values())
                    print(table_task)
                    input('Нажмите Enter для продолжения')
            else:
                print('Такая задача не одна')
                input('Нажмите Enter для продолжения')
        except ValueError:
            print('Не корректные данные')
            input('Нажмите Enter для продолжения')
    elif choice == '5':
        print('Окей давайте поменяем статус задачи')
        choice_id = input('Введите id задачи которую хотим поменять')
        try:
            needed_task = mngr.search_task_id(int(choice_id))
            if len(needed_task) == 1:
                mngr.change_task(mngr.task_list[mngr.task_list.index(needed_task[0])].id, 'status', 'Выполнена')
                table_task = PrettyTable()
                table_task.field_names = (
                    ['id', 'title', 'discription', 'category', 'due_date', 'priority', 'status'])
                table_task.add_row(mngr.task_list[mngr.task_list.index(needed_task[0])].__dict__.values())
                print(table_task)
                input('Нажмите Enter для продолжения')
            else:
                print('Такая задача не одна')
                input('Нажмите Enter для продолжения')
        except ValueError:
            print('Не корректные данные')
            input('Нажмите Enter для продолжения')
    elif choice == '6':
        print('Окей давайте удалим задачу')
        choice_id = input('Введите id задачи которую хотим удалить')
        try:
            needed_task = mngr.search_task_id(int(choice_id))
            if len(needed_task) == 1:
                mngr.delete_task(choice_id)
                print('Эта задача была удалена')
                input('Нажмите Enter для продолжения')
            else:
                print('Такая задача не одна')
                input('Нажмите Enter для продолжения')
        except ValueError:
            print('Не корректные данные')
            input('Нажмите Enter для продолжения')
    elif choice == '7':
        print('Окей давайте удалим категорию задач')
        new_choice = input('Введите категорию задач которую вы хотите удалить: ')
        k = mngr.delete_task(new_choice)
        if k > 0:
            print('Категория задач удалена')
        else:
            print('Такой категории нет')
        input('Нажмите Enter для продолжения')
    elif choice == '8':
        print('Окей давайте найдем задчу по ключевому слову, категории или статусу')
        new_choice = input('Введите ключевое слово, категорию или статус')
        res1 = mngr.search_task(new_choice, 'title')
        res2 = mngr.search_task(new_choice, 'discription')
        res3 = mngr.search_task(new_choice, 'category')
        res4 = mngr.search_task(new_choice, 'status')
        all_res = res1 + res2 + res3 + res4
        if all_res:
            print('По Вашему запросу найдено:')
            table_res = PrettyTable()
            table_res.field_names = (['id', 'title', 'discription', 'category', 'due_date', 'priority', 'status'])
            for task in all_res:
                table_res.add_row(task.__dict__.values())
            print(table_res)
            input('Нажмите Enter для продолжения')
        else:
            print('По Вашему запросу ничего не найдено')
            input('Нажмите Enter для продолжения')
    else:
        print('Вы ввели не корректные данные')
        input('Нажмите Enter для продолжения')
