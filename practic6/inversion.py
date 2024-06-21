class Processor:
    def process(self, callback):
        print(" Выполняется обработка...")
        callback()
        print("Обработка завершена.")

def my_callback():
    print("Вызвана функция обратного вызова!")

if __name__ == "__main__":
    processor = Processor()
    processor.process(my_callback)
