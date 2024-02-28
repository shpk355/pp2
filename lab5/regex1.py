import re

s = input()
def ex1(text):
    x = re.search("ab*", text)
    if x is None:
        return False
    return True
print(ex1(s))

def ex2(text):
    if re.search("abb", text) is None and re.search("abbb", text) is None:
        return False
    return True
print(ex2(s))

def ex3(text):
    x=re.findall("[a-z]_[a-z]", text)
    return x
print(ex3(s))

def ex4(text):
    x = re.findall("[a-z]+[A-Z]", text)
    return x
print(ex4(s))

def ex5(text):
    if re.search("a.", text) and re.search("b\Z", text):
        return True
    return False
print(ex5(s))

def ex6(text):
    x = re.sub("\s", ":", text)
    x = re.sub(",", ":", x)
    x = re.sub("[.]", ":", x)
    return x
print(ex6(s))

def ex7(text):
    return re.sub('_([a-z])', lambda x: x.group(1).upper(), text)
print(ex7(s))

def ex8(text):
    return re.sub('[a-z]', lambda x: x.group().upper(), text)
print(ex7(s))

def ex9(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
print(ex9(s))

def ex10(text):
    return re.sub(r'([a-z])([A-Z])', lambda x: x.group(1) + '_' + x.group(2).lower(), text)
print(ex10(s))