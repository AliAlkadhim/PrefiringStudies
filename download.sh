#!/bin/bash
//this just downloads the samples listed in sckim.csv into the outpur directory
OUTPUT_DIR=$1


while IFS=, read -r SAMPLE UNUSED
do
    echo ">>> Download sample ${SAMPLE}"
    xrdcp root://eospublic.cern.ch//eos/root-eos/HiggsTauTauReduced/${SAMPLE}.root ${OUTPUT_DIR}
done < skim.csv
