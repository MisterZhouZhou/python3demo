#! /usr/bin/python3

import re

str = 'Anna is {age} years old,Bob is {age} years old too';
content = str.replace('/{.*}/g', '13')
print(content)