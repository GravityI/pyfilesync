import os, filecmp, time, logging, sys

logger = logging.getLogger(__name__)

def list_dirs_files(root_path):
    dir_path_list = []
    file_path_list = []
    for root, dirs, files in os.walk(root_path):
        for file in files:
            file_path_list.append(os.path.relpath(os.path.join(root, file), root_path))
        for dir in dirs:
            dir_path_list.append(os.path.relpath(os.path.join(root, dir), root_path))
    return dir_path_list, file_path_list

def synchronize(source_dir, replica_dir):
    logging.info("Synchronization Started")

    source_dir_path_list, source_file_path_list = list_dirs_files(source_dir)
    replica_dir_path_list, replica_file_path_list = list_dirs_files(replica_dir)

    #Copy files/subdirectories from the source directory into the replica directory
    for dir in source_dir_path_list:
        if not os.path.exists(os.path.join(replica_dir, dir)):
            os.makedirs(os.path.join(replica_dir, dir))
            logging.info("Created directory " + os.path.join(replica_dir, dir))
    for file in source_file_path_list:
        with open(os.path.join(source_dir, file), 'r') as source_file:
            #Check if file exists and compare file contents
            file_exists = False
            if os.path.isfile(os.path.join(replica_dir, file)):
                with open(os.path.join(replica_dir, file), 'r') as replica_file:
                        if not filecmp.cmp(os.path.join(source_dir, file), os.path.join(replica_dir, file), shallow=False):
                            with open(os.path.join(replica_dir, file), 'w') as replica_file:
                                replica_file.write(source_file.read())
                                #Implement MD5 checksum
                                logging.info("Modified file " + os.path.join(replica_dir, file))
            else:
                with open(os.path.join(replica_dir, file), 'w') as replica_file:
                    replica_file.write(source_file.read())
                    logging.info("Created file " + os.path.join(replica_dir, file))
    
    #Delete files/subdirectories from the replica directory if they do not exist in the source directory
    for file in replica_file_path_list:
        if not os.path.exists(os.path.join(source_dir, file)):
            os.remove(os.path.join(replica_dir, file))
            logging.info("Removed file " + os.path.join(replica_dir, file))
    for dir in replica_dir_path_list:
        if not os.path.exists(os.path.join(source_dir, dir)):
            os.rmdir(os.path.join(replica_dir, dir))
            logging.info("Removed directory " + os.path.join(replica_dir, dir))

def main():
    source_dir_path, replica_dir_path, log_file_path, interval = sys.argv[1:]
    interval = int(interval)

    #Ensure that the arguments are valid
    if not os.path.exists(source_dir_path):
        raise Exception("Source directory path is not a valid path")
    if not os.path.exists(replica_dir_path):
        raise Exception("Replica directory path is not a valid path")
    if interval <= 0:
        raise Exception("Interval must be greater than zero")
    
    logging.basicConfig(encoding="utf-8", level=logging.INFO, handlers=[logging.FileHandler(log_file_path),
                                                                        logging.StreamHandler()])
    logging.info("Program Started")
    
    while True:
        logging.info("Awaiting Interval")
        time.sleep(interval)
        synchronize(source_dir_path, replica_dir_path)
        
if __name__ == '__main__':
    main()