# merge and sort two array
list1=[]
list2=[]
num1=int(input('enter no.of fst list:'))
for i in range(1,num1+1):
    a = int(input('enter element:'))
    list1.append(a)


num2= int(input('enter no.of scnd list:'))
for i in range(1,num2+1):
    b = int(input('enter element:'))
    list2.append(b)

list = list1 + list2
list.sort()
print('sorted list is :',list)