class Room():
    def __init__(self, x: int, y: int, number: int, area: int):
        self.x: int = x
        self.y: int = y
        self.number: int = number
        self.area: int = area
        self.paths: list[int] = [0, 0, 0, 0]

    def get_type(self):
        result = ""

        for path in self.paths:
            if path > 0:
                result = "1" + result
            else:
                result = "0" + result
        return result
