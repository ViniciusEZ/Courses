import PyPDF2
import os

path_pdfs = '/home/vinicius/Documents/udemyPython/day16/meuspdfs'


new_pdf = PyPDF2.PdfMerger()
for root, dirs, files in os.walk(path_pdfs):
    for file in files:
        full_path_file = os.path.join(root, file)
        with open(full_path_file, 'rb') as f:
            new_pdf.append(f)

with open(f'{path_pdfs}/new_archive.pdf', 'wb') as my_new_pdf:
    new_pdf.write(my_new_pdf)

#
# with open(f'{path_pdfs}/new_archive.pdf', 'rb') as file_pdf:
#     reader = PyPDF2.PdfFileReader(file_pdf)
#     pag_nums = reader.getNumPages()
#
#     for pag_num in range(pag_nums):
#         escritor = PyPDF2.PdfFileWriter()
#         current_page = reader.getPage(pag_num)
#         escritor.addPage(current_page)
#
#         with open(f'/home/vinicius/Documents/udemyPython/day16/new_pdfs/{pag_num}.pdf', 'wb') as pdf_new:
#             escritor.write(pdf_new)


