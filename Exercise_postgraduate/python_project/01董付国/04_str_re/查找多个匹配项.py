"""
findall
finditer
"""

import re


text = "草莓君 草莓君"
pattern = r"草莓君"

print(a:=re.findall(pattern, text), type(a[0]))     # List[str]


for obj in re.finditer(pattern, text):
    print(type(obj), obj.group())       # <class 're.Match'> 草莓君