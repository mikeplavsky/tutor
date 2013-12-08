# -*- coding: utf-8 -*-

print "Привет, Матвей!"
print "Давай поиграем!"

points = 0

while (True):
  
  import random
  import math

  x = math.floor(random.random() * 10)
  y = math.floor(random.random() * 10)

  while (True):

    res = raw_input("Сколько будет %i + %i = ?\n" % (x, y))

    if (int(res) == (x + y)):

      points += 1

      print( "Молодец, Матвей! Правильно!" )
      print( "Ты заработал %i! \n" % points )

      break

    else:

      print( "\nНеправильно!" )
      print( "Матвеюшка! Попробуй ещё раз! \n" )
      continue



