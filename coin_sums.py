'''
Coin sums
problem 31
'''
f = [1,1]

while len(str(f[-1])) != 1000:
    f.append(f[-1]+ f[-2])

print(len(f))
print(len(str(f[-1])))
