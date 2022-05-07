# Python Code to create barcodes from Student Number and Name

import qrcode
from PIL import Image
from barcode import Code39
from barcode.writer import ImageWriter

num = input('Enter Code: \n')
name = input("Enter Student Name: \n")

numCode = Code39(num, add_checksum=False, writer = ImageWriter())

print(numCode)
choice = input('Confirm (y/n)?')

if choice == 'y':
    numCode.save(name)
