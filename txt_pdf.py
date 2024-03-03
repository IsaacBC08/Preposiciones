from fpdf import FPDF

def convertir(archivo):
    pdf = FPDF()
    pdf.add_page()
    for texto in archivo:
        if len(texto) <= 20:
            pdf.set_font("Arial", "B", size= 18)
            pdf.cell(w=200,h=10,txt=texto,ln=1,align="C")
        else:            
            pdf.set_font("Arial", size= 15)
            pdf.multi_cell(w=0,h=10,txt=texto,align="L")
    pdf.output("out/tabla_verdad.pdf")
    print("Todo correcto!")