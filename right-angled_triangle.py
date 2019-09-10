# 세 변의 길이가 모두 자연수 {a.b,c}인 직각삼각형의 둘레를 p로 둘 때, p=120을 만족하는 직각삼각형은 아래와 같이 세 가지다.
# {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# 1000이하의 둘레 p에 대해서, 직각삼각형이 가장 많이 만들어지는 p의 값은 얼마인가?

# Let the perimeter of a right-angled triangle as 'p' which each three legs are integer {a, b, c}.
# For instance, with p = 120, there are three right-angled triangles can be made as follow : {20, 48, 52}, {24, 45, 51}, {30, 40, 50}
# Find 'p' which makes the most number of right-angled triangles when 'p' is smaller than 1000

import time
import math

class Right_angled_triangle:
    def __init__(self, max_perimeter):
        self.p = 0
        self.old_idx = 0
        self.get_p(max_perimeter)

    def get_p(self, max_perimeter) :
        for x in range(1, max_perimeter + 1):   # a leg should be larger than 1
            idx = 0
            for a in range(1, max_perimeter + 1) :
                skip = 5    # skip some numbers to make the loop faster

                isFirst = True
                for fake_b in range(a+1, max_perimeter + 1, skip) : # fake_b helps me omit another 1000 loop for c
                    pythagoras = a ** 2 + fake_b ** 2
                    c = math.sqrt(pythagoras)

                    if a + fake_b + c > x and not isFirst:
                        for b in range(fake_b - skip, fake_b) :
                            pythagoras = a ** 2 + b ** 2
                            c = math.sqrt(pythagoras)

                            if a + b + c == x :
                                idx += 1
                                break
                        break   # if the code is here, if means fake_b is big enough but does not satisfies the rule.
                                # so no need to loop fo fake_b anymore
                    elif a + fake_b + c == x:
                        idx += 1
                        break
                    isFirst = False
            self.isMost(x, idx)

    def isMost(self, x, idx):
        if self.old_idx < idx :
            self.old_idx = idx
            self.p = x
            print('{} : {}개'.format(self.p, self.old_idx))

if __name__ == "__main__":
    start_time = time.time()

    Right_angled_triangle(1000)

    finished_time = time.time()
    duration = finished_time - start_time
    print(duration)