def get_user_input(source_path, replica_path, synchronization_interval, log_file_path):
    return source_path, replica_path, synchronization_interval, log_file_path

if __name__ == '__main__':   
    get_user_input(input("Enter the source directory path: "), 
                   input("Enter the replica directory path: "), 
                   int(input("Enter the synchronization interval in seconds: ")), 
                   input("Enter the log file path: "))