#!/usr/bin/python
#-*- coding: utf-8 -*-

from Usuario import Usuario

class Administrador(Usuario):
    def __init__(self, publicar_evento, aprobar_evento, modificar_evento):
        self.Attribute1 = None
        self.publicar_evento = publicar_evento
        self.aprobar_evento = aprobar_evento
        self.modificar_evento = modificar_evento

    def publicarNuevoEvento(self, ):
        return self.publicar_evento

    def aprobarEvento(self, ):
        return self.aprobar_evento

    def modificarEvento(self, ):
        return self.modificar_evento

