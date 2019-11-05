print("012列表内列表换元素")
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1.insert(1,[1,2,['小鱿鱼']])
del list1[2]
for  number in list1:
  print(number)
print("-------------------------------分割线-------------------------------")  

print("数列求奇数偶数")  
list1 = []
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                list1.append((x, y))
print(list1)               
