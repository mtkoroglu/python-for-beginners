def fac(n):
    if n == 0:
        return 1
    else:
        product = 1
        while n > 0:
            product = n*product
            n = n-1
        return product
x = int(input('Enter a number: '))
while x < 0:
    x = int(input('You cannot enter a negative number. Enter a number again: '))
print('%i! = %i' %(x, fac(x)))