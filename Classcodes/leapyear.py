yr=int(input("enter year"))
if yr%400==0 or((yr%100!=0) and (yr%4==0)):
       print("yes leap year")
else:
    print("not a leap year")
