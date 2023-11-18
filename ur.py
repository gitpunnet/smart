ee=int(input("enter number"))
ss=int(input("enter number"))
dd=input("enter sign")
rr=(int(ee)+int(ss))
tt=(int(ee)-int(ss))
ww=(int(ee)//int(ss))
ff=(int(rr)*int(tt))
if("*"==dd):
 print(ff)
elif("+"==dd):   
 print(rr)
elif("-"==dd):
 print(tt)
elif("/"==dd):
    print(ww)
else:
 print("error")
