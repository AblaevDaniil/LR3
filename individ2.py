#!/usr/bin/env python3
# -*- coding: utf-8 -*-
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 == -x2) and (y1 == -y2):
    print("Точки симметричны относительно начала координат")
if (x1 == -x2) and (y1 == y2):
    print("Точки симметричны относительно оси Y'")
if (x1 == x2) and (y1 == -y2):
    print("Точки симметричны относительно оси X")
else:
    print("Точки не симметричны")