from PyPDF2 import PdfFileMerger, PdfFileReader
import sys

#
# User input: N pdf files to merge
# Example input: python merger.py file1.pdf file2.pdf file3.pdf
# Program output: Merged file
#

merger = PdfFileMerger()

for i in range(1, len(sys.argv)):
  merger.append(PdfFileReader(file(sys.argv[i], 'rb')))

merger.write("merged_file.pdf")