from os_code import *

class OSFactory:
    def build_os(os_type):
        if os_type == 'Android':
            return Android()
        if os_type == 'IOS':
            return IOS()

if __name__ == '__main__':
    res = input('Enter the OS type (Android / IOS): ')
    os = OSFactory.build_os(res)
    os.specs()