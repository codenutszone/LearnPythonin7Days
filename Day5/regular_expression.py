# raw string : to exclude the special meaning of escape character we user r or \ for raw string
import re

st = "sohan\rmohan"
print(st)
st = r"sohan\rmohan"
print(st)

st = "sohan\\rmohan"
print(st)

################## Compile regular expression #######################
import re

reg = 's\whan|m\whan'

prog = re.compile(reg)
st = input("Enter the string: ")
result = prog.search(st)
if result is not None:
    print(result.group())
else:
    print("no pattern matched")

result = re.search(prog, input("Enter the string: "))
if result is not None:
    print("The matched string is :", result.group())

# But search method give only first output , not all matched strings, for this we can use findall method. It gives the list
# of all matched strings
result = re.findall(prog, input("Enter the string: "))
if len(result) > 0:
    print("The matched string is :", result)
else:
    print("No match found")

# match method : matches only at the start of the string

result = re.match(prog, input("Enter the string: "))
if result is not None:
    print("matched string is :", result.group())
else:
    print("No match found at the start of the string")

# split method : splits the string into pieces

st = input("Enter the string: ")
result = re.split(r'\W+', st)
print(result)

# sub method : repalce string if matched with expression

st = input("Enter the string: ")
result = re.sub(r'sohan', 'sohan Dasharathji', st)
print(result)


# Sequence characters in regular expression
# \d - any digit 0-9
# \D - any non Digit
# \s - whitespaces \t\r\n\f\v
# \S - non-white space character
# \w - any alphanumeric
# \W - non alpha numeric
# \b - space around words
# \A - only at the start of the string
# \Z - only at the end of the string


def reg_check(prog):
    result = re.findall(prog, input("Enter the string: "))
    if len(result) > 0:
        print("The matched string is :", result)
    else:
        print("No match found")


prog = r"s[\w]*"
prog = r"\d[\w]*"
prog = r"\bs[\w]*\b"
prog = r"\b\w{5}\b"
prog = r"\b\w{4,}\b"
prog = r"\As\w*"
prog = r"\b\w+nd\Z"
prog = r"\w{4,}\D"
prog = r"[sm]\w+"
prog = r"\b\w+han$"
prog = r"^[sm]ohan\b"
prog = r"[^sm]\w.{3}\b"
reg_check(prog)


# read files and match regular expressions
def reg_check(prog, line):
    result = re.findall(prog, line)
    if len(result) > 0:
        lst.append(result)


f = open('C:/Users/sohan/PycharmProjects/LearnPythonin7Days/Day5/test.txt', 'r')
lst = []

for line in f:
    prog = r"L\w*"
    prog = r"\d{4,}"
    reg_check(prog, line)
print("The matched string is :", lst)
