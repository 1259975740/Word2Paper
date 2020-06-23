# coding: utf-8
import docx
def read_docx(docx_path):
    docStr = docx.Document(docx_path)
    txt = []
    for para in docStr.paragraphs:
        parStr = para.text
        if_center = para.paragraph_format.alignment
        if if_center:
            parStr = parStr.center(30)
        else:
            parStr = '    ' + parStr
            
        txt.append(parStr)
    return '\n'.join(txt)


if __name__ == "__main__":
    txt = read_docx('E:\java-2020-03\eclipse\workspace\Word2write\Input\demo.docx')