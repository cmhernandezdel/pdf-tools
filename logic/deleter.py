from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

#
# User input: File, pages to delete OR File, page range to delete
# Example input: python deleter.py file.pdf 27 48
# Program output: The original pdf file without the desired pages
# Example output: file.pdf without pages 27 and 48
#################################################################
# Example input: python deleter.py file.pdf 27-48
# Program output: The original pdf file without the desired range of pages (BOTH included)
# Example output: file.pdf without pages from 27 to 48 both included
#

def deletePages(original_file, pages_to_remove):
  reader = PdfFileReader(original_file)
  writer = PdfFileWriter()
  output_path = "file_with_deleted_pages.pdf"

  # Write the file without the pages
  for i in range(reader.getNumPages()):
    if i not in pages_to_remove:
      writer.addPage(reader.getPage(i))

  # Output the file
  with open(output_path, 'wb') as output_file:
    writer.write(output_file)

def deleteRange(original_file, startingPage, endingPage):
  # Case of range of pages  
  # Write the file without the pages
  for i in range(reader.getNumPages()):
    if i < first_page_removed or i > last_page_removed:
      writer.addPage(reader.getPage(i))
  # Output the file
  with open(output_path, 'wb') as output_file:
    writer.write(output_file)