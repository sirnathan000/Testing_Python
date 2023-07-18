#codes
# d  = decimal integer
# b = binary interger
# x = hexadecimal interger
# f = float as [-]m.dddddd
# e = float as [-]m.dddddd+-xx
# g = float, but selective use of E notation
# s = stirng
# c = Character


name = 'IBM'
shares = 100
price = 91.1
headers = ('name', 'shares', 'price', 'change')

##output is
#      name     shares      price     change
#      ----     ------      -----     ------ 
#        IBM        100      91.10
#       IBM        100      91.10
#       IBM        100      91.10

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}' )
for header in headers:
	print(f'{"-"*len(header):>10s}', end= " " )
print('\n', f'{name:>10s} {shares:>10d} {price:>10.2f}')
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')


print('\n \n \n')


##output is
#      name     shares      price     change
#---------- ---------- ---------- ---------- 
#       IBM        100      91.10
#       IBM        100      91.10
#       IBM        100      91.10

print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')



print(' \n\n\n\n\n')

#output is
#name		shares
#----		------
#IBM		100


print(f'{headers[0]}\t\t{headers[1]}')
print(f'{"-"*len(headers[0])}\t\t{"-"*len(headers[1])}')
print(f'{name}\t\t{shares}')
