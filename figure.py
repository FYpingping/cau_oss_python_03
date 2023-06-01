# %% figure_main에 쓰일 figure 모듈

# import keyword를 통해 math함수를 쓰기 위한 math 모듈을 부른다.
import math



class line:
    """
    높이, 너비 객체 생성 위한 클래스 정의
    외부에서 접근 불가능한 변수 width와 height을 선언했고
    이를 통해 getter, setter 메소드를 정의
    """

    __width = 0
    __height = 0
    
    # 생성자 초기화 메소드. 값을 받아 __height, __width 변수에 저장
    # width는 가로의 길이, height는 세로의 길이
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    # 인자로 받은 값을 width, height 변수에 저장하는 메소드
    def set_length(self, width, height):
        self.__width = width
        self.__height = height

    # 외부에서 width와 height 값을 알 수 있도록 반환해주는 메소드
    def get_length(self):
        return self.__width, self.__height      #너비와 높이 값 반환

# 인자로 받은 너비와 높이 값을 통해 직사각형의 넓이를 구하는 함수
def area_rectangle(width, height):
    valueErrorReport(width, height)             #너비와 높이 값이 0이하면 ValueError에 대한 예외처리
    return width*height                         # 직사각형의 넓이 int or float 값 반환

# 인자로 받은 타원의 가로와 세로의 길이을 통해 타원의 넓이를 구하는 함수
def area_eclipse(width, height):
    valueErrorReport(width, height)             #가로와 세로 값이 0이하면 ValueError에 대한 예외처리
    return width*height*math.pi                 #타원의 넓이 int or float값 반환

# 인자로 받은 직각삼각형의 가로와 세로의 길이를 통해 직각삼각형의 넓이를 구하는 함수
def area_right_triangle(width, height):
    valueErrorReport                            #가로와 세로 값이 0이하면 ValueError에 대한 예외처리
    return width*height/2                       #직각삼각형의 넓이 int or float 값 반환

# 인자로 받은 width와 height 값이 0이하라면 ValueError에 대한 예외처리를 하는 메소드
def valueErrorReport(width, height):
    if(width<=0 | height <= 0):
        raise ValueError
# %%
