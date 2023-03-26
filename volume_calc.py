length = float(input("가로의 길이:"))
width = float(input("세로의 길이:"))
height = float(input("높이의 길이:"))
volume = length * width * height
weight = float(input("택배의 무게:"))
print("박스의 부피는",volume,"cm^3입니다.", sep=" ")

if ((length > 120) or (width > 120) or (height > 120) or (weight > 25)):
    fee = 12000
elif ((length > 100) or (width > 100) or (height > 100) or (weight > 15)):
    fee = 9000
elif ((length > 80) or (width > 80) or (height > 80) or (weight > 5)):
    fee = 6000
else:
    fee = 3000
print("요금은",fee,"입니다.",sep=" ")
