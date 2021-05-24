#!/usr/bin/env bash

#SBATCH --job-name="GAUSS5_ERROR"
#SBATCH --partition=normal
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks=1
#SBATCH --nodelist="gauss11"
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2000M
#SBATCH --error='j%j.stderr'
#SBATCH --output='j%j.stdout'

python sleep.py
