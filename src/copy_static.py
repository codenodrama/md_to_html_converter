import os
import shutil

def copy_static(src, dest):
    dest_list_dir = os.listdir(dest)
    for dest_item in dest_list_dir:
        path_dest_item = os.path.join(dest, dest_item)
        if(os.path.isfile(path_dest_item)):
            os.remove(path_dest_item)
        elif(os.path.isdir(path_dest_item)):
            shutil.rmtree(path_dest_item)
    
    src_list_dir = os.listdir(src)
    for src_item in src_list_dir:
        path_src_item = os.path.join(src, src_item)
        if(os.path.isfile(path_src_item)):
            shutil.copy(path_src_item, dest)
        elif(os.path.isdir(path_src_item)):
            new_dest_dir = os.path.join(dest, src_item)
            os.makedirs(new_dest_dir)
            copy_static(path_src_item, new_dest_dir)





    



    


    

