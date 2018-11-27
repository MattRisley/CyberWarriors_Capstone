#!/bin/bash
#
#PBS -l walltime=00:30:00
#PBS -l nodes=1:ppn=20
#PBS -W group_list=newriver
#PBS -q open_q
#PBS -j oe
#PBS -A CMDA_Cap_18
#
cd $PBS_O_WORKDIR
#
# 
module purge
#
module load Anaconda
module load gcc/5.2.0 python/3.5.0
easy_install --user `cat requirements.txt`

python arc_sim.py