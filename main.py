class ToDoList:
    def __init__(self):
        self.tasks = []


    def add_task(self, task):
        task_exists = False
        for new_task in self.tasks:
            if new_task['task'] == task:
                task_exists = True
                break

        if task_exists:
            print("Задача уже существует.")
            return

        self.tasks.append({'task': task, 'completed': False})


    def complete_task(self, task):
        for complete_task in self.tasks:
            if complete_task['task'] == task:
                if complete_task['completed']:
                    print("Задача уже выполнена.")
                else:
                    complete_task['completed'] = True
                return

        print("Задача не найдена.")


    def remove_task(self, task):
        remove_task = None
        for task_to_remove in self.tasks:
            if task_to_remove['task'] == task:
                remove_task = task_to_remove
                break

        if remove_task:
            self.tasks.remove(remove_task)
        else:
            print("Задача не найдена.")


    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        for task in self.tasks:
            status = "V" if task['completed'] else "X"
            print(f"{task['task']} - {status}")


todo = ToDoList()
todo.add_task("Сделать зарядку")
todo.add_task("Приготовить еду на весь день")
todo.add_task("Продолжить курс основы Python")
todo.add_task("Почитать теорию ручного тестирования (вечером)")
todo.complete_task("Сделать зарядку")
todo.complete_task("Приготовить еду на весь день")
todo.list_tasks()
todo.remove_task("Почитать теорию ручного тестирования")
todo.remove_task("Почитать теорию ручного тестирования (вечером)")
todo.list_tasks()