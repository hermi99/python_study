# import my_work.ping_test as ping_test
from my_work.ping_test import do_ping_test

if __name__ == '__main__':

    # 1. import로 사용시는 import한 이름에 .을 찍어서 사용
    # ping_test.do_ping_test("168.126.63.1")

    # 2. from xxx import yyy
    # yyy에 있는 모든것을 현재에 로딩한다.
    do_ping_test("168.126.63.1")




