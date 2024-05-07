# 1st Published: 7th May 2024

# Author  : InferiorAK
# Module  : IPv4 Validation
# Language: Python3

# This will validate an IPv4 address. It will return True if the IP is valid, otherwise False.
# You can use this function to validate an IP address before using it in your program.

# ```python

def validate(ipv4Address):
    dots = 0
    format_ = []
    num = 0
    for c in ipv4Address:
        if c == ".":
            if dots > 3 or 0 > num or 255 < num:
                return False
            dots += 1
            format_.append(".")
            num = 0
        elif c.isdigit():
            num = num * 10 + (ord(c) - ord("0"))
            format_.append("0")
        else:
            return False
    if dots != 3 or 0 > num or 255 < num:
        return False
    
    dot = "."
    index = [index for index, string in enumerate(format_) if string == dot]
    print(index)
    for i in range(len(index) - 1):
        diff = index[i + 1] - index[i]
        if diff == 1:
            return False
    return True

# ipv4Address = str(input("Input IP: "))
# ipv4Address = "125.1.1.1"
# if validate(ipv4Address):
#     print("YES")
# else:
#     print("NO")