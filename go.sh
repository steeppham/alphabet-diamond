#!/bin/sh

if [ "$#" -ne 1 ]
	then python alphabet-pyramid.py e
else
	python alphabet-pyramid.py "$1"
fi