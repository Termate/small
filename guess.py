#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

rn = random.randint(1, 101)
print ("\n-----------------------------------------------------------\n")
print ("давай поиграем! Я загадал число от 1 до 100, попробуй угадать! \nу тебя всего 10 попыток")

try:
    p =  int(input("слушаю! "))
    t = 9 # попытки
    
    while p != rn:
        if t >= 5 and t <= 9:
            print ("\n осталось", t, " попыток!")
        elif t >=2 and t <= 4:
            print ("\n осталось", t, " попытки!")
        elif t == 1:
            print ("\n осталось", t, " попытка, подумай!;) ") 


        if t == 0:
            break
        elif p < rn:
            print ("\n я загадал больше")
        elif p > rn:
            print ("\n я загадал меньше")    


        p = int(input("слушаю! "))
        t -= 1

    if p == rn and t == 9:   
        print ("\n Ого! С первого раза! Этого быть не может, давай еще раз!\n")
    elif p != rn and t == 0:
        print (" \n к сожалению это была последняя попытка! а загадал я", rn,"!\n")
    elif p == rn and t < 10:
        print ("поздравляю! ты угадал!")

except ValueError:
    print ("в следующий раз так не делай!) а число было ", rn)




