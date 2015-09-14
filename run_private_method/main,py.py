class Test(object):
    def __init__(self):
        pass
    def __private(self):
        print "you are in private method"


t=Test()
print dir(t)
t._Test__private()