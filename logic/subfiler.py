from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

#
# User input: File, range of pages of the subfile
# Example input: python subfiler.py 25-30
# Program output: A pdf file containing the pages in the index included
# Example output: subfile.pdf: a pdf containing pages from 25 to 30 of the original file, both included
#

with open(sys.argv[1], 'rb') as original_file:
  reader = PdfFileReader(original_file)
  starting_page = int(sys.argv[2].split("-")[0]) - 1
  ending_page = int(sys.argv[2].split("-")[1]) - 1
  writer = PdfFileWriter()
  output_path = "subfile.pdf"


  # Get as many files as cuts
  for i in range(reader.getNumPages()):
    if i >= starting_page and i <= ending_page:
      writer.addPage(reader.getPage(i))

  # Output the file
  with open(output_path, 'wb') as output_file:
    writer.write(output_file)