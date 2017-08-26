# -*- coding: utf-8 -*-
# @Author: Rubén Couoh
# @Date:   2017-08-24 09:02:00
# @Last Modified by:   Rubén Couoh
# @Last Modified time: 2017-08-24 22:40:13

import os

######################################
########## Logica de la cola #########
######################################

container = []

def isEmpty():
	return len(container) is 0 if True else False

def push(item):
	container.append(item);

def pop():

	item = None

	if not isEmpty():
		item = container.pop(0)
	
	return item


def peek():
	item = None
	if not isEmpty():	
		item = container[0]
	return item


def showQueue():
	size = len(container)
	if size > 0:
		head = ''
		body = ''
		foot =''

		#print('\t+-----+')
		for i in range(size):		
			if  0 < i < size-1: 
				#print('\t|{0:^5}|\n\t+-----+'.format(container[i]))
				head += '+-----'
				body += '|{0:^5}'.format(container[i])
				foot += '+-----'
			elif i is 0:
				#print('\t|{0:^5}| --> PRIMERO\n\t+-----+'.format(container[i]))
				head += '+-----'
				body += '|{0:^5}'.format(container[i])
				foot += '+-----'
			elif i is size-1: 
				#print('\t|{0:^5}| --> ULTIMO\n\t+-----+'.format(container[i]))
				head += '+-----+'
				body += '|{0:^5}|'.format(container[i])
				foot += '+-----+'

		if size is 1:
			head += '+'
			body += '|'
			foot += '+'

		print('\t            {}\n\tPRIMERO <-- {} --> ULTIMO\n\t            {}\n'.format(head, body, foot))
	else:
		print('La cola está vacia!')



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
			showQueue()

		elif option is 2:
			if not isEmpty():
				top = peek()
				print('\t{} --> PRIMERO'.format(top))
			else:
				print('La cola está vacia!')

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
				print('La cola está vacia!')
				
		else:
			print('\tOpción incorrecta!\n')

		print()
		input('Presione ENTER para continuar...\n')
	else:
		exit()
			

def printMenu():
	print('+--------------------------------------------------------------+')
	print('| ************************************************************ |')
	print('| *******************     COLA NUMERICA    ******************* |')
	print('| ************************************************************ |')
	print('| ***************      Opciones del menú       *************** |')
	print('| ************************************************************ |')
	print('| **********          1) Ver cola                   ********** |')
	print('| **********          2) Ver primero                ********** |')
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