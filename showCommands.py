import tkinter as tk
from tkinter import ttk




def showingCommands() -> None:
    # Create the main window
    root = tk.Tk()
    root.title("Nova Commands")
    root.geometry("1920x1080")  # Set window size
    root.iconbitmap("gg.ico")
    root.configure(bg="#2b333c")  # Dark background

    # Custom styling
    style = ttk.Style()
    style.configure("TLabel", font=("outfit semibold", 14), background="#2b333c", foreground="#d3e1e5")
    style.configure("TFrame", background="#2b333c")

    # Create a frame with padding
    frame = ttk.Frame(root, padding=20, style="TFrame")
    frame.pack(expand=True)

    # Title Label (centered)
    title_label = ttk.Label(frame, text="Nova Commands", font=("outfit semibold", 35, "bold"), background="#2b333c", foreground="#78cfd2", anchor="center")
    title_label.pack(pady=(0, 10))

    # Text content (left-aligned)
    text = (
        "1 - \"open\"  To open an app\n\n"
        "2 - \"open website\"  To open a specific website\n\n"
        "3 - \"google\"  To google something\n\n"
        "4 - \"shutdown , restart , sleep\"\n\n"
        "5 - or ask a question immediately to have a response from our generative AI\n\n"
    )

    text_label = ttk.Label(frame, text=text, style="TLabel", wraplength=450, anchor="w", justify="left")
    text_label.pack(anchor="w")  # Align text to the left

    root.mainloop()


