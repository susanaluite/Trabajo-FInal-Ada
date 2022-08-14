#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri
import csv

import self as self

from persona import Persona

def crear_cuentas():
    """
    param: None
    :return: Lista de diccionarios
    """
    personas = {}
    archivo = open("personas.csv", "r")
    archivo_csv = csv.reader(archivo)
    titulos = next(archivo_csv)
    for nombre, dni, fecha_nacimiento in archivo_csv:
        persona = Persona(dni, nombre, fecha_nacimiento)
        persona.crear_cuenta()
        # La parte mas importante donde agrego al diccionario
        # con clave = dni el objecto persona
        personas[dni] = persona
    archivo.close()
    return personas

def procesar_gastos(cuentas, archivo):
    global cuentas_actualizadas
    primer_linea = True
     for linea in archivo:
         if not primer_linea:
             # Aca proceso la linea
             nro_cuenta, importe_gasto = linea.replace('\n', '').split(',')  # En Win es '\r\n'
             importe_gasto_int = float(importe_gasto)
             cuentas_actualizadas = aplicar_gastos(cuentas, nro_cuenta, importe_gasto_int)
         else:
             primer_linea = False
     archivo.close()
     return cuentas_actualizadas


def aplicar_depositos(cuentas, nro_cuenta, monto_float):
    pass


def procesar_depositos(cuentas, archivo):
    global cuentas_actualizadas
    primera_linea = True
    for linea in archivo:
        if not primera_linea:
            nro_cuenta, monto = linea.replace('\n', '').split(',')
            monto_float = float(monto)
            cuentas_actualizadas = aplicar_depositos(cuentas, nro_cuenta, monto_float)
        else:
            primera_linea = False
    archivo.close()
    return cuentas_actualizadas


def aplicar_transferencia(cuentas, nro_cuenta, monto_float):
    pass


def procesar_transferencias(cuentas, archivo):
    global cuentas_actualizadas
    primera_linea = True
    for linea in archivo:
        if not primera_linea:
            nro_cuenta, monto = linea.replace('\n', '').split(',')
            monto_float = float(monto)
            cuentas_actualizadas = aplicar_transferencia(cuentas, nro_cuenta, monto_float)
        else:
            primera_linea = False
    archivo.close()
    return cuentas_actualizadas
Footer
