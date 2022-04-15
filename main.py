import os

name = input("Escreva nome do funcionario: ")
sal = int(input("Qual o salário do funcionario: R$"))

aum = sal*(1+0.25)
imp = aum-(1-0.05)

os.system("clear")
print("Nome do funcionario:",name)
print("Salário Inicial: R$",sal)
print("Salário com aumento: R$",aum)
print("Salário final: R$",imp)