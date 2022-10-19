import pandas as pd
import glob
import os 


def consolidateHtmlToCsv(folder_path, brand):

    df = pd.DataFrame(columns = ['brand', 'filename', 'html'])

    for file in os.listdir(folder_path):
        
        # get text from html file
        with open(folder_path + '/' + file, 'r') as html_file:
            html = html_file.read()
            filename = file.split('.')[0]
            
            file_df = pd.DataFrame({'brand': [brand], 'filename': [filename], 'html': [html]})
            
            # combine with df
            df = pd.concat([df, file_df], axis = 0)

    return df


def main():
    folder_path_chicos = os.getcwd() + '/CHICOS/Html'
    folder_path_whbm = os.getcwd() + '/WHBM/Html'
    folder_path_soma = os.getcwd() + '/SOMA/Html'
    
    paths = [folder_path_chicos, folder_path_whbm, folder_path_soma]
    
    df = pd.DataFrame(columns = ['brand', 'filename', 'html'])
    
    for path in paths:
        
        brand = path.split('/')[-2]
        
        file_df = consolidateHtmlToCsv(path, brand)
        
        df = pd.concat([df, file_df], axis = 0)

    return df

if __name__ == '__main__':
    out = main()
    out.to_csv('final_html_csv_file.csv', index = False)