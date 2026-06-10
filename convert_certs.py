import fitz  # PyMuPDF
import os

def convert_pdf_to_png(pdf_filename, output_png_filename):
    # Check if the PDF file exists in your directory
    if not os.path.exists(pdf_filename):
        print(f"⚠️ Error: Could not find file named '{pdf_filename}' in this folder.")
        return

    # Open the PDF document
    doc = fitz.open(pdf_filename)
    
    # Load the first page (index 0)
    page = doc.load_page(0)
    
    # Render the page to a high-quality image matrix (DPI=150 is crisp for text)
    pix = page.get_pixmap(dpi=150)
    
    # Ensure the 'assets' folder exists before saving
    os.makedirs("assets", exist_ok=True)
    
    # Save the target image into the assets folder
    output_path = os.path.join("assets", output_png_filename)
    pix.save(output_path)
    print(f"✅ Successfully converted '{pdf_filename}' -> '{output_path}'")

# --- EXECUTION MAPPING ---
# This matches your exact uploaded file names to clean names inside your assets folder
if __name__ == "__main__":
    conversion_tasks = [
        ("certificate6.pdf", "matlab_onramp.png"),
        ("certificate4.pdf", "vectors_matrices.png"),
        ("certificate3.pdf", "manipulate_matrices.png"),
        ("certificate2.pdf", "matlab_plots.png"),
        ("certificate5.pdf", "ml_onramp.png"),
        ("cer.pdf", "desktop_tools.png"), # 'cer.pdf' and 'certificate.pdf' are identical
        ("certificate 7.pdf", "simulink_fundamentals.png")
    ]

    print("🚀 Starting PDF certificate conversion...")
    for pdf_file, png_file in conversion_tasks:
        convert_pdf_to_png(pdf_file, png_file)
    print("✨ All done! Check your new 'assets' folder.")