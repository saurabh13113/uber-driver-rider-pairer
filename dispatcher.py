"""Dispatcher for the simulation"""

from typing import Optional

from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.

    === Public attributes ===
    riders: Riders who have requested a driver from dispatcher
    drivers: Drivers who have requested a rider from dispatcher
    """
    drivers: list
    riders: list
    _activdrivers: list

    def __init__(self) -> None:
        """Initialize a Dispatcher.

        """
        self.drivers = []
        self.riders = []
        self._activdrivers = []

    def __str__(self) -> str:
        """Return a string representation.

        """
        did = [dr.id for dr in self.drivers]
        rid = [dr.id for dr in self.riders]
        return f"The drivers who have requested a ride: {did}" \
               f"The riders who have requested a drive: {rid}"

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        if not self._activdrivers:
            self.riders.append(rider)
            return None
        else:
            lst = []
            for dr in self._activdrivers:
                tt = dr.get_travel_time(rider.origin)
                lst.append(tt)
            if not lst:
                self.riders.append(rider)
                return None
            else:
                ind = lst.index(min(lst))
                return self._activdrivers.pop(ind)

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver not in self._activdrivers:
            self._activdrivers.append(driver)
        if driver not in self.drivers:
            self.drivers.append(driver)
        if not self.riders:
            return None
        else:
            dr = self.riders.pop(0)
            return dr

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider.
        """
        if rider in self.riders:
            self.riders.remove(rider)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})
