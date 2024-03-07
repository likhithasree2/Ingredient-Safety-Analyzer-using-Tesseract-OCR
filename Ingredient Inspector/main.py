import cv2
import pytesseract
import openpyxl
import tkinter as tk
from tkinter import filedialog
import wikipedia
from tkinter import ttk

wb = openpyxl.load_workbook('harmful_ingredients.xlsx')
sheet = wb.active

harmful_ingredients = {}

def fetch_wikipedia_definition(ingredient):
    try:
        return wikipedia.summary(ingredient, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=2)
    except (wikipedia.exceptions.PageError, wikipedia.exceptions.WikipediaException):
        return None

def check_safety(product_text):
    unsafe_ingredients = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        ingredient, _ = row
        if ingredient.lower() in product_text.lower():
            unsafe_ingredients.append(ingredient.lower())
    return unsafe_ingredients

def process_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])

    if not file_path:
        result_label.config(text="No image selected", fg="#FF5733")
    else:
        image = cv2.imread(file_path)
        product_text = pytesseract.image_to_string(image)
        unsafe_ingredients = check_safety(product_text)
        if unsafe_ingredients:
            result_text = "The Product is Not Recommended due to UNSAFE Ingredients."
            result_label.config(text=result_text, fg="#FF5733", font=("Arial", 18, "bold"), justify="center")

            definitions_text = ""
            for idx, ingredient in enumerate(unsafe_ingredients, start=1):
                definition = fetch_wikipedia_definition(ingredient)
                if definition:
                    definitions_text += f"\n\n{idx}. {ingredient.capitalize()}:\n{definition}"
                else:
                    definitions_text += f"\n\n{idx}. {ingredient.capitalize()}:\nDefinition not found."
            definitions_label.config(text=definitions_text, fg="black", font=("Arial", 14), justify="left", wraplength=600)
        else:
            result_label.config(text="The Product is SAFE to Use. All Ingredients are Safe.", fg="#2ECC71", font=("Arial", 18, "bold"), justify="center")
            definitions_label.config(text="", fg="black")

window = tk.Tk()
window.title("Ingredient Inspector")
window.geometry("800x600")
window.configure(bg="#ECF0F1")

header_frame = tk.Frame(window, bg="#3498DB")
header_frame.pack(fill="x")

content_frame = tk.Frame(window, bg="#ECF0F1")
content_frame.pack(fill="both", expand=True, padx=50, pady=30)

title_label = tk.Label(header_frame, text="Ingredient Inspector", font=("Helvetica", 28, "bold"), bg="#3498DB", fg="white")
title_label.pack(pady=20, padx=20, anchor="nw")

upload_label = tk.Label(content_frame, text="Please upload your image here:", font=("Helvetica", 14), bg="#ECF0F1", fg="#34495E")
upload_label.pack()

tk.Label(content_frame, text="", bg="#ECF0F1").pack(pady=10)

upload_button = ttk.Button(content_frame, text="Upload Image", command=process_image, style="TButton")
upload_button.pack()

tk.Label(content_frame, text="", bg="#ECF0F1").pack(pady=20)

result_label = tk.Label(content_frame, text="", bg="#ECF0F1", justify="center")
result_label.pack(pady=20)

definitions_label = tk.Label(content_frame, text="", bg="#ECF0F1", justify="left", wraplength=600, font=("Arial", 16, "bold"))
definitions_label.pack(pady=20)

style = ttk.Style()
style.configure("TButton", padding=10, relief="flat", background="#2E86C1", foreground="black", font=("Helvetica", 16))

window.mainloop()
