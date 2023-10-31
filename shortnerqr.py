import tkinter as tk
from tkinter import messagebox
import pyshorteners
import qrcode
from PIL import Image, ImageTk

# Function to shorten the URL
def shorten_url():
    original_url = url_entry.get()
    if original_url:
        try:
            s = pyshorteners.Shortener()
            shortened_url = s.tinyurl.short(original_url)  # You can use a different shortening service

            # Display the shortened URL
            shortened_url_label.config(text=f"Shortened URL: {shortened_url}")

            # Generate QR code for the shortened URL
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(shortened_url)
            qr.make(fit=True)

            # Create a QR code image
            qr_image = qr.make_image(fill_color="black", back_color="white")

            # Convert the QR code image to a PhotoImage for display in Tkinter
            photo = ImageTk.PhotoImage(image=qr_image)

            # Display the QR code
            qr_image_label.config(image=photo)
            qr_image_label.photo = photo  # Store a reference to avoid garbage collection
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Please enter a URL.")

# Create a GUI window
app = tk.Tk()
app.title("URL Shortener and QR Code Generator")

# Label and entry field for the original URL
url_label = tk.Label(app, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(app)
url_entry.pack()

# Button to shorten the URL
shorten_button = tk.Button(app, text="Shorten URL", command=shorten_url)
shorten_button.pack()

# Label to display the shortened URL
shortened_url_label = tk.Label(app, text="")
shortened_url_label.pack()

# Label to display the QR code
qr_image_label = tk.Label(app)
qr_image_label.pack()

# Start the GUI main loop
app.mainloop()