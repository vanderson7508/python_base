#!/usr/bin/env python3
"""
LinuxTips
alerta 
"""

temp  = float(input("Digite a temperatura atual: "))

umd = float(input("Digite a umidade atual: "))

if temp > 45:
    print("Alerta!!!! Perigo calor extremo")

elif (temp * 3) >= umd:
    print("Alerta!!!! Perigo calor umido")

elif 10 < temp < 30:
     print("Normal")

elif 0 < temp < 10:
    print("Frio")
    
elif temp < 0:
    print("Alerta!!! Frio extremo")
    
