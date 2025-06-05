m =int(input("No of Rows : "))
n = int(input("No of Columns : "))
tree = int(input("Tree No : "))
tr=[]
num = 1
for i in range(0,m):
    for j in range(0,n):
        
        if(i==0 or j==0 or j==n-1):
            print(num,end="\t ")
            tr.append(num)
        else:
            print(" ",end="\t ")
        num+=1
    print()
if(tree in tr):
    print("\t\tYES, Tree is present")
else:
    print("\t\tNO, Tree is not present")