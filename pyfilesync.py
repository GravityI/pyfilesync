import os

def get_user_input(source_path, replica_path, synchronization_interval, log_file_path):
    #print(source_path, replica_path, synchronization_interval, log_file_path)
    return source_path, replica_path, synchronization_interval, log_file_path

def list_dirs_files(root_path):
    dir_path_list = []
    file_path_list = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            file_path_list.append(os.path.relpath(os.path.join(root, file), root_path))
        for dir in dirs:
            dir_path_list.append(os.path.relpath(os.path.join(root, dir), root_path))
    return dir_path_list, file_path_list

def synchronize(source_dir, replica_dir, synchronization_interval=None, log_file_path=None):
    source_dir_path_list, source_file_path_list = list_dirs_files(source_dir)
    replica_dir_path_list, replica_file_path_list = list_dirs_files(replica_dir)
    
    #Copy files/subdirectories from the source directory into the replica directory
    for dir in source_dir_path_list:
        if not os.path.exists(os.path.join(replica_dir, dir)):
            os.makedirs(os.path.join(replica_dir, dir))
    for file in source_file_path_list:
        with open(os.path.join(source_dir, file), 'r') as source_file:
            with open(os.path.join(replica_dir, file), 'w') as replica_file:
                replica_file.write(source_file.read())
    
    #Delete files/subdirectories from the replica directory if they do not exist in the source directory
    for dir in replica_dir_path_list:
        if not os.path.exists(os.path.join(source_dir, dir)):
            os.remove(os.path.join(replica_dir, dir))
    for file in replica_file_path_list:
        if not os.path.exists(os.path.join(source_dir, file)):
            os.remove(os.path.join(replica_dir, file))
    #sleep(synchronization_interval)
    #return synchronize(source_dir, replica_dir, synchronization_interval, log_file_path)

if __name__ == '__main__':   
    get_user_input(input("Enter the source directory path: "), 
                   input("Enter the replica directory path: "), 
                   int(input("Enter the synchronization interval in seconds: ")), 
                   input("Enter the log file path: "))
    #sleep(synchronization_interval)
    
    '''
    with open("C:\\Nintendo\\test.txt", "r") as file:
        print(file.read())
    '''