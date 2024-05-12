from django.test import TestCase
from .modelservice import TaskService


class TestTaskService(TestCase):
    def create_test_task(self):
        return TaskService().create('title', 'text')

    def test_create(self):
        self.assertEqual(self.create_test_task(), True)

    def test_delete(self):
        self.create_test_task()
        self.assertEqual(TaskService().delete(TaskService().get_last_by_id()), True)

    def test_get_last_by_id(self):
        self.create_test_task()
        task = TaskService().get_last_by_id()
        self.assertEqual(task, type(task) == int)

    def test_order_by_descending(self):
        self.create_test_task()
        self.create_test_task()
        tasks = TaskService().order_by_descending()
        self.assertEqual(tasks.count(), 2)
