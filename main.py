#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
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
#  
#  

def Menu(sel):
	if sel==1:
		import funcionMax
	elif sel==2:
		print('Hola')
def Seleccion():
	try:
		sel= int(raw_input("""
		(1) Determina cual numero es mayor
		(2) Obtener el factorial de un número
		"""))
	except ValueError:
		print('El numero ingresado no es un numero válido')
	return sel
		
def main():
	Menu(Seleccion())
if 1==1:
	main()
