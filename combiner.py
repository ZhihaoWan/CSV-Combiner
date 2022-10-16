import pandas as pd
import sys
import os
import shlex

class Combiner:

    def console_first_file_csv(self):
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
            # print(console_list)
            return console_list


    def combine_all_df(self, df, csv_name_list):
        df_new = None
        # print("****************************************************************")
        # print(csv_name_list)

        if csv_name_list is not None:
            for i in csv_name_list:  
                tem_df = pd.read_csv(i)
                tem_df['source'] = i
                df.append(tem_df)
            df_new = pd.concat(df, ignore_index=True)
        return df_new


    def convert_df_to_csv(self, df): 
        final_csv_string = df.to_string(header=True,
                  index=False,
                  sep = '\t',
                  index_names=False).split('\n')

        final_list_string = final_list_string = ['\"{}\"'.format('\",\"'.join(ele.split('\t'))) for ele in final_csv_string]

        for line in final_list_string:
            sys.stdout.write(line.strip() + '\n')
        return final_list_string


    def main(self):
        file = self.console_first_file_csv()
        # print(file)

        if file is None: 
            return ["Please enter equal or more than two csv files", "File does not exist"]

        df = self.combine_all_df([], file)
        return self.convert_df_to_csv(df)
    

def main():
            combine_obj = Combiner()
            file = combine_obj.console_first_file_csv()

            if file is None: 
                return None 

            df = combine_obj.combine_all_df([], file)
            return combine_obj.convert_df_to_csv(df)
            
if __name__ == "__main__":
    main()
