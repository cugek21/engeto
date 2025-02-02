import sys

def je_os_windows():
    return sys.platform.startswith('win')

print(je_os_windows())