#!/usr/bin/env python
import sys,string

nomfp="/etc/passwd"

fp=open(nomfp,"r")

usuarios={}
while True:
	linea=fp.readline()
	if not linea:
		break
	campos=string.split(linea,":")
	usuarios[campos[0]]=campos[4]
fp.close()

while True:
	sys.stdout.write("¿Usuario?: ")
	linea=sys.stdin.readline()
	if not linea:
		break
	login=string.strip(linea)
	if usuarios.has_key(login):
		print " "+usuarios[login]
	else:
		print " Usuario desconocido"
	print
	print "¡Hasta otra!"