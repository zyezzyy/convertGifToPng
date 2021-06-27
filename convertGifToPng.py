import os
import tkinter
from tkinter import StringVar, filedialog, END
from PIL import Image, ImageSequence
import constString

root = tkinter.Tk()
root.title(constString.get_item("item001"))
# root.iconbitmap("xxx.ico")
root.geometry("500x400")
root.resizable(1, 1)


# bg_color = "#f5cf87"
# root.config(bg=bg_color)

def select_gif():
    gif_file_path = filedialog.askopenfilename(initialdir='./', filetypes=(('Gif', '.gif'), ('All files', '*.*')))
    if gif_file_path == "":
        pass
    else:
        input_textbox.delete(0, END)
        input_textbox.insert(0, gif_file_path)


def select_output_folder():
    folder_path = filedialog.askdirectory(initialdir='./')
    if folder_path == "":
        pass
    else:
        output_textbox.delete(0, END)
        output_textbox.insert(0, folder_path)


def convertGIF():
    gif_file_path = input_textbox.get()
    output_folder_path = output_textbox.get()

    if os.path.isfile(gif_file_path) and \
            os.path.isdir(output_folder_path):
        pass
    else:
        return False

    gif_file = Image.open(gif_file_path)
    file_name = os.path.basename(gif_file_path)
    file_name = file_name.split('.')[0]

    output_folder_path = output_folder_path + os.sep + file_name
    mkdir(output_folder_path)

    gif_iter = ImageSequence.Iterator(gif_file)
    index = 1
    for png in gif_iter:
        # print("image %d: mode %s, size %s" % (index, pgn.mode, png.size))
        png.save(output_folder_path + os.sep + "%s%04d.png" % (file_name, index))
        index += 1


def mkdir(folder_path):
    if os.path.exists(folder_path):
        pass
    else:
        os.makedirs(folder_path)


language_choice = StringVar()
language_choice.set(constString.default_language)
language_list = constString.get_language_list()

language_label = tkinter.Label(root, text=constString.get_item("item002"))
language_label_list = tkinter.OptionMenu(root, language_choice, *language_list)

input_label = tkinter.Label(root, text=constString.get_item("item003"))
input_textbox = tkinter.Entry(root)
input_button = tkinter.Button(root, text=constString.get_item("item004"), command=select_gif)

output_label = tkinter.Label(root, text=constString.get_item("item005"))
output_textbox = tkinter.Entry(root)
output_button = tkinter.Button(root, text=constString.get_item("item004"), command=select_output_folder)

parse_button = tkinter.Button(root, text=constString.get_item("item006"), command=convertGIF)

language_label.grid(row=0, column=0)
language_label_list.grid(row=0, column=1)

input_label.grid(row=1, column=0)
input_textbox.grid(row=1, column=1)
input_button.grid(row=1, column=2)

output_label.grid(row=2, column=0)
output_textbox.grid(row=2, column=1)
output_button.grid(row=2, column=2)

parse_button.grid(row=3, column=1)

root.mainloop()
