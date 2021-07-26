#
# def decorator(func):
#     def decorated():
#         print('func start!')
#         func()
#         print('func end!')
#
#     return decorated
#
# @decorator
# def hello_world():
#     # print('func start!')
#     print('hahaha')
#     # print('func end!')
#
# hello_world()

########################################
# def check_val_deco(func):
#     def decorated(h, w):
#         if h > 0 and w > 0:
#             return func(h, w)
#         else:
#             raise ValueError('Input value is not available')
#     return decorated
#
# @check_val_deco
# def cal_tri(h, w):
#     res = (h * w) / 2
#     return print(res)
#
# @check_val_deco
# def cal_rect(h, w):
#     res = h * w
#     return print(res)
#
# h = int(input('height (integer only) : '))
# w = int(input('width (integer only) : '))
#
# cal_tri(h, w)

#######
"""
User class작성,
user class 내 is_authenticated 변수 작성
User 객체를 넓이 함수인자로 전달
is_authenticated 변수 확인후 True가 아닐경우 Error 발생
"""
class User:
    def __init__(self, auth):
        self.is_authenticated = auth

user = User(auth=False)

def cal_rect(h, w):
    res = h * w
    return print(res)