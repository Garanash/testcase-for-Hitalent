import json
import logging
import unittest

from src.module.clases import TaskManager, Task


class MyTestCase(unittest.TestCase):

    def test_add(self):
        my_mngr = TaskManager()
        my_mngr.new_task(Task('Название', 'Описание', 'Категория', 'Дата', 'Приоритет', 'Статус'))
        self.assertEqual(len(my_mngr.task_list), 1)

        new_mngr = TaskManager()
        for i in range(10):
            new_mngr.new_task(Task(f'Название{i}', 'Описание', 'Категория', 'Дата', 'Приоритет', 'Статус'))
        self.assertEqual(len(new_mngr.task_list), 10)

    def test_load(self):
        new_mngr_1 = TaskManager()
        new_mngr_1.load_tasks()
        with open('database.json', 'r') as file:
            json_file = json.load(file)
        self.assertEqual(len(new_mngr_1.task_list), len(json_file))

    def test_search(self):
        new_mngr_2 = TaskManager()
        new_mngr_2.load_tasks()
        self.assertEqual(len(new_mngr_2.search_task('документацию', 'discription')), 2)
        self.assertEqual(len(new_mngr_2.search_task('Посмеяться', 'title')), 1)
        self.assertEqual(len(new_mngr_2.search_task_id(1)), 1)

    def test_delete(self):
        new_mngr_3 = TaskManager()
        new_mngr_3.load_tasks()
        with open('database.json', 'r') as file:
            json_file = json.load(file)
        new_mngr_3.delete_task('1')
        self.assertEqual(len(new_mngr_3.task_list), len(json_file) - 1)


logging.basicConfig(level=logging.DEBUG)

suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
testResult = unittest.TextTestRunner(verbosity=2).run(suite)

for test in testResult.failures + testResult.errors:
    logging.error("FAIL: %s" % test[0])

if __name__ == '__main__':
    unittest.main()
