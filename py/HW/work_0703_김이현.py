
#--17 while ---------->19

# 구구단 천체 출력 => 중첩for -> for 1개로  연산자 활용




# for i in range(1, 10):
#     for j in range(2, 10):
#         print(f"{j} x {i} ={i * j:2}", end="   ")
#     print()

# #구구단 전체 출력 => 가로로 출력 : 중첩 for,for 1개....-_-
# for i in range(1, 10):
#     for j in range(2, 10):  # 2부터 9단까지 출력
#         # 구구단 계산
#         result = i * j
#         # 출력 포맷 지정하여 가로로 출력
#         print(f"{j} x {i} = {result:2}", end="\t")
#     # 한 줄이 끝나면 줄 바꿈
#     print()



# for i in range(1, 10):
#     for j in range(2, 10):  # 2부터 9단까지 출력
#         # 구구단 계산
        
#         # 출력 포맷 지정하여 가로로 출력
#         print(f"{j} x {i} = {j*i:2}", end="\t")
#     # 한 줄이 끝나면 줄 바꿈
#     print()


# #p195-------------------------------------------------------------

             
# i=0
# while i<100 :
#     print('H',i)
#     i += 1

# i=1
# while i<=100 :
#     print('H',i)
#     i += 1
# #p202--------------

# i=2
# j=5

# while i<=32 or j>1 :
#     print(i,j)
#     i=i*2
#     j=j-1

# #203----------------------
# m=int(input())
# while m>=1350 :
#     m=m-1350
#     print(m)

# #206----------------
# for i in range(100):
#     if i %2 ==0 :
#         continue
#     print(i)
# print('끝')


# i =0
# while i <100 :
#     i=i+1
#     if i% 2 ==0 :
#         continue
#     print(i)

# print('끝끝')
# i =0
# while i <100 :
#     i=i+1
#     if i% 2 ==0 :
#         print(i)

#p211-----------------------------------
# i=0
# while True :
#     if i % 10 !=3 :
#         i+=1
#         continue
#     if i> 73:
#         break
#     print(i,end=' ')
#     i +=1
# 0~73 사이이 숫자중 3으로 끝나는 숫자 출력

#3,13,23,33,43,53,63,73->10으로 나누었을대 나머지가 3
#
i=0
while True :
    if i>73: break
    if i%10 !=3 : 
        i=i+1
        continue
print(i,end='')








#-----------------------------------------------
i=0
while True :
    if i %10  !=3 :
        i=i+1
        continue
    if i>73 :
        break
    print(i ,end="  ")
    i=i+1
#p216----------------------
for i in range(3):
    for j in range(7):
        print( '*',end=' ')
        


for i in range(5):
    for j in range(5):
        if j<=i :
            print('*',end='')
    print()