## Ingredient-Safety-Analyzer-using-Tesseract-OCR
Ingredient Inspector is a Python application designed to assist users in determining the safety of product ingredients by comparing them to a predefined list of harmful ingredients. 
The application utilizes image processing techniques to extract text from images containing product ingredient lists, which are then cross-referenced with a database of harmful ingredients 
stored in an Excel spreadsheet. Additionally, it fetches definitions for detected harmful ingredients from Wikipedia to provide users with more detailed information.

## Features:
- Image Upload: Users can upload images containing product ingredient lists.
- Text Extraction: The application utilizes the Tesseract OCR engine to extract text from uploaded images.
- Safety Check: The extracted text is compared against a list of harmful ingredients from the 'harmful_ingredients.xlsx' file to determine the product's safety.
- Wikipedia Integration: Definitions for harmful ingredients are fetched from Wikipedia to provide users with detailed information.
- User-Friendly Interface: The application provides a simple and intuitive graphical user interface using the Tkinter library.

## Prerequisites:
Before running the application, ensure you have the following dependencies installed:
- Python 3.10
- OpenCV (cv2) 4.5.4.60: OpenCV is used for image processing tasks. Install using `pip install opencv-python`.
- Pytesseract 0.3.10: Pytesseract is a Python wrapper for Google's Tesseract OCR engine  for optical character recognition (OCR). Install using `pip install pytesseract`.
- Openpyxl 3.1.2: Openpyxl is used for reading data from Excel files. Install using `pip install openpyxl`.
- Wikipedia 1.4.0: Install using `pip install wikipedia`.
- Tkinter: Python's de-facto standard GUI package, included with most Python installations.
- Tesseract OCR Engine: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki), set the path in system environment variables, and verify the installation using `tesseract --version` in the command prompt.

## Usage
1. Clone or download the repository to your local machine.
2. Run the `code.py` file.
3. Click on the "Upload Image" button and select an image file containing the product ingredient list.
4. Wait for the application to process the image and display the safety result along with detailed definitions fetched from Wikipedia for harmful ingredients.

## File Structure
- `code.py`: Main Python script containing the GUI application logic.
- `harmful_ingredients.xlsx`: Excel file containing harmful ingredients and safety percentages. Column 1: Ingredient Names, Column 2: Safety Percentage
- `README.md`: README file containing information about the application.

## Contributing
Contributions are welcome! Please feel free to open issues or pull requests for any improvements or bug fixes.
