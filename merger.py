from PyPDF2 import PdfFileMerger, PdfFileReader
import sys

merger = PdfFileMerger()

for i in range(1, len(sys.argv)):
  merger.append(PdfFileReader(file(sys.argv[i], 'rb')))

merger.write("merged_file.pdf")