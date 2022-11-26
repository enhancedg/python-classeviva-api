class ClasseVivaException(Exception):
    def __init__(self, msg: str, error_code: int):
        self.message = msg
        self.error_code = error_code

        super().__init__(msg)

    def __str__(self):
        return f"{self.message}. HTTP Status: {self.error_code}"