def mcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)  # para que el resultado sea positivo

def mcd_four(a,b,c,d):
	return mcd(mcd(a, b), mcd(c, d))
