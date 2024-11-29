import json


class Task:
    """
    Класс задачи
    """
    _id_key = 1

    def __init__(self, id=None, title=None, discription=None, category=None, due_date=None, priority=None,
                 status='Создан'):
        if id:
            self.id = id
            Task._id_key += 1
        else:
            self.id = Task._id_key
            Task._id_key += 1
        self.title = title
        self.discription = discription
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = status

    def __repr__(self):
        return f" {self.id} {self.title} {self.category} {self.due_date} {self.priority} {self.status}"


class TaskManager:
    """
    Класс менеджера задач
    """

    def __init__(self):
        self.task_list = []

    def load_tasks(self):
        with open('database.json', 'r') as file_in:
            self.task_list = [Task(**task) for task in json.load(file_in)]

    def new_task(self, other: Task) -> None:
        self.task_list.append(other)

    def search_task(self, request: str, where: str) -> list:
        neded_task = []
        for task in self.task_list:
            if where == 'title' or where == 'discription':
                if request in task.__getattribute__(where):
                    neded_task.append(task)
            else:
                if task.__getattribute__(where) == request:
                    neded_task.append(task)
        return neded_task

    def search_task_id(self, search_id: int) -> list:
        needed = []
        for task in self.task_list:
            if task.id == search_id:
                needed.append(task)
        return needed

    def delete_task(self, request: str) -> int:
        delete_index = []
        for index in range(len(self.task_list)):
            if str(self.task_list[index].id) == request or self.task_list[index].category == request:
                delete_index.append(index)
        for index in delete_index[::-1]:
            self.task_list.pop(index)
        return len(delete_index)

    def change_task(self, needed_id: str, where: str, new_data: str) -> None:
        task = self.task_list[int(needed_id) - 1]
        task.__setattr__(where, new_data)

    def display_tasks(self, category: str = None) -> None:
        if category:
            for task in list(filter(lambda x: x.category == category, self.task_list)):
                print(task)
        else:
            for task in self.task_list:
                print(task)

    def dump_db(self):
        with open('database.json', 'w', encoding="UTF-8") as file_out:
            json.dump([x.__dict__ for x in self.task_list], file_out, ensure_ascii=False, indent=2)
