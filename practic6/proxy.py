class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Обработка запроса.")

class Proxy(Subject):
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        print("Proxy: Дополнительная логика перед выполнением запроса.")
        self._real_subject.request()
        print("Proxy: Дополнительная логика после выполнения запроса.")

if __name__ == "__main__":
    proxy = Proxy()
    proxy.request()
