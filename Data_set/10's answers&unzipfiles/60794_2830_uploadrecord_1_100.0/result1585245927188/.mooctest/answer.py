b, k = map(int, input().split())
a = list(map(int, input().split()))
c = len([0 for i in a if i % 2])
o = (b % 2 == 0 and a[-1] % 2) or (b % 2 and c % 2)
print('odd' if o else 'even')
