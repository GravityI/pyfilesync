import unittest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pyfilesync import get_user_input

class TestUserInput(unittest.TestCase):
    def setUp(self):
        self.source_path = "C:\\"
        self.replica_path = "C:\\"
        self.synchronization_interval = 60
        self.log_file_path = "C:\\"

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

if __name__ == '__main__':   
    unittest.main()