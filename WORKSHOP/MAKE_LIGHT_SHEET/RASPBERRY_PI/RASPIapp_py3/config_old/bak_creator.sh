#!/bin/bash

echo "Copying (overwrite) of active config into backup"
cp ./*.yaml ./backup/
cd ./backup/
for myfile in *.yaml
do
  mv "$myfile" "${myfile/yaml/bak}"
done
