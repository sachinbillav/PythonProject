from threading import *
class Hello(Thread):

    def run2(self):
        for i in range(500):
            print("hello")
    def run(self):
        self.run2()

class Hi(Thread):
    def run1(self):
        for i in range(500):
            print("Hi")
    def run(self):
        self.run1()



t1 = Hello()
t2 = Hi()

t1.start()
t2.start()
t1.join()
t2.join()
print("#############################")