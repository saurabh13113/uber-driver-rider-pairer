"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""

from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    """A rider for a ride-sharing service.
    === Public Attributes ===
    id : String containing customer identifier
    patience : Integer containing amount of time a customer would wait before
               cancelling
    orig : Location where customer is waiting to be picked up
    dest : Location where customer wants to go
    status : Current mood of the rider in reference to a ride
    """
    id: str
    patience: int
    origin: Location
    dest: Location
    status: str

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.id = identifier
        self.patience = patience
        self.origin = origin
        self.dest = destination
        self.status = WAITING

    def cancelled(self) -> None:
        """Change rider status to cancelled if driver takes too long to come"""
        self.status = CANCELLED

    def satisfied(self) -> None:
        """Change rider status to satisfied if rider is picked up"""
        self.status = SATISFIED


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['location']})
