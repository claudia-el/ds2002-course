#!/bin/bash
#SBATCH --account=ds2002
#SBATCH --partition=standard
#SBATCH --job-name=jokes_array       
#SBATCH --output=jokes_%j.out        
#SBATCH --error=jokes_%j.err     
#SBATCH --time=00:01:00             
#SBATCH --mem=8G
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-10

module load apptainer
module load miniforge
source activate ds2002


echo "Running job array task ID: $SLURM_ARRAY_TASK_ID"


echo "Hello from task $SLURM_ARRAY_TASK_ID!"

apptainer run ~/lolcow-latest.sif