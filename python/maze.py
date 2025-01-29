from room import Room
from blueprint import Blueprint


class Maze(Blueprint):
    def __init__(self, area_count: int, area_size: int):
        super.__init__(area_count, area_size)

        self.areas: dict[int, list[Room]] = dict()

    def build_maze(self, blueprint: Blueprint) -> None:
        for y in range(self.area_count * self.area_size):
            row = []
            for x in range(self.area_count * self.area_size):
                row.append(Room(x, y, -1, -1))

            self.map.append(row)

    def get_area(self, id: int) -> list[Room]:
        """Returns all rooms of a given area.

        Raises:
            KeyError"""
        return self.areas[id]

    def find_area_neighbors(self, room: Room, discovered: set[Room]) -> set[Room]:
        for direction in range(4):
            try:
                neighbor = self.get_next_location(room.x, room.y, direction)

                if neighbor.area == room.area and neighbor not in discovered:
                    discovered.add(neighbor)
                    self.find_area_neighbors(neighbor, discovered)
            except IndexError:
                pass
        return discovered

    def check_area_unity(self, id: int) -> bool:
        area = self.get_area(id)
        start = area[0]
        discovered = {start}
        discovered = self.find_area_neighbors(start, discovered)
        return len(area) == len(discovered)

    def set_area(self, room: Room, area: int) -> bool:
        old_area = room.area
        room.area = area

        if old_area == -1:
            self.get_area(area).append(room)
            return True
        elif self.check_area_unity(old_area):
            self.get_area(old_area).remove(room)
            self.get_area(area).append(room)
            return True
        else:
            # Or raise error
            return False
