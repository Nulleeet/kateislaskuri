z = float(input("5snt kpl? "))
y = float(input("10snt kpl? "))
x = float(input("20snt kpl? "))
w = float(input("50snt kpl? "))
v = float(input("1eur kpl? "))
u = float(input("2eur kpl? "))
t = float(input("5eur kpl? "))
s = float(input("10eur kpl? "))
r = float(input("20eur kpl? "))
q = float(input("50eur kpl? "))
p = float(input("100eur kpl? "))
o = float(input("200eur kpl? "))
n = float(input("500eur kpl? "))
print(" " + " ") #random väli

snt5 = float(0.05*z)
snt10 = float(0.10*y)
snt20 = float(0.20*x)
snt50 = float(0.50*w)
eur1 = float(1.0*v)
eur2 = float(2.0*u)
eur5 = float(5.0*t)
eur10 = float(10.0*s)
eur20 = float(20.0*r)
eur50 = float(50.0*q)
eur100 = float(100.0*p)
eur200 = float(200.0*o)
eur500 = float(500.0*n)

print(f"5snt: {snt5}")
print(f"10snt: {snt10}")
print(f"20snt: {snt20}")
print(f"50snt: {snt50}")
print(f"1euro: {eur1}")
print(f"2euro: {eur2}")
print(f"5euro: {eur5}")
print(f"10euro: {eur10}")
print(f"20euro: {eur20}")
print(f"50euro: {eur50}")
print(f"100euro: {eur100}")
print(f"200euro: {eur200}")
print(f"500euro: {eur500}")
print(" " + " ") #random väli

yht = float(snt5+snt10+snt20+snt50+eur1+eur2+eur5+eur10+eur20+eur50+eur100+eur200+eur500)

print(f"Yhteensä: {yht}")
