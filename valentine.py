import tkinter as tk
from PIL import Image, ImageTk

class ValentineCard:
    def __init__(self, root):
        self.root = root
        self.root.title("Valentine's Day Card")
        self.root.geometry("600x500")
        self.root.configure(bg="#FFC0CB")  # Розовый фон
        
        try:
            self.neutral_img = ImageTk.PhotoImage(Image.open("neutral.jpg").resize((150, 150)))
            self.happy_img = ImageTk.PhotoImage(Image.open("happy.jpg").resize((150, 150)))
            self.sad_img = ImageTk.PhotoImage(Image.open("sad.jpg").resize((150, 150)))
        except:
            self.neutral_img = self.create_cat_image("neutral")
            self.happy_img = self.create_cat_image("happy")
            self.sad_img = self.create_cat_image("sad")
        
        self.text_label = tk.Label(
            root, 
            text="Will you be my Valentine?", 
            font=("Comic Sans MS", 24, "bold"),
            bg="#FFC0CB",
            fg="#D35400"
        )
        self.text_label.pack(pady=30)
        
        self.button_frame = tk.Frame(root, bg="#FFC0CB")
        self.button_frame.pack(pady=20)
        
        self.yes_button = tk.Button(
            self.button_frame, 
            text="YES", 
            font=("Arial", 14, "bold"),
            width=10,
            bg="#27AE60",
            fg="white",
            command=self.yes_clicked
        )
        self.yes_button.pack(side=tk.LEFT, padx=30)
        
        self.no_button = tk.Button(
            self.button_frame, 
            text="NO", 
            font=("Arial", 14, "bold"),
            width=10,
            bg="#E74C3C",
            fg="white",
            command=self.no_clicked
        )
        self.no_button.pack(side=tk.LEFT, padx=30)
        
        # Область для котика
        self.canvas = tk.Canvas(root, width=600, height=300, bg="#FFC0CB", highlightthickness=0)
        self.canvas.pack()
        
        # Изначально показываем нейтрального котика
        self.cat = self.canvas.create_image(300, 200, image=self.neutral_img)

    def create_cat_image(self, state):
        """Создает простое изображение котика если файлы отсутствуют"""
        img = Image.new('RGB', (150, 150), 'white')
        draw = ImageDraw.Draw(img)
        
        if state == "neutral":
            # Нейтральный котик
            draw.ellipse((20, 20, 130, 130), fill='gray')
            draw.ellipse((40, 40, 70, 70), fill='black')
            draw.ellipse((80, 40, 110, 70), fill='black')
            draw.ellipse((50, 80, 100, 100), fill='pink')
        elif state == "happy":
            draw.ellipse((20, 20, 130, 130), fill='gray')
            draw.ellipse((40, 40, 70, 70), fill='black')
            draw.ellipse((80, 40, 110, 70), fill='black')
            draw.ellipse((50, 80, 100, 100), fill='pink')
            # Цветок
            draw.ellipse((100, 10, 140, 50), fill='red')
            draw.ellipse((100, 30, 140, 70), fill='yellow')
            draw.ellipse((100, 50, 140, 90), fill='red')
        else:  # sad
            draw.ellipse((20, 20, 130, 130), fill='gray')
            draw.ellipse((40, 40, 70, 70), fill='black')
            draw.ellipse((80, 40, 110, 70), fill='black')
            draw.ellipse((50, 80, 100, 100), fill='pink')

            draw.ellipse((60, 60, 70, 70), fill='blue')
            draw.ellipse((90, 60, 100, 70), fill='blue')
        
        return ImageTk.PhotoImage(img)

    def yes_clicked(self):
        """Обработка нажатия YES"""
        self.canvas.itemconfig(self.cat, image=self.happy_img)
        
        self.animate_cat_up(200, 100)
        
        self.yes_button.config(state=tk.DISABLED)
        self.no_button.config(state=tk.DISABLED)

    def animate_cat_up(self, current_y, target_y):
        """Анимация движения котика вверх"""
        if current_y > target_y:
            self.canvas.move(self.cat, 0, -5)
            self.root.after(50, lambda: self.animate_cat_up(current_y - 5, target_y))

    def no_clicked(self):
        """Обработка нажатия NO"""
        self.canvas.itemconfig(self.cat, image=self.sad_img)
        
        self.yes_button.config(state=tk.DISABLED)
        self.no_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    
    try:
        Image.open("neutral.jpg")
    except:
        for state in ["neutral", "happy", "sad"]:
            img = Image.new('RGB', (150, 150), 'white')
            draw = ImageDraw.Draw(img)
            if state == "neutral":
                draw.ellipse((20, 20, 130, 130), fill='gray')
            elif state == "happy":
                draw.ellipse((20, 20, 130, 130), fill='gray')
                draw.ellipse((100, 10, 140, 50), fill='red')
                draw.ellipse((100, 30, 140, 70), fill='yellow')
                draw.ellipse((100, 50, 140, 90), fill='red')
            else:
                draw.ellipse((20, 20, 130, 130), fill='gray')
                draw.ellipse((60, 60, 70, 70), fill='blue')
                draw.ellipse((90, 60, 100, 70), fill='blue')
            img.save(f"{state}.jpg")
    
    app = ValentineCard(root)
    root.mainloop()