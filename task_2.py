a = [1, 2]
sum = 0
while a[-1] < 4000000:
    if a[-2] + a[-1] >= 4000000:
        break
    a.append(a[-2] + a[-1])
for i in range(len(a)):
    if a[i] % 2 == 0:
        sum += a[i]
print(sum)
