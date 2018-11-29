#!/bin/bash
#
#PBS -l walltime=05:00:00
#PBS -l nodes=4:ppn=5
#PBS -W group_list=newriver
#PBS -q normal_q
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
#
#export PYTHONUSERBASE=/home/mrisley/newriver/python
#easy_install --user `cat requirements.txt`

python arc_sim.py
