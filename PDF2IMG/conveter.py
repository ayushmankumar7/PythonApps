import os 
from pdf2image import convert_from_path 

def convert(path):

    print(path)
    
    try:
        os.system("mkdir output_file")
    except:
        pass


    pages = convert_from_path(path, 300)
    print(pages)
    
    path = path.split("/")
    pdf_file = path[-1][:-4]


    
    for page in pages:
        
        page.save("output_file/%s-page%d.jpg" % (pdf_file,pages.index(page)), "JPEG")

