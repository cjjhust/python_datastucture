class Test:
    def __init__(self, i):
        self.i = i
for i in range(10):
    t = Test(i)
    print(t.i)
    print(hash(t), id(t))
