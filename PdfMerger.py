from PyPDF2 import *
import sys
import os
import emoji

def pdfMerge():
    merger = PdfMerger()
    pdfs=[]
    
    for file in os.listdir():
        
        if file.endswith(".pdf"):
            pdfs.append(file)
    
    if len(pdfs) == 0:
        print("Error!! No pdfs found in specified folder.")
        return
    
    else:
        print("Here is the list of pdfs found: ")

    for index, pdf in enumerate(pdfs):
        index += 1
        print(f"{index}. {pdf}")
    
    choice = input("Would you like to join the pdf files listed above (Yes or No)?\n ")
    
    if choice == "Yes":
        name = input("Please enter a name for the merged file.\n ")
        new_file = name + ".pdf"
        
        for pdf in pdfs:    
            merger.append(pdf)
        
        merger.write(new_file)
        merger.close
        print("SUCCESS!! Have fun reading!!", emoji.emojize(":fountain_pen:"))
        
    elif choice == "No":
        print("We're always here if you need us")
    
    else:
        print(emoji.emojize(":cross_mark:"),"Sorry, the choice you entered is invalid!")
        
    
    print("Goodbye! Come again",emoji.emojize(":handshake:"))
    return


pdfMerge()