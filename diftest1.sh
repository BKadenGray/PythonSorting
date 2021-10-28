#!/bin/bash

if diff -b sorted.txt shortlong.txt;then
    echo "Passed"
else
    echo "Failed"
fi