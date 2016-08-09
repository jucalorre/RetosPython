#! usr/bin/env python
# -*- coding: utf-8 -*-
#
#funcionFactorial.py

#  Copyright 2016 JuanCarlos <jncrls33@jncrls33-Inspiron-1525>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

def Obtener():
	try:
		numero= int(raw_input('Ingresa un número y te doy su fatorial: '))
	except ValueError:
		print('El valor que usted ingresó no es un número')
	return numero
	
def Factorial(numero, z=1, count=1):
	while z<= numero:
		count*=z
		z+=1
	print('El factorial del numero ' + str(numero) + ' es: ' + str(count))

Factorial(Obtener())
