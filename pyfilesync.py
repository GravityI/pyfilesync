def get_user_input():
    source_path = input("Enter the source directory path: ")
    replica_path = input("Enter the replica directory path: ")
    synchronization_interval = int(input("Enter the synchronization interval in seconds: "))
    log_file_path = input("Enter the log file path: ")

    return source_path, replica_path, synchronization_interval, log_file_path