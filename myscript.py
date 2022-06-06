
class Myclass:
    amount = 1000

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = fname + '.' + lname + "@" + "comp.com"

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    @classmethod
    def salary(cls, amt):
        cls.amount = amt

    @staticmethod
    def weekday_(day):
        if day.weekday()==5 or day.weekday()==6:
            return False

        return True




guy1 = Myclass("Ram", "Raju", 24 )

my_list = ["abc", "bfg", "hjk", "uio"]
for x, y in enumerate(my_list):
    print(x, y)




        
