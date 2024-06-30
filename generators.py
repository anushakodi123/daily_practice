def generateSequence(n):
    count = 0
    while count < n:
        yield count
        count += 1


# print(generateSequence(3))

# next(generateSequence(3))
for i in generateSequence(3):
    print(i)


def infiniteSequence():
    count = 0
    while True:
        yield count
        count += 1

def is_palindrome(n):
    if n // 10 == 0:
        return False
    temp = n
    reverse = 0
    while temp!=0:
        reverse = reverse*10 + temp%10
        temp = temp // 10
    if reverse == n:
        return True
    else:
        return False
    
def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1

pal_gen = infinite_palindromes()
for i in pal_gen:
    digits = len(str(i))
    print(pal_gen.send(10 ** (digits)))