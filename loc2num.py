import string
import re

def loc2num(loc):
  """
  Recieves: loc, a string representing a library of congress classification
  Returns: a float uniquely identifying the loc
  """

def base36encode(decnum):
  """encodes a decimal number in hexatridecimal"""
  numerals = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  result = ''
  while decnum:
    result = numerals[decnum % 36] + result
    decnum /= 36
  return result

int(base36encode(101234235235),36)

def cutter(numstring):
  """
  normalizes Cutter numbers.
  For our purposes, a Cutter number is a letter followed by up to four digits
  Note that in LCC they are assumed to be fractional so .L15 < .L2
  Therefore we will return L1500 (which is less than than L2000)
  The input could also be a year, so if we get something that is not a cutter
  number already, we just return it
  """
  if re.match('[A-Z][0-9]{0,4}', numstring):
    num = numstring[1:]
    num += '0'*(4-len(num))
    numstring = numstring[0] + num
  return numstring

def normalize(LCCstring):
  """
  normalizes call numbers following the Library of Congress Classification syntax
  so they can be sorted in lexical (ascii) order
  """
  result = ''

  elements = re.findall('(^[A-Z]{1,3}|[A-Z][0-9]{1,4}|[A-Z]{1,3}|[0-9]{1,4}[.]?[0-9]{0,2}|[0-9]{4})',LCCstring)
  print elements
  # handle the alphabetical prefix
  subclass = elements[0]
  subclass += '@'*(3-len(subclass))
  result += subclass

  # handle the number following the prefix which can range from 1-9999.99
  num = elements[1]
  result += "%06d" % (float(num)*100) # make it a whole number and pad it with leading zeroes
  for element in elements[2:]:
    result += cutter(element)
  return result


def sortLCC(lcclist):
  """sort a list of LCCs"""
  return sorted(map(normalize, lcclist))

sortLCC(['Q223 .F73 2012','Q324 .L48 2012','QA76.89 .B76 2000','QA7 .W43 2012'])