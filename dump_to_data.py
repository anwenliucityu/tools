import atomman as am
import multiprocessing as mp
from functools import partial
import re
import os
import numpy as np

# extract the number of files and name of files
def fileprocess(path):
    filenames = []
    filenum = 0
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            filenum = filenum+1
            filenames.append(lists)
    # sort the list according to its dump sequence
    filenames.sort(key=lambda x: int(x.split('PyrII_ac_')[-1]))
    return filenum, filenames

def dump_to_data(dump_path, work_path):
    new_name = dump_path + '.dat'
    output_path = os.path.join(work_path,'data_file')
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    new_file = os.path.join(output_path,new_name)
    sys = am.load('atom_dump', os.path.join(work_path,dump_path))
    write_data = sys.dump('atom_data', f=new_file)

def multicore(dump_path, work_path):
    pool = mp.Pool()
    par_ave = partial(dump_to_data, work_path = work_path)
    pool.map(par_ave, dump_path)

if __name__ == '__main__':
    work_path = '/gauss12/home/cityu/anwenliu/scratch/dislocation_simulation/Mg/metastable_core_MEAM/dump_file'
    filenum, dump_path = fileprocess(work_path)
    multicore(dump_path, work_path)
