n=int(input())
m=int(input())
result=8
if m==0:
    result=1
if n==1:
    result=2
if n==2 :
    if m==1:
        result=3
    else:
        result=4
if m==1:
    result=4
if m==2:
    result=7
print(result)