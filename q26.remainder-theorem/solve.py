#!python3

# x = r1 mod n1
# x = r2 mod n2
# -> x = r + n k
# -> r2-r1 = n1*k1 - n2*k2
r1 = 32134
n1 = 1584891

r2 = 193127
n2 = 3438478

def exgcd(a, b):
	if b == 0:
		return (a, 1, 0)
	(u, v, w) = exgcd(b, a % b)
	return (u, w, v - a // b * w)

# a*n1 + b*n2 = 1
(gcd, a, b) = exgcd(n1, n2)

print(gcd, a, b)
print(a*n1 + b*n2 == gcd)

# ((r1-r2)*a*n1 + (r1-r2)*b*n2) = r1-r2
k1 = +(r2 - r1) * a
k2 = -(r2 - r1) * b

print(r2-r1 == n1*k1 - n2*k2)
print(n1*k1 + r1)
print(n2*k2 + r2)

x = (n1*k1 + r1) % (n1*n2)
print(x)
x = (n2*k2 + r2) % (n1*n2)
print(x)
