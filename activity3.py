#take marks as input
print("enter marks in 4 subjects:")
math = int(input("maths:"))
english = int(input("english:"))
science = int(input("science:"))
hindi = int(input("hindi:"))

#calculate the %
sum = math+english+hindi+science
print("sum is:", sum)
per = (sum/400)*100
print("% is:", per)