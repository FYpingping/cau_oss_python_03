# %% figure 모듈을 import하여 작성한 프로그램


# 프로그램 실행에 필요한 모듈 import
import figure

# 모듈을 통해 10을 인자로 하는 생성자 호출
myline = figure.line(10)

# 모듈 속 길이 변수를 getter를 통해 구하고 그것으로 정사각형의 넓이를 구한다
square = figure.area_square(myline.get_length())
print(square)

# 모듈 속 길이 변수를 setter를 통해 값을 저장하고 새로 저장된 길이를 토대로 정삼각형의 넓이를 구한다
myline.set_length(20)
regular_triangle = figure.area_regular_triangle(myline.get_length())
print(regular_triangle)


# 모듈속 길이 변수를 setter를 통해 값을 저장하고 새로 저장된 길이를 토대로 원의 넓이를 구한다
myline.set_length(30)
circle = figure.area_circle(myline.get_length())
print(circle)