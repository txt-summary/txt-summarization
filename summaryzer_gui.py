# Core Packages
# Import Heapq for Finding the Top N Sentences
# from nltk_summarization import nltk_summarizer
# from spacy_summarization import text_summarizer
import heapq
from gensim.summarization import summarize
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
from heapq import nlargest
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
# Pkgs for Normalizing Text
import spacy
nlp = spacy.load('en')

# NLP Pkgs
# text_summarizer


def text_summarizer(raw_docx):
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency # word.text is tokenization in spacy
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [sentence for sentence in docx.sents]

    # Sentence Scores
    sentence_scores = {}
    for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    summarized_sentences = nlargest(
        7, sentence_scores, key=sentence_scores.get)
    final_sentences = [w.text for w in summarized_sentences]
    summary = ' '.join(final_sentences)
    return summary

# nltk_summarizer


def nltk_summarizer(raw_text):
    stopWords = set(stopwords.words("english"))
    word_frequencies = {}
    for word in nltk.word_tokenize(raw_text):
        if word not in stopWords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_list = nltk.sent_tokenize(raw_text)
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(
        7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return summary


# Web Scraping Pkg

# Structure and Layout
window = Tk()
window.title(" Text Summarizer GUI")
window.geometry("1000x800")
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
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab3, text=f'{"URL":^20s}')
tab_control.add(tab4, text=f'{"Comparer ":^20s}')
tab_control.add(tab5, text=f'{"About ":^20s}')


label1 = Label(tab1, text='Summaryzer', padx=5, pady=5)
label1.grid(column=0, row=0)

label2 = Label(tab2, text='File Processing', padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab3, text='URL', padx=5, pady=5)
label3.grid(column=0, row=0)

label3 = Label(tab4, text='Compare Summarizers', padx=5, pady=5)
label3.grid(column=0, row=0)

label4 = Label(tab5, text='About', padx=5, pady=5)
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
    soup = BeautifulSoup(page)
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
    final_text = text_summarizer(raw_text)
    print(final_text)
    result = '\nSumy Summary:{}\n'.format(final_text)
    tab4_display.insert(tk.END, result)


# MAIN NLP TAB
l1 = Label(tab1, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry = Text(tab1, height=10)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# BUTTONS
button1 = Button(tab1, text="Reset", command=clear_text,
                 width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Summarize", command=get_summary,
                 width=12, bg='#ced', fg='#fff')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab1, text="Clear Result",
                 command=clear_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)

button4 = Button(tab1, text="Main Points", width=12, bg='#03A9F4', fg='#fff')
button4.grid(row=5, column=1, padx=10, pady=10)

# Display Screen For Result
tab1_display = Text(tab1)
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


# FILE PROCESSING TAB
l1 = Label(tab2, text="Open File To Summarize")
l1.grid(row=1, column=1)

displayed_file = ScrolledText(tab2, height=7)  # Initial was Text(tab2)
displayed_file.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

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
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2, height=10)
tab2_display_text.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)


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

# Display Screen For Result
url_display = ScrolledText(tab3, height=10)
url_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


tab3_display_text = ScrolledText(tab3, height=10)
tab3_display_text.grid(row=10, column=0, columnspan=3, padx=5, pady=5)


# COMPARER TAB
l1 = Label(tab4, text="Enter Text To Summarize")
l1.grid(row=1, column=0)

entry1 = ScrolledText(tab4, height=10)
entry1.grid(row=2, column=0, columnspan=3, padx=5, pady=3)

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
tab4_display = ScrolledText(tab4, height=15)
tab4_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)


# About TAB
about_label = Label(
    tab5, text="Text Summarizer with Deep Learning \n A project by Karan, Vikrant & Anurag", pady=5, padx=5)
about_label.grid(column=0, row=1)

window.mainloop()
