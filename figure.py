# %% figure_main에 쓰일 figure 모듈

# import keyword를 통해 math함수를 쓰기 위한 math 모듈을 부른다.
import math


# 선에 대한 객체 생성 위한 클래스 정의
class line:
    __length = 0
    
    # 생성자 초기화 메소드. 값을 받아 __length 변수에 저장
    def __init__(self, length):
        self.__length = length
    
    # 인자로 받은 값을 __length 변수에 저장하는 메소드
    def set_length(self, length):
        self.__length = length

    # __length 값을 반환받는 메소드
    def get_length(self):
        return self.__length

# 인자로 받은 정사각형의 길이를 통해 정사각형의 넓이를 구하는 함수
def area_square(length):
    return length**2

# 인자로 받은 원의 반지름의 길이을 통해 원의 넓이를 구하는 함수
def area_circle(length):
    return length**2*math.pi

# 인자로 받은 정삼각형의 한 변의 길이를 통해 정삼각형의 넓이를 구하는 함수
def area_regular_triangle(length):
    return length**2*math.sqrt(3)/4