# --- Abrindo um arquivo PDF em Python

from pathlib import Path
import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'

leitor_pdf = pypdf.PdfReader(caminho_pdf)

print(leitor_pdf.pages)  # Lista contendo as páginas
print(len(leitor_pdf.pages))  # Número de páginas
print(leitor_pdf.pages[0])  # Primeira página


print(leitor_pdf.metadata)  # Metadados
print(leitor_pdf.metadata.creation_date)  # Acessando metadado
print(leitor_pdf.metadata.author)  # Acessando metadado inexistente
