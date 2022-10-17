import mammoth
import logging 

logging.basicConfig(level=logging.INFO)

def docx_to_html(docx_file):
    with open(docx_file, "rb") as docx:
        # docx_file_name =  get everything before the .docx
        docx_file_name = docx_file.split('.')[0]
        result = mammoth.convert_to_html(docx)
        html = result.value # The generated HTML
        messages = result.messages # Any messages, such as warnings during conversion
        logging.info('messages: %s', messages)
        return html, docx_file_name


def convert_bad_characters(text):
    return text.replace('’', "'").replace('“', '"').replace('”', '"').replace('–', '-').replace('—', '-').replace('…', '...')


def write_to_file(html, filename):
    # get filetype from filename
    filetype = filename.split('.')[1]
    
    # remove bad characters from html 
    html = convert_bad_characters(html)
    
    with open(filename, 'w') as filetype:
        filetype.write(html)


def main(doc_path):
    
    html, docx_file_name = docx_to_html(doc_path)
    
    write_to_file(html, docx_file_name + '.txt')    
    write_to_file(html, docx_file_name + '.html')


if __name__ == '__main__':
    main(doc_path = 'TESTING.docx')