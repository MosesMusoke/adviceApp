import docx
from docx.oxml.ns import qn
from docx.shared import Pt

# Create a reference document with Montserrat font for body and headings

doc = docx.Document()

styles = doc.styles

# Set Normal style to Montserrat
normal = styles['Normal']
normal.font.name = 'Montserrat'
normal.font.size = Pt(11)
# Ensure Word uses the font by setting eastAsia
normal.element.rPr.rFonts.set(qn('w:eastAsia'), 'Montserrat')

# Update Heading styles
for level in range(1, 4):
    style_name = f'Heading {level}'
    if style_name in styles:
        s = styles[style_name]
        s.font.name = 'Montserrat'
        s.element.rPr.rFonts.set(qn('w:eastAsia'), 'Montserrat')
        if level == 1:
            s.font.size = Pt(18)
        elif level == 2:
            s.font.size = Pt(14)
        else:
            s.font.size = Pt(12)

# Add a title to ensure styles exist in the template
p = doc.add_paragraph('Reference Template (Montserrat)')
p.style = styles['Title'] if 'Title' in styles else styles['Normal']

# Save the reference docx
output_path = '/workspace/docs/reference-montserrat.docx'
doc.save(output_path)
print(f'Wrote {output_path}')