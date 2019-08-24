from PyPDF2 import PdfFileMerger, PdfFileReader

#
# User input: N pdf files to merge
# Example input: python merger.py file1.pdf file2.pdf file3.pdf
# Program output: Merged file
#
def merge_files(file_list):
  merger = PdfFileMerger()

  for element in file_list:
    merger.append(PdfFileReader(open(element, 'rb')))

  merger.write("merged_file.pdf")