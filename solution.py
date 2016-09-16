mtn=0
voda=0
c=0
for i in range(10):
    a=input("enter a cellphone number(10digits)")
    if a[:3]=="083":
    	print("mtn user")
    	mtn=mtn+1
    elif a[:3]=="082":
    	print("voda user")
    	voda=voda+1
    elif a[:3]=="076":
    	print("voda user")
    	voda=voda+1
    elif a[:3]=="084":
    	print("cellc user")
    	c=c+1
    elif a[:3]=="062":
    	print("cellc user")
    	c=c+1
    else:
    	print("error")
print("there was",mtn,"amount of mtn users",voda,"amount of voda users and",c,"amount of cell c users")     	
