#-------------------------------------------------------------------------------
# Name: Default Arguments       module1
# Purpose: In this challange, the task is to debug the existing code to
# successfully execute all provided test file. Debug the given function:
# print_from_stream using the default value of one ot this arguments.
# This function should print the first n values returned by get_next() method of
# stream object  provided as an argument. Each of these values should be printed
# in a separate line. Whenever the function is called without the stream
# argument, it should use an instance of EvenStream class defined in the code
# stubs below as the value of stream.
# Your function will be tested on several cases by the locked template code.
# Input Format: The input is read by the provided locked code template. In the
# first line, there is a single integer q denoting the number of queries. Each
# of the following q  lines contains a stream_name followed by integer n, and
# it corresponds to a single test for your function.
# Constraints 1<=q<=100   1<=n<=10
# Output Format: The output is produced by the provided and locked code
# template. For each of the queries (stream_name, n), if the stream_name is
# even then print_from_stream(n) is called. Otherwise, if the stream_name is
# odd, then print_from_stream(n, OddStream()) is called.
#
#
# Author:      tioFer
#
# Created:     23/04/2022
# Copyright:   (c) tioFer 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


# Due is used an Object like default argument for variable called stream,
# Object EvenStream() is used like default argument, in python default
# arguments values are initialized once when is defined, not every time that
# function is invoke. In this code The initial configutation has the
# EvenStream() object like default parameter so if multiple call of
# print_from_stream(n,stream) are made the late call will use the same
# object and pick up the stream value parameter where the previus call finished.
# To solve this bug only use stream.__init__() to reset the value of
# stream argument.

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()  # reset the class variable stream every time is invoke
    for _ in range(n):
        print(stream.get_next())

queries = int(input())
# The print func,in the next 3 lines is no required is used for improve output
print(36*"*")
print(12*' ' + 'ouput:' + 12*' ')
print('')
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
