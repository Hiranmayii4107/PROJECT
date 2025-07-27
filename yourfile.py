Password Strength Analyzer with Custom Wordlist Generator
Objective: Build a tool to analyze password strength and generate custom wordlists.
Tools: Python, argparse, NLTK, zxcvbn

First step I did was set up the environment
Opened terminal and gave in "pip install zxcvbn nltk tkinter argparse"

Next I gave the code in python
from zxcvbn import zxcvbn

def analyze_password(password):
    result = zxcvbn(password)
    print(f"Password: {password}")
    print(f"Score (0-4): {result['score']}")
    print(f"Crack Time (online fast): {result['crack_times_display']['online_no_throttling_10_per_second']}")
    print(f"Feedback: {result['feedback']}")
    return result

Next I generated custom word lists:
import itertools

def leetspeak_variants(word):
    mapping = str.maketrans("aeios", "43105")
    return [word, word.translate(mapping)]

def generate_wordlist(name, year, pet):
    base_words = [name, pet, year]
    variants = []
    for word in base_words:
        variants.extend(leetspeak_variants(word))
    # Combine pairs
    combos = [''.join(p) for p in itertools.permutations(base_words, 2)]
    return list(set(variants + combos))


Next, I exported wordlist:
def save_wordlist(words, filename="wordlist.txt"):
    with open(filename, "w") as f:
        for w in words:
            f.write(w + "\n")
    print(f"Wordlist saved as {filename}")


Next I added  CLI (argparse):
import argparse

def main():
    parser = argparse.ArgumentParser(description="Password Analyzer & Wordlist Generator")
    parser.add_argument("--password", help="Password to analyze")
    parser.add_argument("--name", help="User's name", default="")
    parser.add_argument("--year", help="Year", default="")
    parser.add_argument("--pet", help="Pet name", default="")
    args = parser.parse_args()

    if args.password:
        analyze_password(args.password)
    words = generate_wordlist(args.name, args.year, args.pet)
    save_wordlist(words)

if __name__ == "__main__":
    main()


Next, I went for a basic GUI:
import tkinter as tk
from tkinter import filedialog, messagebox

def run_gui():
    def process():
        pw = entry_pw.get()
        name = entry_name.get()
        year = entry_year.get()
        pet = entry_pet.get()
        analyze_password(pw)
        words = generate_wordlist(name, year, pet)
        save_wordlist(words)
        messagebox.showinfo("Done", "Password analyzed & Wordlist saved!")

    root = tk.Tk()
    root.title("Password Analyzer")

    tk.Label(root, text="Password:").grid(row=0, column=0)
    entry_pw = tk.Entry(root, show="*"); entry_pw.grid(row=0, column=1)
    tk.Label(root, text="Name:").grid(row=1, column=0)
    entry_name = tk.Entry(root); entry_name.grid(row=1, column=1)
    tk.Label(root, text="Year:").grid(row=2, column=0)
    entry_year = tk.Entry(root); entry_year.grid(row=2, column=1)
    tk.Label(root, text="Pet:").grid(row=3, column=0)
    entry_pet = tk.Entry(root); entry_pet.grid(row=3, column=1)
    tk.Button(root, text="Analyze & Generate", command=process).grid(row=4, column=1)

    root.mainloop()

if __name__ == "__main__":
    run_gui()


Completed with a whole working model.