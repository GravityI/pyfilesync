import unittest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pyfilesync import get_user_input, synchronize, list_dirs_files

class TestUserInput(unittest.TestCase):
    def setUp(self):
        self.source_path = "C:\\Nintendo\\"
        self.replica_path = "C:\\Nintendo\\"
        self.synchronization_interval = 60
        self.log_file_path = "C:\\Nintendo\\"

    #Test if input types are correct
    def test_get_user_input_types(self):
        source_path, replica_path, synchronization_interval, log_file_path = get_user_input(self.source_path, self.replica_path, self.synchronization_interval, self.log_file_path)
        self.assertIsInstance(source_path, str)
        self.assertIsInstance(replica_path, str)
        self.assertIsInstance(synchronization_interval, int)
        self.assertIsInstance(log_file_path, str)
    
    #Test if input paths are valid
    def test_get_user_input_paths(self):
        source_path, replica_path, synchronization_interval, log_file_path = get_user_input(self.source_path, self.replica_path, self.synchronization_interval, self.log_file_path)
        self.assertTrue(os.path.exists(os.path.dirname(source_path)))
        self.assertTrue(os.path.exists(os.path.dirname(replica_path)))
        self.assertTrue(os.path.exists(os.path.dirname(log_file_path)))

class TestSynchronization(unittest.TestCase):
    def setUp(self):
        self.source_dir = "C:\\testdir\\source\\"
        self.replica_dir = "C:\\testdir\\replica\\"
        self.inside_dir = "C:\\testdir\\source\\insideDir\\"
        self.even_more_inside_dir = "C:\\testdir\\source\\insideDir\\insideDir\\"
        if not os.path.exists(self.even_more_inside_dir):
            os.makedirs(self.even_more_inside_dir)
        with open(os.path.join(self.source_dir, "test.txt"), "w") as file:
            file.write("Hello World")
        with open(os.path.join(self.inside_dir, "test2.txt"), "w") as file:
            file.write("Bello Borld")
        with open(os.path.join(self.even_more_inside_dir, "test3.txt"), "w") as file:
            file.write("Aello Aorld")
    
    def test_synchronize(self):
        source_dirs, source_files = list_dirs_files(self.source_dir)
        synchronize(self.source_dir, self.replica_dir)
        replica_dirs, replica_files = list_dirs_files(self.replica_dir)
        for relative_file_path in source_files:
            with open(os.path.join(self.source_dir, relative_file_path), 'r') as source_file:
                with open(os.path.join(self.replica_dir, relative_file_path), 'r') as replica_file:
                    self.assertEqual(source_file.read(), replica_file.read())
        

if __name__ == '__main__':   
    unittest.main()