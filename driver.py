"""Drivers for the simulation"""
from typing import Optional
from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    id: A unique identifier for the driver.
    location: The current location of the driver.
    is_idle: True if the driver is idle and False otherwise.
    destination: A destination the driver has to go to (May be None)

    === Private Attributes ===
    _speed: Integer value of the driver's speed
    _rider: String value storing current passenger
    """

    id: str
    location: Location
    is_idle: bool
    destination: Optional[Location]

    _speed: int
    _rider: Optional[str]

    def __init__(self, identifier: str, location: Location, speed: int) -> None:
        """Initialize a Driver.

        """
        self.id = identifier
        self.location = location
        self.is_idle = True
        self._speed = speed
        self.destination = None
        self._rider = None

    def __str__(self) -> str:
        """Return a string representation.

        """
        return f"Driver {self.id} currently at {self.location} " \
               f"with speed {self._speed}"

    def __eq__(self, other: object) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return self.id == other.id and self.location == other.location

    def get_travel_time(self, destination: Location) -> int:
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        """
        dist = manhattan_distance(self.location, destination)
        return round(dist / self._speed)

    def start_drive(self, location: Location) -> int:
        """Start driving to the location.
        Return the time that the drive will take.

        """
        self.destination = location
        return self.get_travel_time(self.destination)

    def end_drive(self) -> None:
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.
        """
        self.location = self.destination
        self.is_idle = True

    def start_ride(self, rider: Rider) -> int:
        """Start a ride and return the time the ride will take.

        """
        self.location = rider.origin
        self.destination = rider.dest
        self.is_idle = False
        self._rider = rider.id
        return self.get_travel_time(self.destination)

    def end_ride(self) -> None:
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.
        """
        self.location = self.destination
        self.destination = None
        self.is_idle = True
        self._rider = None


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(
        config={'extra-imports': ['location', 'rider']})
