"""values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)


color =['red','blue','orange','gray']
print(color[0])
print(color[-1])

def exam_st_date(dd,mm,yyyy):
     date=dd
     month=mm
     year=yyyy
     print("Your Examnation will start form: {0}/{1}/{2}".format(date,month,year))

dd  = int(input("Enter Date: "))
mm  = int(input("Enter Month: "))
yyyy= int(input("Enter Year: "))
exam_st_date(dd,mm,yyyy)

import datetime

now= datetime.datetime.now()
y
print(now)
print(yy)

from datetime import date
f_date = date(2019,7,2)
l_date=    date(2019,12,2)
print(l_date-f_date)



list1 = ['ab','tb','cb','db','mb','gb','kb']
print(list1[1])
print(list1[-1])
print(list1[2:4])
print(list1[4:2])
print(list1[-4:-2])
print(list1[:5])
print(list1[2:])
print(list1[:])
list1[0]='ub'
print(list1)

for x in list1:
    print(x)

if 'ub' in list1:
    print("true")
else:
    print("false")

print(len(list1))

list1.append('hb')
print(list1)

list1.insert(1,'Tb')
print(list1)

list1.remove("Tb")
print(list1)

list1.pop()
print(list1)

del list1[1]
print(list1)

list1.clear()
print(list1)

tuple1 = (1,2,3,4,5,6,7,8)
print(tuple1)
print(tuple1[-1])
print(tuple1[2:5])
lis =list(tuple1)
lis[1]=9
l=tuple(lis)
print(l)

for x in l:
    print(l)

if 3 in l:
    print("true")
else:
    print("False")

print(len(l))

t1 =(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)

t4 = tuple((1,2,3,4,5,6,6,7,8,))
print(t4)

#we can not add and delete tuple items we have to delte tuple completetly

"""


s1={1,2,3,4,5,5,6,7,8,8,8}
print(s1)
s2 = {'sub','sonu','ronu','rishu','rinku','akash','ankur','mitthu'}
print(s2)

for x in s2:
    print(x)

if 'sub' in s2:
    print("Avialable")
else:
    print("Not Avialable")


#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.

s2.add("ramu")
print(s2)

s2.update(['sneha','priyanka'])
print(s2)
print(len(s2))
s2.remove("ramu")
print(s2)
print(len(s2))

#Note: If the item to remove does not exist, remove() will raise an erro
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.



