class Task(object):
    def test_task(self,arg):
        print arg


def run():
    task=Task()
    input = "test_task"
    b=getattr(Task, input)
    a=getattr(task, input)
    print a
    print b
    a("234")
    b(task,"123")

if __name__ == "__main__":
    run()