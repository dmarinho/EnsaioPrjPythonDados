# --- Ver todas as imagens de um PDF
from pathlib import Path

import pypdf

caminho_pdf = Path('H:\\_diogenes_\\queiroz&cavalcante\\ged_queiroz\\ged_queiroz\Administração Judicial - PE\\0037079-45.2012.8.17.0001\\8410197 - 6 Ata AGC Butiá 04042014 plano aprovado.pdf.pdf')
leitor_pdf = pypdf.PdfReader(caminho_pdf)

for page in leitor_pdf.pages:
    for obj_imagem in page.images:
       with open('img.png','wb') as arquivos_imagem:
            arquivos_imagem.write(obj_imagem.data)



# # --- Extrair texto de um PDF nem sempre é infalível!

# from pathlib import Path

# import pypdf

# caminho_pdf = Path('H:\\_diogenes_\\queiroz&cavalcante\\ged_queiroz\\ged_queiroz\Administração Judicial - PE\\0037079-45.2012.8.17.0001\\8410197 - 6 Ata AGC Butiá 04042014 plano aprovado.pdf.pdf')
# leitor_pdf = pypdf.PdfReader(caminho_pdf)

# for i, pagina in enumerate(leitor_pdf.pages, 1):
#     print(f' ---------- Página {i:2d}')
#     print(pagina.extract_text())
#     input()


# --- Dificuldades de ler arquivos com formatação

# from pathlib import Path

# import pypdf

# caminho_pdf = Path('materiais de aula') / 'documentos' / 'RI Ambev - 1T23.pdf'
# leitor_pdf = pypdf.PdfReader(caminho_pdf)

# for i, pagina in enumerate(leitor_pdf.pages, 1):
#     print(f' ---------- Página {i:2d}')
#     print(pagina.extract_text())
#     input()
