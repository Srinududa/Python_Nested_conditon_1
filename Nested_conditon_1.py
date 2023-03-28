a=10
b=3
x= a % b
print(x)


Result==>>1


N=35
if (N % 7) == 0:
    print("Divisible by Seven")
else:
    print("Not Divisible by Seven")
# Result==>>Divisible by Seven


a = 5
b = 2

Q, R = divmod(a, b)

print(Q)
print(R)
Result==>>2
Result==>>1

N=4
Z = N % 2 == 0
if Z:
    print("Even")
else:
    print('Odd')
Result==>>Even


N=12
A =int(N%4)
B =int(N%5)
if (A>B):
    print(A)
else:
    print(B)
Result==>>Even


D=3
S = D<=10
F = D>10
z = 10+(D-10)*3
if S:
    print(D)
else:
    print(z)
 Result==>>3


a=4
z=(a**3)
print(z)
Result==>>64


a=4
import math
s=math.sqrt(a)
print(s)
Result==>>2.0



a=10
b=2
sum_a_and_b=a**2+b**2
if sum_a_and_b>=60:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")
Result==>>Greater than or Equal to 60


a=15
squ=a**2
str_a=str(a)
last_dig_a=str_a[-1:]
str_squ=str(squ)
last_dig_squ=str_squ[-1:]
z=last_dig_a==last_dig_squ
if z:
    print("Equal")
else:
    print("Not Equal")
Result==>>Equal

a=6
g=a*3
h=g % 6 == 0
if h:
    print(g)
else:
    print(a)
Result==>>18


a=3
b=a*3
c=a*2
g=a%3==0
if g:
    print(b)
else:
    print(c)
Result==>>9



a=9
g=a%5==0
h=a%7==0
r=a%5
i=a%7
j=a<7
if (g and h) or j:
    print(a)
else:
    print(r)
    print(i)
Result==>>4
Result==>>2



a=64
b=8
import math
g=math.sqrt(a)
j=g==b
if j:
    print("Square root of A is equal to B")
else:
    print("Square root of A is not equal to B")


 Result==>>   Square root of A is equal to B




a=1634
str_a=str(a)
first_a=str_a[0]
second_a=str_a[1]
third_a=str_a[2]
fourth_a=str_a[3]
int_first_a=(int(first_a)**4)
int_second_a=(int(second_a)**4)
int_third_a=(int(third_a)**4)
int_fourth_a=(int(fourth_a)**4)
sum_all= (int_first_a + int_second_a + int_third_a + int_fourth_a)
if sum_all == a:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


Result==>>  Armstrong Number



N = 1329
years = N//365
remain_1 = N%365
weeks = remain_1//7
remain_2 = remain_1%7
days = remain_2
print(years)
print(weeks)
print(days)

Result==>> 
3
33
3




