from pyclbr import Class
import unittest
import pandas as pd
import sys
import os
from combiner import Combiner
from unittest.mock import patch


class Combiner_Test(unittest.TestCase):
      # initialize all paths
    output_file_path = "./output.csv"
    file_csv_path = "./file.csv"
    accessories_part_path = "./test_csv/accessories_part.csv"
    clothing_part_path = "./test_csv/clothing_part.csv"
    hc_path = "./test_csv/hc_part.csv"
    final_csv_file = "./test_csv/final.csv"
    non_exist_path = "./non_exist_file.csv"


    combiner = Combiner()
    
    # def test_two_files_merge_fail_without_enough_input_files(self):
    #   """
    #   test_two_files_merge_fail_without_enough_input_files: if the number of input file <= 1 then not work
    #   """
    #   # python combiner.py (1.csv 2.csv) > output.csv 
    #   with patch("sys.argv", [self.accessories_part_path]):
    #     final_list_string = self.combiner.main()
    #     self.assertEquals(final_list_string[0], "Please enter equal or more than two csv files")

    # def test_non_exist_file(self):
    #   """
    #   test_non_exist_file: if the file does not exist then not work
    #   """
    #   with patch("sys.argv", [self.non_exist_path]):
    #     final_list_string = self.combiner.main()
    #     # print( final_list_string)
    #     self.assertEquals(final_list_string[1], "File does not exist")

    def test_value(self):
      # mock_args = [self.accessories_part_path, self.clothing_part_path]
      with patch("sys.argv", [self.accessories_part_path, self.clothing_part_path]):
        final_list_string = self.combiner.main()
        print(final_list_string)
        # self.assertEquals(final_list_string[0], "Please enter equal or more than two csv files")

if __name__ == '__main__':
    unittest.main()
