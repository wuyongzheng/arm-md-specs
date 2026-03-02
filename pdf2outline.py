import sys
import fitz  # PyMuPDF is imported as fitz

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    # Get the table of contents (outline)
    toc = doc.get_toc(simple=False)
    doc.close()
    return toc

# Example usage:
outline = extract_outline(sys.argv[1])
for lvl, title, page, dest in outline:
    if 'to' in dest and dest['to'].y >= 739:
        print(lvl, page, title, sep="\t")
