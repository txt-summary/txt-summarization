# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
# Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

# NLP Pkgs
from spacy_summarization import text_summarizer
from gensim.summarization import summarize
from nltk_summarization import nltk_summarizer
from sumy_summarization import sumy_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Structure and Layout
window = Tk()
window.title(" Text Summarizer ")
window.geometry("900x800")
window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn',)


# TAB LAYOUT
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^40s}')
tab_control.add(tab2, text=f'{"File":^40s}')
tab_control.add(tab3, text=f'{"URL":^40s}')
tab_control.add(tab4, text=f'{"Comparer ":^40s}')
tab_control.add(tab5, text=f'{"About ":^40s}')


label1 = Label(tab1, font="h1", text='Text Summarizer', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, font="h1", text='File Processing', padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, font="h1", text='URL', padx=5, pady=5)
label3.grid(column=0, row=0)

label3 = Label(tab4, font="h1", text='Compare Summarizers', padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab5, font="h1", text='About', padx=5, pady=5)
label4.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')


# Functions
def get_summary():
    raw_text = str(entry.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSummary:{}'.format(final_text)
    tab1_display.insert(tk.END, result)


# Clear entry widget
def clear_text():
    entry.delete('1.0', END)


def clear_display_result():
    tab1_display.delete('1.0', END)


# Clear Text  with position 1.0
def clear_text_file():
    displayed_file.delete('1.0', END)

# Clear Result of Functions


def clear_text_result():
    tab2_display_text.delete('1.0', END)

# Clear For URL


def clear_url_entry():
    url_entry.delete(0, END)


def clear_url_display():
    tab3_display_text.delete('1.0', END)


# Clear entry widget
def clear_compare_text():
    entry1.delete('1.0', END)


def clear_compare_display_result():
    tab1_display.delete('1.0', END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
    file1 = tkinter.filedialog.askopenfilename(
        filetypes=(("Text Files", ".txt"), ("All files", "*")))
    read_text = open(file1).read()
    displayed_file.insert(tk.END, read_text)


def get_file_summary():
    raw_text = displayed_file.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab2_display_text.insert(tk.END, result)

# Fetch Text From Url


def get_text():
    raw_text = str(url_entry.get())
    page = urlopen(raw_text)
    soup = BeautifulSoup(page, features="lxml")
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    url_display.insert(tk.END, fetched_text)


def get_url_summary():
    raw_text = url_display.get('1.0', tk.END)
    final_text = text_summarizer(raw_text)
    result = '\nSummary:{}'.format(final_text)
    tab3_display_text.insert(tk.END, result)


# COMPARER FUNCTIONS
def use_spacy():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSpacy Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_nltk():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = nltk_summarizer(raw_text)
    print(final_text)
    result = '\nNLTK Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_gensim():
    raw_text = str(entry1.get('1.0', tk.END))
    final_text = summarize(raw_text)
    print(final_text)
    result = '\nGensim Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


def use_sumy():
    raw_text = str(entry1.get('1.0', tk.END))
    # 26/5
    # final_text = text_summarizer(raw_text)
    final_text = sumy_summarizer(raw_text)
    print(final_text)
    result = '\nSumy Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


# MAIN NLP TAB
def main_tab_entry_update(event):
    entry_var.set("Original Word Count: " +
                  str(len(entry.get("1.0", 'end-1c'))))


entry_var = StringVar()

og_word_count_main_tab = Label(tab1, textvariable=entry_var)
og_word_count_main_tab.grid(row=1, column=1)

l1 = Label(tab1, text="Enter Text To Summarize: ")
l1.grid(row=1, column=0)

entry = Text(tab1, wrap=WORD, height=18)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

entry.bind("<KeyRelease>", main_tab_entry_update)


# BUTTONS
button1 = Button(tab1, text="Reset", command=clear_text,
                 width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Summarize", command=get_summary,
                 width=12, bg='blue', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab1, text="Clear Result",
                 command=clear_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab1, text="Main Points", width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result


def main_tab_result_update(event):
    tab1_display_var.set("Summary Word Count: " +
                         str(len(tab1_display.get("1.0", 'end-1c'))))


tab1_display_var = StringVar()

summ_word_count_main_tab = Label(tab1, textvariable=tab1_display_var)
summ_word_count_main_tab.grid(row=6, column=1)

tab1_display = Text(tab1, wrap=WORD, height=18)
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

tab1_display.bind("<KeyRelease>", main_tab_result_update)

# FILE PROCESSING TAB


def file_tab_entry_update(event):
    displayed_file_var.set("Original Word Count: " +
                           str(len(displayed_file.get("1.0", 'end-1c'))))


displayed_file_var = StringVar()

l1 = Label(tab2, text="Open File To Summarize")
l1.grid(row=1, column=0)

og_word_count_file_tab = Label(tab2, textvariable=displayed_file_var)
og_word_count_file_tab.grid(row=1, column=1)

displayed_file = ScrolledText(
    tab2, wrap=WORD, height=17)  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

displayed_file.bind("<KeyRelease>", file_tab_entry_update)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0 = Button(tab2, text="Open File", width=12, command=openfiles, bg='#c5cae9')
b0.grid(row=3, column=0, padx=10, pady=10)

b1 = Button(tab2, text="Reset ", width=12,
            command=clear_text_file, bg="#b9f6ca")
b1.grid(row=3, column=1, padx=10, pady=10)

b2 = Button(tab2, text="Summarize", width=12,
            command=get_file_summary, bg='blue', fg='#fff')
b2.grid(row=3, column=2, padx=10, pady=10)

b3 = Button(tab2, text="Clear Result", width=12, command=clear_text_result)
b3.grid(row=5, column=1, padx=10, pady=10)

b4 = Button(tab2, text="Close", width=12, command=window.destroy)
b4.grid(row=5, column=2, padx=10, pady=10)

# Display Screen


def file_tab_result_update(event):
    tab2_display_text_var.set("Summary Word Count: " +
                              str(len(tab2_display_text.get("1.0", 'end-1c'))))


tab2_display_text_var = StringVar()

summ_word_count_file_tab = Label(tab2, textvariable=tab2_display_text_var)
summ_word_count_file_tab.grid(row=6, column=1)

tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, wrap=WORD, height=17)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

tab2_display_text.bind("<KeyRelease>", file_tab_result_update)

# URL TAB
l1 = Label(tab3, text="Enter URL To Summarize")
l1.grid(row=1, column=0)

raw_entry = StringVar()
url_entry = Entry(tab3, textvariable=raw_entry, width=50)
url_entry.grid(row=1, column=1)

# BUTTONS
button1 = Button(tab3, text="Reset", command=clear_url_entry,
                 width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab3, text="Get Text", command=get_text,
                 width=12, bg='#03A9F4', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab3, text="Clear Result",
                 command=clear_url_display, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab3, text="Summarize", command=get_url_summary,
                 width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For URL Result


def url_tab_entry_update(event):
    url_display_var.set("Original Word Count: " +
                        str(len(url_display.get("1.0", 'end-1c'))))


url_display_var = StringVar()

og_word_count_url_tab = Label(tab3, textvariable=url_display_var)
og_word_count_url_tab.grid(row=6, column=1)

url_display = ScrolledText(tab3, wrap=WORD, height=18)
url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

url_display.bind("<KeyRelease>", url_tab_entry_update)

# Display Screen For URL Summary Result


def url_tab_summary_update(event):
    tab3_display_text_var.set("Summary Word Count: " +
                              str(len(tab3_display_text.get("1.0", 'end-1c'))))


tab3_display_text_var = StringVar()

summ_word_count_url_tab = Label(tab3, textvariable=tab3_display_text_var)
summ_word_count_url_tab.grid(row=8, column=1)

tab3_display_text = ScrolledText(tab3, height=18)
tab3_display_text.grid(row=10, column=0, columnspan=3, padx=5, pady=5)

tab3_display_text.bind("<KeyRelease>", url_tab_summary_update)


# COMPARER TAB
def comparer_tab_entry_update(event):
    entry1_var.set("Original Word Count: " +
                   str(len(entry1.get("1.0", 'end-1c'))))


entry1_var = StringVar()

og_word_count_comparer_tab = Label(tab4, textvariable=entry1_var)
og_word_count_comparer_tab.grid(row=1, column=2)

l1 = Label(tab4, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry1 = ScrolledText(tab4, wrap=WORD, height=18)
entry1.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

entry1.bind("<KeyRelease>", comparer_tab_entry_update)

# BUTTONS
button1 = Button(tab4, text="Reset", command=clear_compare_text,
                 width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab4, text="SpaCy", command=use_spacy,
                 width=12, bg='red', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab4, text="Clear Result",
                 command=clear_compare_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab4, text="NLTK", command=use_nltk,
                 width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=4, column=2, padx=10, pady=10)

button4 = Button(tab4, text="Gensim", command=use_gensim,
                 width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

button4 = Button(tab4, text="Sumy", command=use_sumy,
                 width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=2, padx=10, pady=10)


variable = StringVar()
variable.set("SpaCy")
choice_button = OptionMenu(tab4, variable, "SpaCy", "Gensim", "Sumy", "NLTK")
choice_button.grid(row=6, column=1)


# Display Screen For Result
def comparer_tab_summary_update(event):
    tab4_display_var.set("Summary Word Count: " +
                         str(len(tab4_display.get("1.0", 'end-1c'))))


tab4_display_var = StringVar()

summ_word_count_summary_tab = Label(
    tab4, textvariable=tab4_display_var)

summ_word_count_summary_tab.grid(row=6, column=2)

tab4_display = ScrolledText(tab4, wrap=WORD, height=18)
tab4_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

tab4_display.bind("<KeyRelease>", comparer_tab_summary_update)

# About TAB
about_label = Label(
    tab5, text="Text Summarizer with Deep Learning \n A project by Karan, Vikrant & Anurag", pady=5, padx=5)
about_label.grid(column=0, row=2)

window.mainloop()
