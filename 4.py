
def isSixDigit(n: int) -> bool:
    return len(str(n)) == 6


def isIncreasing(n: int) -> bool:
    num = str(n)
    prev = num[0]
    for i in range(1, len(num)):
        if str(n)[i] < prev:
            return False
        prev = num[i]
    return True


def hasSingleDoubleDigits(n: int) -> bool:
    num = str(n)
    count = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
             '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    for i in range(len(num)):
        count[num[i]] += 1
    if max(count.values()) >= 2:
        # if sorted(count.values(), reverse=True).count(6) == 1:
        #     return True
        if sorted(count.values(), reverse=True).count(2) >= 1:
            return True
    return False


def checkAttributes(n: int) -> bool:
    if not isIncreasing(n):
        return False
    if not isSixDigit(n):
        return False
    if not hasSingleDoubleDigits(n):
        return False
    return True


assert checkAttributes(123789) == False
assert checkAttributes(223450) == False
# assert checkAttributes(111111) == True
assert checkAttributes(112233) == True
assert checkAttributes(123444) == False
assert checkAttributes(111122) == True

count = 0
for i in range(193651, 649729):
    ans = checkAttributes(i)
    if ans:
        count += 1

print(count)
