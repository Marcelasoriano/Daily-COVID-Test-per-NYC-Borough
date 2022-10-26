#Name: Marcela Soriano Cornejo
#Email: marcela.sorianocornejo40@myhunter.cuny.edu
#Date: 25 October 2022
#Program 27: This code prints Daily Covid Test

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = input("Enter a csv file: ")
df = pd.read_csv(file)
borough = input("Enter a borough (Bronx, Brooklyn, Queens, Manhattan, Staten Island: ")
output = input("Enter output name: ")

min = df[borough].min()
max = df[borough].max()
mean = df[borough].mean()
median = df[borough].median()
standard = round(df[borough].std(), 3)

print("Min:", min)
print("Max:", max)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", standard)

df["Fraction"] = (df[borough]/df["Case Count"])
df.plot(x="Date of Interest", y= "Fraction")

fig = plt.gcf()
fig.savefig(output)