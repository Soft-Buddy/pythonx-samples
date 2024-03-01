import PyPDF2

def encrypt_pdf(input_pdf_path, output_pdf_path, password):
    # Open the PDF file in binary mode
    with open(input_pdf_path, 'rb') as pdf_file:
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Add each page from the original PDF to the writer object
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Encrypt the PDF with the provided password
        pdf_writer.encrypt(password)

        # Write the encrypted PDF to the output file
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your input PDF file
    input_pdf_path = 'input.pdf'
    
    # Replace 'output.pdf' with the desired name for the output PDF file
    output_pdf_path = 'output.pdf'
    
    # Replace 'your_password' with the desired password for the PDF
    password = 'your_password'
    
    # Call the function to encrypt the PDF
    encrypt_pdf(input_pdf_path, output_pdf_path, password)
