import sys
import os


def prime(s):
    # your code goes here
    if s>1:
        for n in range(2,s):
            if (s%n)==0:
                return False
            else:
                return True
print(prime(11))
print(prime(7))                

def solution(s):
    return prime(3)
solution(3)
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))
    print(solution(sys.argv[1]))
