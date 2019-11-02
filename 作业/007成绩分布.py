print("成绩分布")
score = input("请输入分数")
score = int(score)
if score >= 90:
    print("A")
else:
    if score < 90 and score >= 80:
        print("B")
    else:
        if score < 80 and score >= 60:
           print("C")
        else:
          if score < 60:
             print("D")
        
