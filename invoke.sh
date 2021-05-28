#!/bin/bash

OUTPUT=$(export OPENFAAS_URL=https://faasd.cthulu.tk && echo | faas-cli publish $1)
echo $OUTPUT
