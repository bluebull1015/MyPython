
#range는 정수만 다룬다.
total = 0
for i in range(1,11): #range(from 0베이스, to, step 1베이스)
    total += i
# end for 권장사항
print('총합01 : %d' % (total))

total = 0
for i in range(1,101, 3): #range(from 0베이스, to, step 1베이스)
    total += i
# end for 권장사항
print('총합01 : %d' % (total))

total = 0
for i in range(97, 1, -5): #range(from 0베이스, to, step 1베이스)
    total += i
# end for 권장사항
print('총합01 : %d' % (total))

total = 0
for i in range(1, 97, 5): #range(from 0베이스, to, step 1베이스)
    total += i**2 #i의 제곱
# end for 권장사항
print('총합01 : %d' % (total))

total = 0
for i in range(1, 6): #range(from 0베이스, to, step 1베이스)
    total += i*(i+1)
# end for 권장사항
print('총합01 : %d' % (total))
