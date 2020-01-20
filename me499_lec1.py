#!/usr/bin.env python3
print('Hello, World!')

#Print squares of numbers form 0 to 5
for i in range(6):
    s = i*i
    print(i,s)

a = [7,8,12,19,4]
#b = sort(a)
#print(b)

print(sum(list(range(1,366))))
print(list(range(1,366))[-1])

for n in range(1,100):
    print('{0}:{1}'.format(n,sum(range(n,365+n))))

