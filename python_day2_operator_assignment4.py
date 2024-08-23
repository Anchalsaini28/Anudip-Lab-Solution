Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python program to find the area of a triangle whose sides are given
>>> #Sides of the triangle
>>> a = 4
>>> b = 3
>>> c = 5
>>> #Calculate the semi-perimeter
>>> s = (a + b + c) / 2
>>> # Calculate the area using Heron's formula
>>> area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
>>> print("The area of the triangle is:", area)
The area of the triangle is: 6.0
