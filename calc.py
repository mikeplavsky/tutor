# -*- coding: utf-8 -*-
import sys

if sys.argv.count == 1: 
  name = raw_input("Как тебя зовут?\n")
else:
  name = sys.argv[1]

print("\nПривет, %s!" % name)
print("Давай поиграем!\n")

points = 0

while (True):
  
  from random import random, choice
  import math

  digit = lambda: math.floor(random() * 20)

  x = digit()
  y = digit()

  op = choice(['+', '-'])

  if op == '-' and y > x:

    t = x
    x = y
    y = t

  q = "%i %s %i" % (x,op,y)

  while (True):

    res = raw_input("Сколько будет %s = ?\n" % q)

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



