"""
Подвиг 10 (на повторение). В программе объявлены два класса и глобальная переменная:

CURRENT_OS = 'windows'   # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов

Вам необходимо объявить класс с именем FileDialogFactory (фабрика классов), который бы при выполнении команды:

dlg = FileDialogFactory(title, path, exts)

возвращал объект класса WindowsFileDialog, если CURRENT_OS равна строке 'windows', в противном случае - объект класса
LinuxFileDialog. Объект самого класса FileDialogFactory создаваться не должен.

Для реализации такой логики, объявите внутри класса FileDialogFactory два статических метода:

def create_windows_filedialog(title, path, exts) - для создания объектов класса WindowsFileDialog;
def create_linux_filedialog(title, path, exts) - для создания объектов класса LinuxFileDialog.

Эти методы следует вызывать в магическом методе __new__() класса FileDialogFactory. Подумайте, как это правильно
сделать, чтобы не создавался объект самого класса, а лишь возвращался объект или класса WindowsFileDialog, или класса
LinuxFileDialog.

Пример использования класса (эту строчку в программе не писать):

dlg = FileDialogFactory('Изображения', 'd:/images/', ('jpg', 'gif', 'bmp', 'png'))

P.S. В программе нужно дополнительно объявить только класс FileDialogFactory. На экран выводить ничего не нужно.

"""
CURRENT_OS = 'windows'


class WindowsFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class LinuxFileDialog:
    def __init__(self, title, path, exts):
        self.__title = title
        self.__path = path
        self.__exts = exts


class FileDialogFactory:
    @staticmethod
    def create_windows_filedialog(title, path, exts):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title, path, exts):
        return LinuxFileDialog(title, path, exts)

    def __new__(cls, title, path, exts):
        if CURRENT_OS == 'windows':
            return cls.create_windows_filedialog(title, path, exts)
        if CURRENT_OS == 'linux':
            return cls.create_linux_filedialog(title, path, exts)
