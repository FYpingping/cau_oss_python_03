# %%

"""
area_rectangle, area_right_triangle, area_ellipse 함수들에서
예외 발생 시 0이하의 값은 입력할 수 없습니다를 출력하도록 변경!
"""

import figure

#생성자를 통해 가로 10, 세로 20의 객체 myline을 생성
myline = figure.line(10, 20)
# 생성된 객체 myline의 가로, 세로 길이를 변수 width, height에 저장
width, height = myline.get_length()

# implement exception handler
try:
    #figure 모듈의 직사각형의 넓이를 구하는 메소드를 통해 직사각형의 넓이를 rectangle 변수에 저장하고 출력
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    #width, height에 저장된 값이 0 이하인 예외가 발생하면 메세지를 출력
    print("plese input positive number for width and height")




#객체에 저장된 가로, 세로 길이를 20, 30으로 변경
myline.set_length(20, 30)
#객체에 저장된 가로, 세로 길이를 변수 width, height에 저장
width, height = myline.get_length()

# implement exception handler
try:
    #figure 모듈의 직각삼각형의 넓이를 구하는 메소드를 통해 직각삼각형의 넓이를 triangle 변수에 저장하고 출력
    triangle = figure.area_right_triangle(width, height)
    print(triangle)
except ValueError:
    #width, height에 저장된 값이 0 이하인 예외가 발생하면 메세지를 출력
    print("plese input positive number for width and height")



#객체에 저장된 가로, 세로 길이를 30, 40으로 변경
myline.set_length(30, 40)
#객체에 저장된 가로, 세로 길이를 변수 width, height에 저장
width, height = myline.get_length()

# implement exception handler
try:
    #figure 모듈의 타원의 넓이를 구하는 메소드를 통해 타원의 넓이를 eclipse 변수에 저장하고 출력
    eclipse = figure.area_eclipse(width, height)
    print(eclipse)
except ValueError:
    #width, height에 저장된 값이 0이하인 예외가 발생하면 메세지를 출력
    print("plese input positive number for width and height")