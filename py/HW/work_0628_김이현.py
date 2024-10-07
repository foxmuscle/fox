#p109------------------------------------------------
nums= list(range(5,-10,-2))
print(nums)

nums=list(range(-10,9,2))
print(nums)

nums=list(range(-10,9,3))
print(nums)

#140--------------------------------------------------
year = [2011,2013,2014,2015,2016,2017,2018]
population=[10249679,10195318,10143645,1003233,10022181,9930616,9857426,9838892]

print(year[-3:])
print(population[-3:])

#p141-----------------------------------------------------------
n =-32,75,97,-10,9,32,4,-15,0,76,14,2
print(n[1:100:2])
print(n[1:len(n):2])

#------------------------------------------
x=[1,2,3,4,5,6,7,8,9,10]
x[:]=['1','2','3','4','5']
print(tuple(x))


x='1 2 3 4 5 6 7 8 9 10'
x2=x.split(' ')
print(x2)
del x2[-5:]
print(tuple(x2))

x='1 2 3 4 5 6 7 8 9 10'
x2=x.split(' ')
print(x2)
print(tuple(x2[1:6]))

# del x[-5:]
# print(x)
# x[:]=['1','2','3','4','5']
# print=x

#p142--------------------------------------------------------------
m='oven bat pony total leak curl crop space navy loss knee'
m2=m.split(' ')
print(m2)
print(tuple(m2[:6]))


#----------------------------------------
a='python'
b='python'

aa=a[1::2]
bb=b[::2]
print(aa+bb)
#--------
a='apple'
b='strawberry'

aa=a[1::2]
bb=b[::2]
print(aa+bb)

