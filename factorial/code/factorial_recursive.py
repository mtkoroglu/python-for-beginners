def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fac(n-1)
x = int(input('Enter a number: '))
while x < 0:
    x = int(input('You cannot enter a negative number. Enter a number again: '))
print('%i! = %i' %(x, fac(x)))