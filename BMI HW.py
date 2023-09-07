# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:07:33 2023

@author: Manar
"""

def calculate_bmi(weight, height):
    bmi = (weight*10) /((height*height)*.001)
    return bmi

def interpret_bmi(bmi):
    if (bmi<18.5):
     print("underweight")
    elif (bmi>18.5 and bmi<=25):
     print("normal")
    elif (bmi>25 and bmi<=40):
     print("overweight")
    elif(bmi>40):
     print("obese")
weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)
description=interpret_bmi(bmi)



         
     
    
