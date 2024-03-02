## Overview:
Ingredient Inspector is a Python application designed to assist users in determining the safety of product ingredients by comparing them to a predefined list of harmful ingredients. 
The application utilizes image processing techniques to extract text from images containing product ingredient lists, which are then cross-referenced with a database of harmful ingredients 
stored in an Excel spreadsheet.

## Features:
Image Upload: Users can upload images containing product ingredient lists.
Text Extraction: The application utilizes the Tesseract OCR engine to extract text from uploaded images.
Safety Check: The extracted text is compared against a list of harmful ingredients from the 'harmful_ingredients.xlsx' file to determine the product's safety.
User-Friendly Interface: The application provides a simple and intuitive graphical user interface using the Tkinter library.

## Prerequisites:
Before running the application, ensure you have the following dependencies installed:
Python: The application is developed in Python 3.10
OpenCV(4.5.4.60): OpenCV (cv2) is used for image processing tasks. Please install it using pip install opencv-python.
Pytesseract(0.3.10): Pytesseract is a Python wrapper for Google's Tesseract OCR engine. Please install it using pip install pytesseract.
Openpyxl(3.1.2): Openpyxl is used for reading data from Excel files. Install it using pip install openpyxl.
Tkinter: Tkinter is Python's de-facto standard GUI (Graphical User Interface) package. It should be included with most Python installations.
Note: Download Tesseract from Github: https://github.com/UB-Mannheim/tesseract/wiki --> Download the .exe file and set the path in system environment variables, then check tessseract --version in cmd.

*Clone or download the repository to your local machine.*

## Usage
1. Run the `code.py` file.
2. Click on the "Upload Image" button and select an image file containing the product ingredient list.
3. Wait for the application to process the image and display the safety result.

## File Structure
- `code.py`: Main Python script containing the GUI application logic.
- `harmful_ingredients.xlsx`: Excel file containing harmful ingredients and safety percentages. Column 1: Ingredient Names, Column 2: Safety Percentage
- `README.md`: README file containing information about the application.

## Contributing
Contributions are welcome! Please feel free to open issues or pull requests for any improvements or bug fixes.


