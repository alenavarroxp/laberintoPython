#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bicho():
    def __init__(self):
        self.modo = None
        self.poder = None
        self.vidas = None
        self.posicion = None
    
    def esAgresivo(self):
        return self.modo.esAgresivo()
    
    def esPerezoso(self):
        return self.modo.esPerezoso()