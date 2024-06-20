"""Locations for the simulation"""

from __future__ import annotations


class Location:
    """A two-dimensional location.
    === Public Attributes ===
    rows: Number of blocks location is from bottom of grid
    columns: Number of blocks location is from left of grid
    """
    rows: int
    columns: int

    def __init__(self, row: int, column: int) -> None:
        """Initialize a location.

        """
        self.rows = row
        self.columns = column

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f"({self.rows}, {self.columns})"

    def __eq__(self, other: Location) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return self.columns == other.columns and self.rows == other.rows


def manhattan_distance(origin: Location, destination: Location) -> int:
    """Return the Manhattan distance between the origin and the destination.

    """
    vert_dist = abs(destination.rows - origin.rows)
    hor_dist = abs(destination.columns - origin.columns)
    return vert_dist + hor_dist


def deserialize_location(location_str: str) -> Location:
    """Deserialize a location.

    location_str: A location in the format 'row,col'
    """
    row, col = int(location_str.split(',')[0]), int(location_str.split(',')[1])
    return Location(row, col)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
