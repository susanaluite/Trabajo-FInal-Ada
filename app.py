#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Meri

import flask
from flask import Flask, render_template, request

import proceso_cuentas

# Creación de la App
app = Flask(__name__)

# definimos configuraciones
app.config['UPLOAD_FOLDER'] = './'
app.config['MAX_CONTENT_PATH'] = 2048

# definimos nuestros datos en memoria (base de datos)
lista_de_datos = {}


# TODO: Reemplazar por cada uno de los procesos
@app.route('/procesar_depositos', methods=['POST'])
def procesar_depositos():
    global cuentas_actualizadas
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        f: primera_linea = True
        for linea in archivo:
        if not primera_linea:
            nro_cuenta, monto = linea.replace('\n', '').split(',')
            monto_float = float(monto)
            cuentas_actualizadas = aplicar_depositos(cuentas, nro_cuenta, monto_float)
        else:
            primera_linea = False
    archivo.close()
    return cuentas_actualizadas
        # lista_de_datos = proceso_cuentas.procesar_depositos(lista_de_datos, f.filename)
        return flask.redirect(flask.url_for('home'), code=302)


def aplicar_gastos(cuentas, nro_cuenta, importe_gasto_int):
    pass


@app.route('/procesar_gastos', methods=['POST'])
def procesar_gastos():
    global cuentas_actualizadas
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        f: primer_linea = True
    for linea in archivo:
        if not primer_linea:
            # Aca proceso la linea
            nro_cuenta, importe_gasto = linea.replace('\n', '').split(',')  # En Win es '\r\n'
            importe_gasto_int = float(importe_gasto)
            cuentas_actualizadas = aplicar_gastos(cuenta, nro_cuenta, importe_gasto_int)
        else:
            primer_linea = False
    archivo.close()
    return cuentas_actualizadas


def aplicar_transferencias(cuenta, nro_cuenta, importe_gasto_int):
    pass


@app.route('/procesar_transferencias', methods=['POST'])
def procesar_transferencias():
    global cuentas_actualizadas
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        f: primer_linea = True
    for linea in archivo:
        if not primer_linea:
            # Aca proceso la linea
            nro_cuenta, importe_gasto = linea.replace('\n', '').split(',')  # En Win es '\r\n'
            importe_gasto_int = float(importe_gasto)
            cuentas_actualizadas = aplicar_transferencias(cuenta, nro_cuenta, importe_gasto_int)
        else:
            primer_linea = False
    archivo.close()
    return cuentas_actualizadas


@app.route('/proceso')
def proceso():
    return render_template('proceso.html')


@app.route('/')
def home():
    # TODO: Si no existe, reemplazar saludo por un mensaje que explique que no se envio dni o no existe en nuestra db
    persona_titular = lista_de_datos[str(dni)]
    return render_template('home-banking.html',
                           saludo=persona_titular.saludo(),
                           movements=persona_titular.obtener_todos_los_movimientos())


if __name__ == '__main__':
    lista_de_datos = proceso_cuentas.crear_cuentas()
    app.run(debug=True)
