import unittest, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pyfilesync import synchronize, list_dirs_files

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
        source_files = list_dirs_files(self.source_dir)[1]
        synchronize(self.source_dir, self.replica_dir)
        with open(os.path.join(self.replica_dir, "test.txt"), "w") as file:
            file.write("New text that wasn't previously here")
        synchronize(self.source_dir, self.replica_dir)
        #Check if file contents are the same after synchronization
        for relative_file_path in source_files:
            with open(os.path.join(self.source_dir, relative_file_path), 'r') as source_file:
                with open(os.path.join(self.replica_dir, relative_file_path), 'r') as replica_file:
                    self.assertEqual(source_file.read(), replica_file.read())
        #Check if synchronization also removes files from replica if they are removed from source
        os.remove(os.path.join(self.inside_dir, "test2.txt"))
        source_files = list_dirs_files(self.source_dir)[1]
        synchronize(self.source_dir, self.replica_dir)
        self.assertEqual(list_dirs_files(self.source_dir), list_dirs_files(self.replica_dir))

if __name__ == '__main__':   
    unittest.main()