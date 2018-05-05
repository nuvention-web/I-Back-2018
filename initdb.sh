#!/bin/bash

rm ./data.db

python app.py &

python initdb.py
