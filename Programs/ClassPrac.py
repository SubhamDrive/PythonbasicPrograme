class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.bal=0


    def greting(self):
        print(f'My name is {self.name} and age is {self.age} and i earn {self.bal}')

    def balance(self,bal):
        self.bal=bal



u1 = user('Subham choudhary',25)
print("My name is "+str(u1.name))
print("My age is "+str(u1.age))
u1.bal=200
print(u1.greting())



