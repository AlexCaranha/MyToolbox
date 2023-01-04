# Install
# pip install pikepdf

from pikepdf import Pdf

def create_in_memory(pdf_input, pages:list, offset:int):
    pdf_object = Pdf.new()
    
    for page in pages:
        index = page + offset
        page_selected = pdf_input.pages.p(index)
        pdf_object.pages.append(page_selected)
    
    return pdf_object

def save_pdf(pdf_object, filename):
    pdf_object.save(filename)

# a dictionary mapping PDF file to original PDF's page range
file2pages = [
    (12,16),
    (16,24),
    (24,28),
    (28,33),
    (33,40),
    (40,43),
    (43,44),
    (44,48),
    (48,54),
    (54,56),
    (56,66),
    (66,74),
    (74,78),
    (78,79),
    (79,80),
    (80,81),
    (81,83),
    (83,84),
    (84,86),
    (86,88),
    (88,90),
    (90,92),
    (92,96),
    (96,98),
    (98,100),
    (100,104),
    (104,108),
    (108,112),
    (112,119),
    (119,122),
    (122,126),
    (126,135),
    (135,139),
    (139,146),
    (146,150),
    (150,158),
    (158,160),
    (160,166),
    (166,170),
    (170,174),
    (174,178),
    (178,182),
    (182,184),
    (184,190),
    (190,196),
    (196,202),
    (202,204),
    (204,212),
    (212,214),
    (214,220),
    (220,224),
    (224,228),
    (228,232),
    (232,233),
    (233,235),
    (235,236),
    (236,238),
    (238,240),
    (240,242),
    (242,244)
]

# the target PDF document to split
filename = "C:\\Temp\\input.pdf"

# load the PDF file
pdf_input = Pdf.open(filename)

# pages offset
offset = 2

# Iterate over the items in the dictionary
index = 0
for pair in file2pages:
    index += 1
    indice = str(index) if index > 9 else f'0{index}'
    new_pdf_filename = f'{filename.replace(".pdf", "")}_song_{indice}.pdf'
    print(f"processing file: {new_pdf_filename}")
    
    numbers = list(range(pair[0], pair[1]))
    pdf_object = create_in_memory(pdf_input, numbers, offset)
    save_pdf(pdf_object, new_pdf_filename)

print("done!")