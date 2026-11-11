# l = "listen"
# n = "silent"

# def is_anagram(l, n):

#     if len(l) == len(n):

#         a = sorted(l)
#         b = sorted(n)

#         return a == b

#     else:
#         return False


# if is_anagram(l, n):
#     print("They are Anagrams")
# else:
#     print("They are not Anagrams")


# l = "listen"
# n = "silent"

# if len(l) == len(n):

#     a = sorted(l)
#     b = sorted(n)

#     if a == b:
#         print("They are Anagrams")
#     else:
#         print("They are not Anagrams")

# else:
#     print("They are not Anagrams")



# def is_anagram(a, b):

#     if len(a) != len(b):
#         return False

#     s = sorted(a)
#     t = sorted(b)

#     return s == t

# # Test cases
# print(is_anagram("eat", "tea"))
# print(is_anagram("listen", "silent"))
# print(is_anagram("hello", "world"))
# print(is_anagram("race", "care"))

# ---------------METHOD 1--------------
a = "listen"
b= "silentt"

def check_anag(a,b):
    if len(a) == len(b):

        l = sorted(a)
        n = sorted(b)

        if l == n:
            print("they are anagram")
        else:
            print("they are not anagram")
    else:
        print("they are not anagram")

check_anag(a,b)

#-----------MTHEOD 2-------------
c = "eat"
d = "tea"

def check(c,d):
    if len(c) != len(d):
        return False

    o = sorted(c)
    p = sorted(d)

    return o == p 

if check(c,d):
    print("they are anagram")
else:
    print("they are not anagram")

#-----------METHOD 3 -------------
e = "race"
f = "care"

def check1(e,f):

    if len(e) != len(f):
        return False

    q = sorted(e)
    r = sorted(f)

    return q == r

if check1(e,f):
    print("they are anagram")
else:
    print("they are not anagram")

check(e,f)

#-----------METHOD 4-------------
aa = str(input("Enter a word: "))
bb= str(input("enter a 2nd word: "))

def check2(aa,bb):
    if len(aa) == len(bb):

        ac = sorted(aa)
        ad = sorted(bb)

        return ac == ad
    else:
        return False
if check2(aa,bb):
    print("They are Anagram")
else:
    print("They are not Anagram")
