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

with open(sys.argv[1], 'rb') as original_file:
  reader = PdfFileReader(original_file)
  writer = PdfFileWriter()
  output_path = "file_with_deleted_pages.pdf"

  # Case of certain pages
  if "-" not in sys.argv[2]:

    # Get the pages we want to remove (-1 because users start counting from 1)
    pages_to_remove = []
    for page in sys.argv[2:]:
      pages_to_remove.append(int(page) - 1)

    # Write the file without the pages
    for i in range(reader.getNumPages()):
      if i not in pages_to_remove:
        writer.addPage(reader.getPage(i))

  # Case of range of pages  
  else:
    # Get the starting and ending pages (-1 because users start counting from 1)
    first_page_removed = int(sys.argv[2].split("-")[0]) - 1
    last_page_removed = int(sys.argv[2].split("-")[1]) - 1

    # Write the file without the pages
    for i in range(reader.getNumPages()):
      if i < first_page_removed or i > last_page_removed:
        writer.addPage(reader.getPage(i))

# Output the file
  with open(output_path, 'wb') as output_file:
    writer.write(output_file)