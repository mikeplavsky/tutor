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
  
  import random
  import math

  digit = lambda: math.floor(random.random() * 10)

  x = digit()
  y = digit()

  while (True):

    res = raw_input("Сколько будет %i + %i = ?\n" % (x, y))

    import os
    os.system('clear')

    if (int(res) == (x + y)):

      points += 1

      print( "\nМолодец, %s! Правильно!" % name )
      print( "Ты заработал %i" % points )
      print( "\n%s, давай ещё поиграем!\n" % name )

      break

    else:

      print( "\nНеправильно!" )
      print( "%s, попробуй ещё раз! \n" % name )
      continue



