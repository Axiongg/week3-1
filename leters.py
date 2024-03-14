# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:29:41 2024

@author: student
"""

letters = {"a":"A","b":"B","c":"C","d":"D","e":"E","f":"F","g":"G","h":"H","i":"I","j":"J","k":"K","l":"L","m":"M","n":"N","o":"O","p":"P","q":"Q","r":"R","s":"S","t":"T","u":"U","v":"V","w":"W","x":"X","y":"Y","z":"Z"}
a = input("輸入一個小寫字母:")
print("輸入的字母為",a,"大寫是",letters.get(a))