from room import Room


class Blueprint():
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __init__(self, area_count: int, area_size: int):
        self.area_count: int = area_count
        self.area_size: int = area_size
        self.rooms: list[Room] = []
        self.map: list[list[Room]] = []

    def build_blueprint(self, data, randomize: bool = True) -> None:
        # data: something like json, dict

        for y in range(self.area_count):
            row = []
            for x in range(self.area_count):
                row.append(Room(x, y, -1, -1))

            self.map.append(row)

    def get_room(self, number) -> Room:
        """Returns the room with the given room number

        Raises:
            IndexError"""
        return self.rooms[number]

    def get_location(self, x: int, y: int) -> Room:
        """Returns the room at (x, y).

        Raises:
            IndexError"""
        return self.map[y][x]

    def get_next_location(self, x: int, y: int, dir: int) -> Room:
        """Returns a room adjacent to the room at (x, y).

        Raises:
            IndexError"""
        if dir == Blueprint.NORTH:
            return self.get_location(x, y - 1)
        elif dir == Blueprint.EAST:
            return self.get_location(x + 1, y)
        elif dir == Blueprint.SOUTH:
            return self.get_location(x, y + 1)
        elif dir == Blueprint.WEST:
            return self.get_location(x - 1, y)
        else:
            return self.get_location(x, y)
