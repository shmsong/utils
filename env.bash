#/usr/bin/bash
function sr(){
  screen -r $1
}

function sls(){
  screen -ls
}

function sc(){
  screen -S $1
}

