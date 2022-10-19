import mammoth
import logging 
import re

logging.basicConfig(level=logging.INFO)

def docx_to_html(docx_file):
    with open(docx_file, "rb") as docx:
        # docx_file_name =  get everything before the .docx
        docx_file_name = docx_file.split('.')[0]
        result = mammoth.convert_to_html(docx)
        # result_no_id_tags = mammoth.convert_to_html(docx, style_map = [
            
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion
        logging.info('messages: %s', messages)
        return html, docx_file_name


def convert_bad_characters(text):
    return text.replace('’', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-').replace('…', '...')

def remove_id_tags_from_html(text):
    # remove anything matching regex id\S*"
    return re.sub(r'id\S*"', '', text)



def write_to_file(html, filename):
    # get filetype from filename
    filetype = filename.split('.')[1]
    
    # remove bad characters from html 
    html = convert_bad_characters(html)
    html = remove_id_tags_from_html(html)
    
    # html remove instances of exact match <a ></a>
    html = html.replace('<a ></a>', '')
    html = html.replace('&lt;p&gt;', '')
    html = html.replace('&lt;br&gt;', '')
    html = html.replace('&lt;/h3&gt;;', '')
        
    with open(filename, 'w') as filetype:
        filetype.write(html)


def main(doc_path):
    
    html, docx_file_name = docx_to_html(doc_path)
    
    # write_to_file(html, docx_file_name + '.txt')    
    write_to_file(html, docx_file_name + '.html')


if __name__ == '__main__':
    import os 
    folder_path = os.getcwd() + '/SOMA'
    # get list of files in folder_path
    for file in os.listdir(os.getcwd()):
        # if file ends with .docx
        if file.endswith('.docx'):
            # html_file_name = file.split('.')[0] + '.html'
            # os.remove(html_file_name) # delete html file
            
            main(doc_path = file) # create html
            os.remove(file) # delete docx file