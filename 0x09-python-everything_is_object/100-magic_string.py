#!/usr/bin/python3
def magic_string(lst=[]):
    lst.insert(len(lst) - 1, 'BestSchool')
    return ', '.join(lst)
