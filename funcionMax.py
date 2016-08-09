#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funcionMax.py
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

def Max(val1, val2):
	if val1>val2:
		print "El primer numero es mayor al segundo"
	elif val1<val2:
		print "El segundo numero es mayor al primero"
	else:
		print "Los dos numeros son iguales"
		
try:
    val1=int(raw_input('Ingresa el primer valor: '))
    val2=int(raw_input('Ingresa el segundo valor: '))
    Max(val1,val2)
except ValueError: #Captura los errores 
    print "Alguno de los valores ingresados no es un número"

