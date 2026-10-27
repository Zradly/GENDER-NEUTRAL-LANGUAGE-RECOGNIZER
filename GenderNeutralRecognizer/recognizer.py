

import re
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk

TERMS = {
    "chairman": "chairperson",
    "policeman": "police officer",
    "fireman": "firefighter",
    "stewardess": "flight attendant",
    "mankind": "humankind",
    "salesman": "salesperson",
    "businessman": "businessperson",
    "waitress": "server",
    "manpower": "workforce",
    "man-made": "artificial",
}


def analyze_text(text):
    """Return (term, occurrence_count, suggestion) for every term found."""
    results = []
    for term, suggestion in TERMS.items():
        
        pattern = re.compile(
            rf"(?<!\w){re.escape(term)}(?!\w)",
            re.IGNORECASE,
        )
        count = sum(1 for _ in pattern.finditer(text))
        if count:
            results.append((term, count, suggestion))
    return results


class RecognizerApp:
    def __init__(self, root):
        self.root = root
        root.title("Gender Neutral Language Recognizer")
        root.geometry("760x460")
        root.minsize(620, 360)

        ttk.Label(
            root,
            text="Gender Neutral Language Recognizer",
            font=("Arial", 16, "bold"),
        ).pack(pady=(16, 8))

        ttk.Button(root, text="Open a .txt file", command=self.open_file).pack()
        self.file_label = ttk.Label(root, text="No file selected")
        self.file_label.pack(pady=(8, 2))
        self.status_label = ttk.Label(root, text="Choose a text file to begin.")
        self.status_label.pack(pady=(2, 10))

        columns = ("term", "count", "suggestion")
        self.table = ttk.Treeview(root, columns=columns, show="headings", height=12)
        self.table.heading("term", text="Detected term")
        self.table.heading("count", text="Occurrences")
        self.table.heading("suggestion", text="Suggested alternative")
        self.table.column("term", width=220)
        self.table.column("count", width=120, anchor="center")
        self.table.column("suggestion", width=300)

        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        self.table.pack(side="left", fill="both", expand=True, padx=(16, 0), pady=(0, 16))
        scrollbar.pack(side="right", fill="y", padx=(0, 16), pady=(0, 16))

    def open_file(self):
        file_path = filedialog.askopenfilename(
            title="Choose a text file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if not file_path:
            return

        path = Path(file_path)
        if path.suffix.lower() != ".txt":
            messagebox.showerror("Unsupported file", "Please choose a .txt file.")
            return

        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            messagebox.showerror(
                "File could not be read",
                "This file is not readable as a UTF-8 text file.",
            )
            return
        except OSError as error:
            messagebox.showerror("Could not open file", str(error))
            return

        for row in self.table.get_children():
            self.table.delete(row)

        self.file_label.config(text=f"File: {path.name}")
        if not content.strip():
            self.status_label.config(text="The selected text file is empty.")
            return

        results = analyze_text(content)
        for term, count, suggestion in results:
            self.table.insert("", "end", values=(term, count, suggestion))

        if results:
            self.status_label.config(text="Review the terms and suggestions below.")
        else:
            self.status_label.config(
                text="No predefined gender-specific terms were detected."
            )


def main():
    root = tk.Tk()
    RecognizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
