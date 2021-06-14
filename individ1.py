#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input("Введите вас возраст: "))
if (n%10)>=5 or (n%10)==0:
    print("мне ",n," лет")
if (n%10)>1 and (n%10)<5:
    print("мне ",n," года")
if n%10==1:
    print("мне ",n," год")