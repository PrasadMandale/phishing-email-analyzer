import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

CHECKS = {
    "Urgent wording": [
        "act now",
        "immediately",
        "account will be closed",
    ],
    "Sensitive information request": [
        "enter your password",
        "verify your password",
        "bank details",
    ],
    "Unusual payment request": [
        "gift card",
        "wire transfer",
        "send payment",
    ],
}


def analyze_email():
    email = email_box.get("1.0", tk.END).lower().strip()

    if not email:
        result_label.config(text="Paste an email first.", foreground="#555555")
        warnings_box.config(state="normal")
        warnings_box.delete("1.0", tk.END)
        warnings_box.config(state="disabled")
        return

    warnings = []

    for warning, phrases in CHECKS.items():
        if any(phrase in email for phrase in phrases):
            warnings.append(warning)

    if len(warnings) >= 2:
        result = "HIGH"
        color = "#b42318"
    elif len(warnings) == 1:
        result = "MEDIUM"
        color = "#b54708"
    else:
        result = "LOW"
        color = "#027a48"

    result_label.config(
        text=f"Risk indicator: {result}",
        foreground=color,
    )

    warnings_box.config(state="normal")
    warnings_box.delete("1.0", tk.END)

    if warnings:
        for warning in warnings:
            warnings_box.insert(tk.END, f"• {warning}\n")
    else:
        warnings_box.insert(
            tk.END,
            "No warning signs from this basic check were found.\n"
        )

    warnings_box.config(state="disabled")


window = tk.Tk()
window.title("Phishing Email Analyzer")
window.geometry("700x600")
window.minsize(550, 480)

main = ttk.Frame(window, padding=24)
main.pack(fill="both", expand=True)

title = ttk.Label(
    main,
    text="Phishing Email Analyzer",
    font=("Arial", 22, "bold"),
)
title.pack(anchor="w")

intro = ttk.Label(
    main,
    text="Paste a sample email to check for a few common warning signs.",
    wraplength=640,
)
intro.pack(anchor="w", pady=(8, 18))

email_box = ScrolledText(main, height=12, wrap="word", font=("Arial", 12))
email_box.pack(fill="both", expand=True)

analyze_button = ttk.Button(
    main,
    text="Analyze Email",
    command=analyze_email,
)
analyze_button.pack(anchor="w", pady=16)

result_label = tk.Label(
    main,
    text="Your result will appear here.",
    font=("Arial", 16, "bold"),
    anchor="w",
)
result_label.pack(fill="x", pady=(0, 10))

warnings_title = ttk.Label(main, text="Warning signs")
warnings_title.pack(anchor="w")

warnings_box = ScrolledText(
    main,
    height=5,
    wrap="word",
    font=("Arial", 12),
)
warnings_box.pack(fill="x", pady=(6, 12))
warnings_box.config(state="disabled")

note = ttk.Label(
    main,
    text="Learning project only. A LOW result does not prove an email is safe.",
    wraplength=640,
)
note.pack(anchor="w", pady=(4, 0))

window.mainloop()