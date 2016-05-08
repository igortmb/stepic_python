class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append (self,x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError("NonPositiveError")


a = PositiveList()
a.append(-2)
print(a)