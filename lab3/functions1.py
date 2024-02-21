from random import randint
import math
from itertools import permutations

def ounces(grams):
    return 28.3495231 * grams


def centigrade(f):
    return (5 / 9) * (f - 32)


def solve(numheads, numlegs):
    rabbits = (numlegs - numheads*2)//2
    chickens = numheads - rabbits
    return rabbits, chickens


def filter_prime(nums):
    a = []
    for i in nums:
        t = True
        for j in range(2, i):
            if i % j ==0:
                t = False
                break
        if t:
            a.append(i)
    return a

def perm(s):
    perms = [''.join(p) for p in permutations(s)]
    print(set(perms))

def rev_str(s):
    a = ""
    b = ""
    arr = []
    for i in range(len(s)):
        if s[i]==' ' or i==len(s)-1:
            b+=s[i]
            b = b.strip()
            arr.append(b)
            b=""
        else:
            b+=s[i]
    for i in range(len(arr)-1, -1, -1):
        a+=arr[i]
        a+=' '
    return a


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] and nums[i] == 3:
            return True
    return False


def spy_game(nums):
    for i in range(0, len(nums)-2):
        if nums[i]==0:
            for j in range(i+1, len(nums)-1):
                if nums[j]==0:
                    for k in range(j+1, len(nums)):
                        if nums[k]==7:
                            return True
    return False

def volume(radius):
    return math.pi * radius**3 * 4 /3


def unique(nums):
    a = []
    for i in nums:
        if i not in a:
            a.append(i)
    return a


def pal(st):
    if st == st[::-1]:
        print("YES")
        return
    print("NO")


def histogram(nums):
    for i in nums:
        print("*"*i)


def guess(number, name, i):
    print("Take a guess.")
    n = int(input())
    if n == number:
        i+=1
        print("Good job,", name+"! You guessed my number in", i, "guesses!")
    elif n < number:
        print()
        i+=1
        print("Your guess is too low.")
        guess(number, name, i)
    else:
        print()
        i += 1
        print("Your guess is too high.")
        guess(number, name, i)


def game():
    print("Hello! What is your name?")
    name = input()
    print("Well, "+name+", I am thinking of a number between 1 and 20.")
    rn = randint(1, 20)
    guess(rn, name, 0)