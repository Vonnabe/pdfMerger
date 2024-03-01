import PyPDF2
import sys
import os 

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        #merger = PyPDF2.PdfMerger()
        merger.append(file)
merger.write("mergedFile.pdf")

print(file)
