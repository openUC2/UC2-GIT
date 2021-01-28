#!/bin/bash 
#set -x 
# solution from: https://stackoverflow.com/a/13738951 
function git_sparse_clone() { 
    rurl="$1" localdir="$2" && shift 2 
    mkdir -p "$localdir" 
    cd "$localdir" 
    git init 
    git remote add -f origin "$rurl" 
    git config core.sparseCheckout true 
    # Loops over remaining args 
    for i; do 
     echo "$i" >> .git/info/sparse-checkout 
    done 
    git pull --depth=1 origin master 
} 
git_sparse_clone "https://github.com/bionanoimaging/UC2-Software-GIT/tree/master/GUI/RASPBERRY_PI/RASPIapp_py3" "."