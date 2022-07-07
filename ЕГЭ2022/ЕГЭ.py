#python "C:\Test\ege15.py"

#14 задание
'''
f = 5*343**8+4*49**12+7**14-98

s =''

while f >0:
	s = s + str(f%7)
	f = f// 7

print(s.count('6'))
'''
# 8 задание
'''
k=0
for x1 in 'росомаха':
	for x2 in 'росомаха':
		for x3 in 'росомаха':
			for x4 in 'росомаха':
				for x5 in 'росомаха':
					for x6 in 'росомаха':
						for x7 in 'росомаха':
							for x8 in 'росомаха':
								s=x1+x2+x3+x4+x5+x6+x7+x8
								if s.count('р')==1 and s.count('о')==2 and s.count('с')==1 and s.count('м')==1 and s.count('а')==2 and s.count('х')==1:
									if s.count ('оо')==0  and s.count ('аа')==0 and s.count ('ао')==0 and s.count ('оа')==0 and s.count ('рс')==0 and s.count ('ср')==0 and s.count ('см')==0 and s.count ('мс')==0 and s.count ('сх')==0 and s.count ('хс')==0 and s.count ('рм')==0 and s.count ('мр')==0 and s.count ('рх')==0 and s.count ('хр')==0 and s.count ('мх')==0 and s.count ('хм')==0:
										k+=1
print(k)	
'''
# 16 задание
'''
def F(n):
	if n%2 == 1:
		return F(n-1)+1
	if (n % 2 ==0) and (n >=0) :
		return F(n/2)
k=0
i=0
while i<1000000000:
	i+=1
	if F(i) == 2:
		k += 1
print(k)
print(F(0))
'''
# 12 задание
'''
for ed in range (1,100):
	for dv in range (1,100):
		for tr in range (1, 100):
			s = '0'+'1'*ed+'2'*dv+'3'*tr+'0'

			while not ('00') in s:
				s = s.replace('01','210',1)
				s = s.replace('02','3101',1)
				s = s.replace('03','2012',1)

			if s.count('1')==70 and s.count('2')==56 and s.count('3')==23:
				print(2+ed+dv+tr)
				break
'''
#17задание
'''
with open('C:\\Test\\17.txt') as f:
	numbers = [int(x) for x in f]
	s =[]
	for i in range(1, len(numbers)):
		if numbers[i] % 3 ==0 or numbers[i-1] % 3==0:
			s.append(numbers[i]+numbers[i-1])
	print(len(s), max(s))
'''
#15 задание
'''
A=1
while True:
	for x in range(0,1000):
		for y in range(0,1000):
			if not():
				break
		else:
			continue
		break
	else:
		print(A)
	A+=1
print(A)
'''
#19
'''
#x-первая куча, y -вторая куча, n -кол-во ходов

def f(x,y,n):
	if n==2 and x+y>=77: return True
	elif n<2 and  x+y>=77: return False
	elif n==2 and x+y<77: return False
	else:
		return f(x+1,y,n+1) or f(x*2,y,n+1) or f(x,y+1,n+1) or f(x,y*2,n+1)
for s in range (1,70):
	if f(7,s,0): print (s)
'''
#20
'''
def f(x,y,n):
	if n==3 and x+y>=77: return True
	elif n<3 and  x+y>=77: return False
	elif n==3 and x+y<77: return False
	else:
		if n %2 ==0: #Пети
			return f(x+1,y,n+1) or f(x*2,y,n+1) or f(x,y+1,n+1) or f(x,y*2,n+1)
		else:
			return f(x+1,y,n+1) and f(x*2,y,n+1) and f(x,y+1,n+1) and f(x,y*2,n+1)
for s in range (1,70):
	if f(7,s,0): print (s)
'''
#21
'''
def f(x,y,n):
	if (n==2 or n==4) and x+y>=77: return True
	elif n%2==1 and  x+y>=77: return False
	elif n==4 and x+y<77: return False
	else:
		if n %2 ==1: #Васи
			return f(x+1,y,n+1) or f(x*2,y,n+1) or f(x,y+1,n+1) or f(x,y*2,n+1)
		else:
			return f(x+1,y,n+1) and f(x*2,y,n+1) and f(x,y+1,n+1) and f(x,y*2,n+1)
def f1(x,y,n):
	if n==2 and x+y>=77: return True
	elif n<2 and  x+y>=77: return False
	elif n==2 and x+y<77: return False
	else:
		if n %2 ==1: #Васи
			return f1(x+1,y,n+1) or f1(x*2,y,n+1) or f1(x,y+1,n+1) or f1(x,y*2,n+1)
		else:
			return f1(x+1,y,n+1) and f1(x*2,y,n+1) and f1(x,y+1,n+1) and f1(x,y*2,n+1)

for s in range (1,70):
	if f(7,s,0) and not f1(7,s,0): print (s)

'''
#24
'''
f=open('C:\\Новая папка\\10.05.22\\24\\24-01.txt')
s=f.readline()

c=0
m=0
ch=[0]
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        c+=1
        if c>m:
            m,ch =c,s[i]
    else:    
        c=1
print(ch,m)
'''
#ЮРА
'''
kolvo=0
for chislo in range	(1,109,2): #перебор чисел от 1 до 108 с шагом +2(т.к.4,6,8 и тд чёт,'запомним 2')
	schetchik=0 #считает количество делителей

	for delitel in range(2,chislo+1): #перебор делителей от 2 до 108
		if chislo%delitel==0: #проверка
			schetchik+=1

	if schetchik==1:	#простое число, которое делится на 1 и на себя(==1, т.к. в переборе с 2)
		kolvo +=1		#считаю колличество чисел (тут можно их вывести, помня про 2)

print(kolvo+1) #не забываю про 2, поэтому +1

#Ответ: 28
'''

#Ботаю дома

#27
'''
with open('C:\\Новая папка\\Информатика\\07_06\\27.txt') as f:
	s = [int(x) for x in f]

mins=100000
for q in range(0,len(s)-1):
	for w in range(0,len(s)-1):
		for e in range(0,len(s)-1):
			for r in range(0,len(s)-1):				
				if (s[q]+s[w]+s[e]+s[r])%4==0 and mins>(s[q]+s[w]+s[e]+s[r]) and q!=w and q!=e and q!=r and w!=e and w!=r and e!=r:
					mins= (s[q]+s[w]+s[e]+s[r])
					print(mins, s[q], s[w], s[e], s[r])
'''
'''
#24
f = open('C:\\Новая папка\\Информатика\\14.06\\24.txt')
s=f.readline()
k=0
for i in range(0,len(s)-1):
	if (s[i]=='X' and s[i+1]=='Y' and s[i+2]=='Z') or (s[i]=='X' and s[i+1]=='Z' and s[i+2]=='Y') or (s[i]=='Y' and s[i+1]=='X' and s[i+2]=='Z') or (s[i]=='Y' and s[i+1]=='Z' and s[i+2]=='X') or (s[i]=='Z' and s[i+1]=='Y' and s[i+2]=='X') or (s[i]=='Z' and s[i+1]=='X' and s[i+2]=='Y'):
		k+=1
print(k)
'''
#25
'''
for a in range(110203,110246):
	s=[]
	print(s)
	for b in range(2,a,2):
		if a%b==0:
			s.append(b)

		if len(s)==4:
			print(s,a)
	
'''
#HOME
#24
'''
s=open('C:\\Users\\Ivan\\Desktop\\24.txt').readline()
s=s.replace('PR', 'P R').replace('RP', 'R P')
print(s)
print(max(map(len, s.split())))
'''
'''
f=open('C:\\Users\\Ivan\\Desktop\\27.2.txt')
s=[int(x) for x in f]
l=[]
k=0
for i in range(0, len(s)):
	l.append(s[i])
	if len(l)<=20:
		if sum(l)%39==0:
			continue
		if sum(l)%39!=0:
			if len(l)==1:
				l=[]
			else:
				k+=1
				print(sum(l),l[len(l)-1])
				l=[]
print(k)
'''
'''
def f(x,y,n):
	if n==2 and x*y>=63: return True
	elif n<2 and  x*y>=63: return False
	elif n==2 and x*y<63: return False
	else:
		return f(x+1,y,n+1) or f(x*2,y,n+1) or f(x,y+1,n+1) or f(x,y*2,n+1)
for s in range (1,32):
	if f(2,s,0): print (s)
'''
