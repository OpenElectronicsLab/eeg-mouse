#!/bin/sh

EXG="../OpenHardwareExG/src"
SAMPLE=`date +"%Y%m%d.%H%M%S"`

./killreader.sh $1 &
$EXG/serial-reader.pl |
$EXG/frame-parser.pl |
./parsed-frame-filter.pl |
tee sample-${USER}-${SAMPLE}.csv |
./plot.pl
