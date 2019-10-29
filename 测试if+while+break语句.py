print ("测试if + while + break语句")
test = input ("请输入“1”:  ")
print (test)
while test != ("1"):
  test = input ("请输入“1”:  ")
  if test == ("1"):
    print("对")
    break 
  else:
    print ("不对")
print("测试结束")
   
