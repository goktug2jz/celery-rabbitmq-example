from celery import Celery

# Celery uygulamasını oluşturuyoruz
app = Celery('tasks', broker='pyamqp://goktug:123456@192.168.248.141:5672//')

# Basit bir görev tanımlıyoruz
@app.task
def add(x, y):
    return x + y
