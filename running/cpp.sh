#!/bin/sh

echo
g++ $1.cpp -std=c++11 -o $1
./$1
