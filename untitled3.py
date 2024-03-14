# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:14:32 2024

@author: student
"""

transform = {}

transform["a"] = "A"
transform["b"] = "B"
transform["c"] = "C"
transform["d"] = "D"
transform["e"] = "E"
transform["f"] = "F"
transform["g"] = "G"
transform["h"] = "H"
transform["i"] = "I"
transform["j"] = "J"
transform["k"] = "K"
transform["l"] = "L"
transform["m"] = "M"
transform["n"] = "N"
transform["o"] = "O"
transform["p"] = "P"
transform["q"] = "Q"
transform["r"] = "R"
transform["s"] = "S"
transform["t"] = "T"
transform["u"] = "U"
transform["v"] = "V"
transform["w"] = "W"
transform["x"] = "X"
transform["y"] = "Y"
transform["z"] = "Z"

input_string = input(": ")
input_string = list(input_string)
for i in range(len(input_string)):
    input_string[i] = transform[input_string[i]]
    
output_string = "".join(input_string)
print(":",output_string)    