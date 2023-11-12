#Do this first in terminal
#pip install pymupdf

import fitz  # PyMuPDF

def pdf_to_text(pdf_path, text_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Initialize an empty string to store the text
    text = ""

    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Extract text from the page
        text += page.get_text()

    # Close the PDF file
    pdf_document.close()

    # Save the extracted text to a text file
    with open(text_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

# Example usage
pdf_file_path = "C:/Users/ogarz/Downloads/First Aid Step 1.pdf"
text_output_path = "C:/Users/ogarz/Downloads/First_Aid_Step1.txt"
pdf_to_text(pdf_file_path, text_output_path)

