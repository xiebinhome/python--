print("求奇数不换行")
i = 0
while i <= 100:
    if i % 2 != 0:
        print(i, end=' ')
        i += 1
    else:
        i += 1
        
print("\n-----------------------分割线----------------------------------")

print("求奇数会换行")
range1 = range(100)
for number in range1:
    if number % 2 !=0:
         print(number)
