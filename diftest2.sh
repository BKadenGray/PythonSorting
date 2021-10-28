#!/bin/bash

if diff -b sorted.txt longshort.txt;then
    echo "Passed"
else
    echo "Failed"
fi