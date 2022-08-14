#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri

import datetime
import pyowm

def convertir_fecha(string_fecha):
    anio = string_fecha[0:4]
    mes = string_fecha[5:7]
    dia = string_fecha[8:10]
    if len (string_fecha) != 10:
        print ("Formato incorrecto, favor registrar la fecha con formato aaaa/mm/dd ")


def persona_titular(self)
    return f'Nombre: {self.persona_titular}'

class Persona(object):
    def __init__(self, dni, nombre, str_fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = convertir_fecha(str_fecha_nacimiento)
        self.dni = dni
        self.cuentas = []

    def __str__(self):
        return f'Nombre: {self.nombre}'

    @property
    def edad(self):
        hoy = datetime.date.today()
        delta = hoy - self.fecha_nacimiento
        return int(delta.days/365)

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def crear_cuenta(self):
        if 18 > self.edad < 31
            cuenta_nueva = cuenta.CuentaJoven(bonificacion=15)
        else self.edad >= 31:
            return cuenta == Cuenta()
        self.cuentas.appened(cuenta_nueva)
        if self.edad < 18:
            else:
            raise ValueError("Debe ser mayor de edad para crear una cuenta joven")

    def obtener_todos_los_movimientos(self):
        todos_los_movimientos = []
        for cuenta in self.cuentas:
            todos_los_movimientos += cuenta.movimientos
        return todos_los_movimientos

    def saludo(self):
        self persona_titular(saludo)
        return f"Persona saludando {self.nombre,w.get_reference_time(timeformat='iso')}"
