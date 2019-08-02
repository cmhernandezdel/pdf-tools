from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

#
# User input: File, number of cuts, cut points (page number)
# Example input: python splitter.py file.pdf 2 13 35
# Program output: As many PDF files as cut points + 1
# Example output: 3 files: 1-13, 14-35 and 36-last
#

with open(sys.argv[1]) as original_file:
  reader = PdfFileReader(original_file)
  number_of_cuts = int(sys.argv[2])
  starting_page = 0

  # Get as many files as cuts
  for i in range(number_of_cuts + 1):
    ending_page = int(sys.argv[3+i]) if i != number_of_cuts else reader.getNumPages()
    writer = PdfFileWriter()
    for j in range(starting_page, ending_page):
      writer.addPage(reader.getPage(j))
    output_path = ("splitted_file_" + str(i) + ".pdf")
    with open(output_path, 'wb') as output_file:
      writer.write(output_file)
    starting_page = ending_page
