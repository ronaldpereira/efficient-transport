#!/bin/bash

time python3 efficient_transport.py < $1 > $2

time pypy3 efficient_transport.py < $1 > $2
