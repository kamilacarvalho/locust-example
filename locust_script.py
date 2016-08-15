from locust import TaskSet, task, HttpLocust

class ConverterTasks(TaskSet):
    @task
    def f_to_c(self):
        self.client.get('/FC/20')


class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000