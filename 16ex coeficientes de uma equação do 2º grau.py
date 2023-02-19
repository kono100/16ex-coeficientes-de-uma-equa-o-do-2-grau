''' Faça um programa que leia os coeficientes de uma equação do 2º grau, sendo: a, b e c. 
Calcule e retorne o valor de seu discriminante (delta), através da fórmula: 
https://brasilescola.uol.com.br/matematica/equacao-2-grau.htm
Calcule as raízes da equação através da fórmula: '''


a = int(input('Escreva o valor de a: '))
b = int(input('Escreva o valor de b: '))
c = int(input('Escreva o valor de c: '))

delta = (b**2) - (4*a*c)

raizdelta = delta**0.5

x1 = (-b + raizdelta) / (2*a)
x2 = (-b - raizdelta) / (2*a)

print(f'X1: {x1}')
print(f'X2: {x2}')
