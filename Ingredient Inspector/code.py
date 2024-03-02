import cv2
import pytesseract
import openpyxl
import tkinter as tk
from tkinter import filedialog

# Load the XLSX file with harmful ingredients and safety percentages
wb = openpyxl.load_workbook('harmful_ingredients.xlsx')
sheet = wb.active

# Create a list to store the harmful ingredients
harmful_ingredients = []

# Iterate through the rows in the XLSX file
for row in sheet.iter_rows(min_row=2, values_only=True):
    ingredient, safety_percentage = row
    harmful_ingredients.append((ingredient.lower(), safety_percentage))

# Function to check if a product is safe or unsafe
def check_safety(product_text):
    for ingredient, _ in harmful_ingredients:
        if ingredient in product_text.lower():
            return "The Product Ingredients are NOT SAFE"
    return "The Product Ingredients are SAFE"

# Function to open the file dialog and process the image
def process_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])

    if not file_path:
        result_label.config(text="No image selected", fg="red")
    else:
        image = cv2.imread(file_path)
        product_text = pytesseract.image_to_string(image)
        safety_result = check_safety(product_text)
        result_label.config(text=safety_result, fg="red" if "NOT SAFE" in safety_result else "green")

# Create the main window
window = tk.Tk()
window.title("Ingredient Inspector")

# Set window dimensions
window.geometry("800x400")

# Create frames to style different sections
header_frame = tk.Frame(window, bg="#87CEFA")  # Light blue for the header
header_frame.pack(fill="x")

content_frame = tk.Frame(window, bg="#E6E6FA")  # Light purple for the content
content_frame.pack(fill="both", expand=True)

# Create a label with the title in the header frame
title_label = tk.Label(header_frame, text="Ingredient Inspector", font=("Arial", 28), bg="#87CEFA")
title_label.pack(pady=20)

# Add a label for the upload instructions in the content frame
upload_label = tk.Label(content_frame, text="Please upload your image here", font=("Arial", 14), bg="#E6E6FA")
upload_label.pack()

# Create a button for uploading images in the content frame
upload_button = tk.Button(content_frame, text="Upload Image", command=process_image, bg="#0073e6", fg="white", font=("Arial", 16))
upload_button.pack(pady=20)

# Create a label to display the result in the content frame
result_label = tk.Label(content_frame, text="", font=("Arial", 20), bg="#E6E6FA")
result_label.pack()

# Start the GUI event loop
window.mainloop()
