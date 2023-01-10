#!/usr/bin/python3
'''
Write a function that returns an object (Python data structure)
represented by a JSON string
'''
import json


def from_json_string(my_str):
    '''Function that gives the python object of
    a string JSON'''
    return json.loads(my_str)
