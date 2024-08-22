import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

class ImageCompressorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Compressor")

        self.filepath = None

        
        self.select_button = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=10)

        self.compress_button = tk.Button(root, text="Compress Image", command=self.compress_image, state=tk.DISABLED)
        self.compress_button.pack(pady=10)

        self.quality_label = tk.Label(root, text="Quality (1-100):")
        self.quality_label.pack(pady=5)

        self.quality_input = tk.Entry(root)
        self.quality_input.insert(0, "50")  
        self.quality_input.pack(pady=5)

    def select_image(self):
        self.filepath = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if self.filepath:
            self.compress_button.config(state=tk.NORMAL)

    def compress_image(self):
        if not self.filepath:
            messagebox.showerror("Error", "No image selected")
            return

        try:
            quality = int(self.quality_input.get())
            if quality < 1 or quality > 100:
                raise ValueError("Quality must be between 1 and 100")

            img = Image.open(self.filepath)

            
            save_path = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")]
            )
            if not save_path:
                return

            
            img.save(save_path, "JPEG", quality=quality)
            messagebox.showinfo("Success", f"Image saved to {save_path}")

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", str(e))



if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorApp(root)
    root.mainloop()