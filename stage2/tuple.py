def powersum(power, *args):
    # '''Return the sum of each argument raised to the specified power.'''
    total = 0
    print power , "in def"
    print args , "in def"
    for i in args:
        total += pow(i, power)
    return total

print powersum(2, 3, 4)
# 25
print powersum(2, 10)
# 100
