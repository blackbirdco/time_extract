#!/bin/sh

docker run -t -i --rm -e LANG=C.UTF-8 -v $PWD:/time_extract time_extract
