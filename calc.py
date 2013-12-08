# -*- coding: utf-8 -*-
from optparse import OptionParser
parser = OptionParser()

parser.add_option("-n", "--name", dest="name", help="player's name")
parser.add_option("-m", "--max", dest="max", type="int", help="upper bound")

(options,args) = parser.parse_args()

if not options.name or not options.max:
  parser.print_help()
  exit(-1)

name = options.name

print("\nПривет, %s!" % name)
print("Давай поиграем!\n")

points = 0

while (True):
  
  from random import random, choice
  import math

  op = choice(['+', '-'])
  max = options.max

  if op == '+':
    max = max / 2

  digit = lambda: math.floor(random() * max)

  x = digit()
  y = digit()

  if op == '-' and y > x:

    t = x
    x = y
    y = t

  q = "%i %s %i" % (x,op,y)

  while (True):

    res = raw_input("Сколько будет %s = ?\n" % q)

    try:

      res = int(res)

    except ValueError:

      print("%s, надо ввести цифру!\n") % name
      continue

    import os
    os.system('clear')

    if (int(res) == eval(q)):

      points += 1

      print( "\nМолодец, %s! Правильно!" % name )
      print( "Ты заработал %i" % points )
      print( "\n%s, давай ещё поиграем!\n" % name )

      break

    else:

      print( "\nНеправильно!" )
      print( "%s, попробуй ещё раз! \n" % name )
      continue



