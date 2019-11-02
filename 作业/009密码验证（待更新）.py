print("密码验证程序")
password = input("请输入密码")
i = 3
def pas():
  global password
  global i
  if password == "truepassword":
      print("密码正确，进入程序.....")
  else:
      for p in password:
          print(p)
          if p == "*":
              i = str(i)
              print("密码中不能包含\"*\"号!您还有"+i+"次机会")
              i = int(i)
              password = input("请输入密码")
              pas()
          else:
              i -= 1
              i = str(i)
              print("密码错误!您还有"+i+"次机会")
              i = int(i)
              password = input("请输入密码")
              pas()
             
pas()
    
