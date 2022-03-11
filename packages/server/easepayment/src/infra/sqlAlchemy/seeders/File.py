class File:
    @staticmethod
    def init(path: str, permition: str = "r"):
        file_open = open(path, permition)

        return file_open
