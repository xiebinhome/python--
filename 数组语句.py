print ("for循环语句+len计算长度+range递增")
number = ['第一','第二','第三“字数”','第四','第五']
for  test in number:
  print(test,len(test))
  
print("------------------------分割线------------------------")

print ("range递增，从1到19，递增2")
  
for i in range(1,20,2):
    print(i)
    
print("------------------------分割线------------------------")

print("append增加第六：")
number = ['第一','第二','第三“字数”','第四','第五']
number.append("增加的第六")
for  test in number:
  print(test,len(test))
print("extend增加第七和第八：")
number.extend(["第七","可以增加多个数的第八"])
for test in number:
  print(test,len(test))
  
print("------------------------分割线------------------------")
print("insert调换位置")
number = ['第一','第二','第三“字数”','第四','第五']
number.insert(0,"调换位置的第六")

for test in number:
  print(test,len(test))
  
print("------------------------分割线------------------------")

print ("remove删除第五：")
number = ['第一','第二','第三“字数”','第四','第五']
number.remove("第五")
for  test in number:
  print(test,len(test))
print ("del删除第二：")
del number[1]
for  test in number:
  print(test,len(test))
print ("pop删除第四：")
number.pop()
for  test in number:
  print(test,len(test))

print("------------------------分割线------------------------")
print ("count查看成员出现次数：")
number = ['第一','第二','第三“字数”','第四','第五']
number *= 4
time = number.count("第四")
for  test in number:
  print(test,len(test))
time = str(time)
print("第四出现了"+ time +"次" )

print ("index查看成员第一次出现的位置：")
number = ['第一','第二','第三“字数”','第四','第五']
number *= 4
location = number.index("第四")
for  test in number:
  print(test,len(test))
location = str(location)
print("第四第一次出现在第"+ location +"个" )

print ("reverse颠倒顺序：")
number.reverse()
for  test in number:
  print(test,len(test))
  
print("------------------------分割线------------------------")

list1 = [1,5,3,95,22,54]
for  test1 in list1:
  print(test1)
print("sort按顺序排列")
list1.sort()
for  test1 in list1:
  print(test1)

print("sort按相反顺序排列")
list1.sort(reverse=True)

for  test1 in list1:
  print(test1)



