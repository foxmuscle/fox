#--------------------------------------------
# outer =5 inner=5
for i in range(5):
    for j in range(5) :
        print( f'j:{j}',end='   ')
    print(f' i:{i}\\n')

#--------------------------------------------------
#[2]
#  *
#   *
#    *
#     *
#      *

for v in range(5) :
    for h in range(v+1):
        if h==v :
            print('*')
        else :
            print(' ', end='')
        


for v in range(5) :
    for h in range(v+1):
        print('*' if h==v else ' ', end='\n' if h==v else ' ')