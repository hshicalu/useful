#!/bin/sh

echo
kotlinc $1.kt -include-runtime -d $1.jar
kotlin $1.jar
