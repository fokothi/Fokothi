#!/usr/bin/env python
# coding: utf-8

"""MCCM1107L Programming Lab-II
Assignment 1: HCF and LCM of Two Numbers
Student: Fokothi Mashoai | Roll Number: 26071257
"""
def calculate_hcf_lcm(first_number, second_number):
    
    #Negative numbers are not allowed
    #Reject the input if either integer is negative
    if first_number < 0 or second_number < 0:
        raise ValueError("Negative numbers are not allowed.")
    #Check if the HCF and LCM entered are both Zeros, then return the message
    if first_number == 0 and second_number == 0:
        raise ValueError("HCF and LCM are undefined when both numbers are zero.")

    #HCF and LCM are undefined when both numbers are zero
    if first_number == 0 or second_number == 0:
        non_zero_number = max(first_number, second_number)
        return non_zero_number, 0

    #If exactly one integer is zero, return the non-zero integer as HCF and zero as LCM
    larger_number = first_number
    smaller_number = second_number
    #Use While loop to find the HCF using the modulus sign
    while smaller_number != 0:
        larger_number, smaller_number = (
            smaller_number,
            larger_number % smaller_number,
        )
    hcf = larger_number

    #For two positive integers, use the algorithm and repeatedly replace (a, b) 
    #with (b, a and b) until b becomes zero
    lcm = (first_number // hcf) * second_number
    return hcf, lcm

#Print the results of HCF and LCM
print("HCF and LCM Calculator")
try:
    first_number = int(input("Enter the first non-negative integer:"))
    second_number = int(input("Enter the second non-negative integer: "))
    hcf, lcm = calculate_hcf_lcm(first_number, second_number)
    #Displaying the results in a user-friendly format
    print("\nResults")
    print("First Number:", first_number)
    print("Second Number:", second_number)
    print("HCF/GCD:", hcf)
    print("LCM", lcm)
except ValueError as error:
    print("\nInvalid input:", error)
    

