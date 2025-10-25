import tkinter as tk
from PIL import Image, ImageTk
import os


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        self.root.geometry("500x500")
        self.root.title("Начало")
        self.setUpMainWindow()

    def setUpMainWindow(self):
        """Создайте Label для отображения в главном окне."""
        hello_label = tk.Label(self.root, text="Добро пожаловать!",
                               font=("Arial", 15))
        hello_label.place(x=175, y=15)

        image_path = r"assets\pht1.jpg"
        try:
            if os.path.exists(image_path):
                image = Image.open(image_path)
                image = image.resize((490, 500))
                photo = ImageTk.PhotoImage(image)
                world_label = tk.Label(self.root, image=photo)
                world_label.image = photo  # сохраняем ссылку на изображение
                world_label.place(x=0, y=40)
            else:
                print(f"Image not found: {image_path}")
        except Exception as error:
            print(f"Error loading image: {error}")

    def show(self):
        self.root.mainloop()


class SecondWindow:
    def __init__(self):
        self.root = tk.Toplevel()
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс для второго окна."""
        self.root.geometry("400x700+550+100")
        self.root.title("Профиль пользователя")
        self.setUpMainWindow()

    def createImageLabels(self):
        """Открывает файлы изображений и создаёт метки изображений."""
        images = [
            r"assets\photo.jpg",
        ]
        x_position = 0
        y_position = 0

        for image_path in images:
            try:
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    # Масштабируем изображение если нужно
                    image = image.resize((395, 380))  # настройте размер по необходимости
                    photo = ImageTk.PhotoImage(image)

                    label = tk.Label(self.root, image=photo)
                    label.image = photo  # сохраняем ссылку
                    label.place(x=x_position, y=y_position)

                    x_position += 100
                    y_position += 150
                else:
                    print(f"Файл {image_path} не найден")
            except Exception as e:
                print(f"Ошибка при загрузке изображения {image_path}: {e}")

    def setUpMainWindow(self):
        """Создайте метки, которые будут отображаться в окне."""
        self.createImageLabels()

        # Информация о пользователе

        bio_label = tk.Label(self.root, text="Биография: Калганова Софья, 19 лет.",
                             font=("Arial", 15))
        bio_label.place(x=15, y=340)

        teach_label = tk.Label(self.root,
                               text="Обучение: МАИ , 2 курс , 317 кафедра - Инноватика",
                               wraplength=370, justify="left",font=("Arial", 17) )
        teach_label.place(x=15, y=405)

        experience_label = tk.Label(self.root, text="Опыт работы: отсутствует, в процессе",
                                    font=("Arial", 16))
        experience_label.place(x=15, y=470)

        developer_label = tk.Label(self.root,
                                   text="Фраза - чего то,\n то добиться надо ", font=("Arial", 17))
        developer_label.place(x=15, y=510)


    def show(self):
        self.root.mainloop()


# Запуск приложения
if __name__ == "__main__":
    window = MainWindow()
    window1 = SecondWindow()
    window.show()