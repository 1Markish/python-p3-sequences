#!/usr/bin/env python3
lenth= 10

def print_fibonacci(length):
      if length == 0 :
          print([])
      elif length == 1 :
          print([0])
      elif length == 2 :
          print([0,1])
      else :
          s=print_fibonacci(length - 1 )
          s.append(s[-1] + s[-2]) ;   print(s)  