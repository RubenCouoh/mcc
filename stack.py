# -*- coding: utf-8 -*-
# @Author: Rubén Couoh
# @Date:   2017-08-24 09:02:00
# @Last Modified by:   Rubén Couoh
# @Last Modified time: 2017-08-24 22:41:16

import os

######################################
########## Logica de la pila #########
######################################

container = []

def isEmpty():
	return len(container) is 0 if True else False

def push(item):
	container.append(item);

def pop():

	item = None

	if not isEmpty():
		item = container.pop()
	
	return item


def peek():
	item = None
	if not isEmpty():	
		item = container[-1]
	return item


def showStack():
	size = len(container)
	if size > 0:
		print('\t+-----+')
		for i in range(size-1, -1, -1):
			
			if i is not size-1: 
				print('\t|{0:^5}|\n\t+-----+'.format(container[i]))
			else:
				print('\t|{0:^5}| --> CIMA\n\t+-----+'.format(container[i]))
	else:
		print('La pila está vacia!')



########################################
########## Logica del programa #########
########################################

def main():
	while True:
		os.system('clear')
		
		printMenu()
		option = readOption()
		
		print()
		if option is 5:
			break

		elif option is 1:
			showStack()

		elif option is 2:
			if not isEmpty():
				top = peek()
				print('\t{} --> CIMA'.format(top))
			else:
				print('La pila está vacia!')

		elif option is 3:
			try:
				item = int(input('\tELEMENTO: '))
				push(item)
				print('\t{} AGREGADO'.format(item))
			except ValueError as e:
				print('\tElemento incorrecto!')

		elif option is 4:
			if not isEmpty():
				top = pop()
				print('\t{} ELIMINADO'.format(top))
			else:
				print('La pila está vacia!')
		else:
			print('\tOpción incorrecta!\n')

		print()
		input('Presione ENTER para continuar...\n')
	else:
		exit()
			

def printMenu():
	print('+--------------------------------------------------------------+')
	print('| ************************************************************ |')
	print('| *******************     PILA NUMERICA    ******************* |')
	print('| ************************************************************ |')
	print('| ***************      Opciones del menú       *************** |')
	print('| ************************************************************ |')
	print('| **********          1) Ver pila                   ********** |')
	print('| **********          2) Ver cima                   ********** |')
	print('| **********          3) Agregar elemento           ********** |')
	print('| **********          4) Eliminar elemento          ********** |')
	print('| **********          5) Salir                      ********** |')
	print('| ************************************************************ |')
	print('+--------------------------------------------------------------+')

def readOption():
	try :
		option = int(input('Selecciona una opción: '))
	except ValueError as e:
		option = -1;
	
	return option


if __name__ == '__main__':
	main()