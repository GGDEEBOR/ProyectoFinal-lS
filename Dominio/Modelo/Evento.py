#!/usr/bin/python
#-*- coding: utf-8 -*-

class Evento:
    def __init__(self, tipoEvent, nombre, fecha, descripcion, lugar):
        self.tipoEvent = tipoEvento
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion
        self.lugar = lugar

    def setFecha(self, fecha):
        self.fecha = fecha

    def getFecha(self, ):
        return self.fecha

    def setLugar(self, lugar):
        self.lugar = lugar

    def getLugar(self, ):
        return lugar

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getDescripcion(self, ):
        return self.descripcion

