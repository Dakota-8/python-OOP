class PrinterError(Exception):
    """Класс общих ошибок принтера"""


class PrinterConnectionError(PrinterError):
    """Ошибка соединения с принтером"""


class PrinterPageError(PrinterError):
    """Ошибка отсутствия бумаги в принтере"""


try:
    raise PrinterConnectionError('соединение с принтером отсутствует')
except (PrinterConnectionError, PrinterPageError) as e:
    print(e)
except PrinterError as e:
    print(e)
