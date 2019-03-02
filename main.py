#!/usr/bin/python
#coding: utf-8

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import ParagraphStyle

header_data = ['ID', 'Nome', 'Status']
rows_data = [
            ['1','Teste','Cancelado'],
            ['2','Teste2','Concluído']
          ]

doc = SimpleDocTemplate("export_dir/export.pdf",
                        pagesize=landscape(letter))
# container for the 'Flowable' objects
elements = []

style = ParagraphStyle(
    name='Normal',    
    fontSize=12,
)

elements.append(Paragraph('Relatório criado em: 12/10/2019 às 14:00\n',style))
elements.append(Paragraph('Total de registros: 1040',style))
elements.append(Paragraph('<br/><br/><br/>',style))

t = Table(rows_data)
t.setStyle(TableStyle([('ALIGN', (1, 1), (-2, -2), 'LEFT'),
                       ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                       ('VALIGN', (0, 0), (0, -1), 'TOP'),
                       ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                       ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                       ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                       ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                       ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                       ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                       ]))

elements.append(t)
# write the document to disk
doc.build(elements)
