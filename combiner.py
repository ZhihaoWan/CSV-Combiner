import pandas as pd
import sys
import os
import shlex

class Combiner:

    def console_first_file_csv(self):
        """
        Combiner for first file csv
        
        Read all arguments from the termial console, and save them to a console_list

        If the csv file name do not exist, then the write a "File does not exist" in to the combine.csv file
        If the number of input csv file <= 1, then write a "Please enter equal or more than two csv files" into the combine.csv file
        """
        console_list = []

        for i in range(1, len(sys.argv)):
                contents = sys.argv[i]
                console_list.append(contents)

        for filename in console_list:
                        if not os.path.exists(filename):
                            print("File does not exist")
                            return None

        if len(console_list) <= 1:
                print("Please enter equal or more than two csv files")
                return None 
        return console_list


    def combine_all_df(self, df, csv_name_list):
        """
        1.Combine all csv files into the a data frame at first.
        2. For the last column is for the 'source' 
        3. Finally, return the data frame.
        """
        df_new = None

        if csv_name_list is not None:
            for i in csv_name_list:  
                tem_df = pd.read_csv(i)
                tem_df['source'] = i
                df.append(tem_df)
            df_new = pd.concat(df, ignore_index=True)
        return df_new


    def convert_df_to_csv(self, df): 
        """
        1. Dataframe to String
        2. String preossing as a string list 
        3. sys.stdout write them into a csv file
        4. return the final_list_string for testing usage
        """
        final_csv_string = df.to_csv(index=False)
        sys.stdout.write(final_csv_string)
        return final_csv_string

    def main(self):
        """
        1. If the file is not exist, which means we have to return a Error list for testing purposes
        2. Otherwise, the following process for wrap up the data frame process still need to be executed
        """
        file = self.console_first_file_csv()

        if file is None: 
            return ["Please enter equal or more than two csv files", "File does not exist"]

        df = self.combine_all_df([], file)
        return self.convert_df_to_csv(df)
    

def main():
    """
    -- Main funciton here for the command line calling 
    """
    combine_obj = Combiner()
    file = combine_obj.console_first_file_csv()

    if file is None: 
        return None 

    df = combine_obj.combine_all_df([], file)
    return combine_obj.convert_df_to_csv(df)
            
if __name__ == "__main__":
    main()
