class Test:
    def __init__(self, i):
        self.i = i
for i in range(10):
    t = Test(1)
    print(hash(t), id(t))
