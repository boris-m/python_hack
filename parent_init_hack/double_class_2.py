
class parent(object):
    id = 0
    count = 0

    @property
    def id(self):
        parent.count += 0.5
        return int(parent.count)


class cl1(parent):
    def __init__(self):
        self.tmp=self.id

def run():
    print cl1().id, cl1().id, cl1().id
    # 1 2 3
run()