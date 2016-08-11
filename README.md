The main feature of the Locust is the way the tests, simple python code are written. With a few lines of code you can write strong tests.

Installation:
http://docs.locust.io/en/latest/installation.html

Test aplication:

To demonstrate the use of the Locust, is necessary to create a simple web service that performs conversions of time (eg. Time for second).

In creating this web service, will be used Flask to be one of the simplest and frameworks currently used. As the Locust use Flask internally, it is already installed in our virtualenv.

Create a file called `converter.py` with the following code:

```javascript
from flask import Flask


converter = {'DH': lambda d: d * 24,     # day to hours
             'HM': lambda h: h * 60,     # hour to minutes
             'MS': lambda m: m * 60,     # minute to seconds
             'DM': lambda d: d * 1440,   # day to minutes
             'DS': lambda d: d * 86400,  # day to seconds
             'HS': lambda h: h * 3600}   # hour to seconds

app = Flask(__name__)

@app.route('/<rule>/<int:value>')
def conversion(rule, value):
    try:
        return str(converter[rule.upper()](value))
    except KeyError:
        return "Rule for conversion not found", 404


if __name__ == "__main__":
    app.run()
```

Importing Flask
```javascript
from flask import Flask
```
This code block deals the conversion time.
```javascript
converter = {'DH': lambda d: d * 24,     # day to hours
             'HM': lambda h: h * 60,     # hour to minutes
             'MS': lambda m: m * 60,     # minute to seconds
             'DM': lambda d: d * 1440,   # day to minutes
             'DS': lambda d: d * 86400,  # day to seconds
             'HS': lambda h: h * 3600}   # hour to seconds
```

?????
```javascript
@app.route('/<rule>/<int:value>')
def conversion(rule, value):
    try:
        return str(converter[rule.upper()](value))
    except KeyError:
        return "Rule for conversion not found", 404


if __name__ == "__main__":
    app.run()
```

To execute this application you need to use the command ```python converter.py```:
```javascript
(venv)user@machine:~/locust$ python converter.py
 * Running on http://127.0.0.1:5000/
```

To check if your application is running, open another tab in the terminal and make the following request:
```javascript
curl http://127.0.0.1:5000/hm/3
180
```

Locus test:
The tests are based on ```Tasks``` that are created in a class that inherits from the Locust ```taskset``` class. In taskset class which determines whether a method is a task is the presence of ```@task``` decorator.

The Locust works with the concept of requests based on customers with specific characteristics. The main attribute of Locust client classes is ```task_set``` attribute, receiving the test class where tasks are specified. Since the focus is web application test, the relevant protocol is the HTTP protocol, so the base class for the creation of these customers is ```HttpLocust class```.

To test some methods of our webservice, create a file called ```locust_script.py``` with the following code.
```javascript
from locust import TaskSet, task, HttpLocust

class ConverterTasks(TaskSet):
    @task
    def day_to_hour(self):
        self.client.get('/dh/5')

    @task
    def day_to_minute(self):
        self.client.get('/dm/2')


class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000
```
