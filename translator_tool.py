import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator
import pyttsx3

translator = Translator()
tts_engine = pyttsx3.init()

def translate_text():
    src_lang = source_lang.get()
    tgt_lang = target_lang.get()
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showwarning("Input Needed", "Please enter some text to translate.")
        return

    try:
        translated = translator.translate(text, src=src_lang, dest=tgt_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed.\n{e}")

def copy_text():
    output = output_text.get("1.0", tk.END).strip()
    if output:
        root.clipboard_clear()
        root.clipboard_append(output)
        messagebox.showinfo("Copied", "Translated text copied to clipboard.")

def speak_text():
    output = output_text.get("1.0", tk.END).strip()
    if output:
        tts_engine.say(output)
        tts_engine.runAndWait()

root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")

tk.Label(root, text="Enter Text:").pack()
input_text = tk.Text(root, height=5)
input_text.pack()

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="From:").grid(row=0, column=0)
source_lang = ttk.Combobox(frame, values=["en", "fr", "es", "hi", "ta", "te"], width=10)
source_lang.set("en")
source_lang.grid(row=0, column=1, padx=10)

tk.Label(frame, text="To:").grid(row=0, column=2)
target_lang = ttk.Combobox(frame, values=["en", "fr", "es", "hi", "ta", "te"], width=10)
target_lang.set("fr")
target_lang.grid(row=0, column=3, padx=10)

translate_btn = tk.Button(root, text="Translate", command=translate_text)
translate_btn.pack(pady=5)

tk.Label(root, text="Translated Text:").pack()
output_text = tk.Text(root, height=5)
output_text.pack()

options_frame = tk.Frame(root)
options_frame.pack(pady=5)
tk.Button(options_frame, text="Copy", command=copy_text).grid(row=0, column=0, padx=10)
tk.Button(options_frame, text="Speak", command=speak_text).grid(row=0, column=1, padx=10)

root.mainloop()
