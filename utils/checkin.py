'''
Created on: 24 Sept 2024
Author: <Thinhdv>
Check an element in an array
'''


def exist(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return True
    return False
