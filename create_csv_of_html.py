import pandas as pd
import glob
import os 

folder_paths = ['/_data/IDENTIFIER/html']

def consolidateHtmlToCsv(folder_path, brand):

    df = pd.DataFrame(columns = ['brand', 'filename', 'html'])

    for file in os.listdir(folder_path):
        
        # get text from html file
        with open(folder_path + '/' + file, 'r') as html_file:
            html = html_file.read()
            filename = file.split('.')[0]            
            page_id = filename.split('_')[0]
            
            file_df = pd.DataFrame({'brand': [brand], 'filename': [filename], 'page_id': [page_id], 'html': [html]})
            
            # combine with df
            df = pd.concat([df, file_df], axis = 0)

    return df


def main(folder_paths=folder_paths):
    
    paths_for_html = []
    
    for path in folder_paths:
        paths_for_html.append(os.getcwd() + path)
    
    df = pd.DataFrame(columns = ['brand', 'filename', 'page_id', 'html'])
    
    for path in paths_for_html:
        brand = path.split('/')[-2]
        file_df = consolidateHtmlToCsv(path, brand)
        df = pd.concat([df, file_df], axis = 0)

    return df

if __name__ == '__main__':
    out = main()
    out.to_csv('final_html_csv_file.csv', index = False)