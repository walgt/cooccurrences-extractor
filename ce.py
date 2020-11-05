import sys,re
if(int(sys.argv[2])<2):
	print("Le deuxième argument doit être supérieur strictement à 1")
	sys.exit()
if(int(sys.argv[3])<1):
	print("Le troisième argument doit être supérieur strictement à 0")
	sys.exit()
if(int(sys.argv[4])<1 or int(sys.argv[5])<0 ):
	print("Le quatrième et cinquième arguments doivent être supérieur strictement à 0")
	sys.exit()

var=open(sys.argv[1],'r',encoding="UTF-8")
res=var.readlines()
l=[]
for i in (range(len(res))):
	
	l=l+re.findall(r"\w+",res[i].lower())
lc=int(sys.argv[2])
f={}
k=0
m=[]
i=0
while (i<lc):
	m.append(l[k])
	k+=1
	i+=1
k=1
j=0

while(m[-1]!=l[-1]):
	i=0
	
	k=j+1
	f[tuple(m)]=f.get(tuple(m),0)+1
	m=[]
	while (i<lc):
		m.append(l[k])
		k+=1
		i+=1
	j=j+1
	
f[tuple(m)]=f.get(tuple(m),0)+1
k=len(l)-lc
while (i<lc):
	m.append(l[k])
	k+=1
	i+=1

f[tuple(m)]=f.get(tuple(m),0)+1

nb=0


for i in sorted(f.keys()):
	
	if(len(i[0])==int(sys.argv[4]) and len(i[-1])==int(sys.argv[5]) and (f[i]==int(sys.argv[3]))):
		for j in i:
			print(j,"",end="")
		nb+=1
		print("\n")

print("*********",nb,"cooccurrences","*********")

var.close()
