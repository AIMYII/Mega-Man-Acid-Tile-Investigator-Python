from tkinter import *
from PIL import  ImageTk,Image

def open():
    root = Tk()
    root.title("Hexadecimal to decimal converter output")
    root.geometry("600x400")
    #root = Toplevel()
    # root.iconbitmap()

    hexa_value = Entry(root, width=50)
    hexa_value.pack()
    hexa_value.insert(0, "Enter any hexa value - Only allowed 0-9 and A-F: ")

    # def hexa_to_decimal(hexValue):
    #     conversion_table = {
    #         "0": 0, "1": 1, "2": 2, "3": 3,
    #         "4": 4, "5": 5, "6": 6, "7": 7,
    #         "8": 8, "9": 9, "A": 10, "B": 11,
    #         "C": 12, "D": 13, "E": 14, "F": 15
    #     }
    #     position = len(hexValue) - 1
    #     decimal_number = 0
    #
    #     for x in hexValue:
    #         decimal_number += conversion_table[x] * pow(16, position)
    #         position -= 1
    #
    #     return decimal_number
    #
    #     output = hexa_to_decimal(hexa_value)
    #     print("Decimal value:", output)


    # def hex_brute_force_system(hex_target):
    #     # Standardise target: remove prefix and make lowercase
    #     target = hex_target.lower().replace("0x", "")
    #     target_hex = hexa_value.get()
    #
    #     # Start the "brute force" counter
    #     i = 0
    #     while True:
    #         # Check if the hex version of our current number matches the target
    #         if hex(i)[2:] == target:
    #             hex_i = hex(1)[2:]
    #             printhextodec = f"Attempting: Decimal {i} -> Hex {hex_i.upper()}"
    #             printhextodecLabel = Label(root, text=printhextodec)
    #             printhextodecLabel.pack()
    #
    #             if hex_i == target:
    #                 return i
    #             i += 1
    #
    # # User Input
    # target_hex = "1A2B"
    # decimal_result = hex_brute_force_system(target_hex)

    # def myClick():
    #     completetext = "Brute force complete!"
    #     completetextLabel = Label(root, text=completetext)
    #     completetextLabel.pack()

    #hextargettext = f"Hex Target: {target_hex}"
    #hextargettext = Label(root, text=hextargettext)
    # hextargettext.pack()

   # decimalmatchtext = f"Decimal Match: {decimal_result}"
   # decimalmatchtext = Label(root, text=decimalmatchtext)
   # decimalmatchtext.pack()

    btn = Button(root, text="Close second window", command=root.destroy)
    btn.pack()

    mainloop()