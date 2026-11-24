"""HW2: one club event with limited seats."""

from dataclasses import dataclass, field

from errors import AlreadySignedUpError, NotSignedUpError


@dataclass
class Event:
    """One club event with seats and a waitlist."""

    title: str
    capacity: int
    seats: list[str] = field(default_factory=list)
    waitlist: list[str] = field(default_factory=list)

    def seats_left(self) -> int:
        """How many seats are still free."""
        return self.capacity - len(self.seats)

    def sign_up(self, member: str) -> str:
        """Give the member a seat or a waitlist place."""

        if member in self.seats or member in self.waitlist:
            raise AlreadySignedUpError(member, self.title)

        if self.seats_left() > 0:
            self.seats.append(member)
            return "seat"

        self.waitlist.append(member)
        return "waitlist"

    def cancel(self, member: str) -> str | None:
        """Remove the member and promote the first waiting member."""

        if member in self.waitlist:
            self.waitlist.remove(member)
            return None

        if member in self.seats:
            self.seats.remove(member)

            if self.waitlist:
                next_member = self.waitlist.pop(0)
                self.seats.append(next_member)
                return next_member

            return None

        raise NotSignedUpError(member, self.title)

    def place(self, member: str) -> int:
        """Return 0 for a seat or the waitlist position."""

        if member in self.seats:
            return 0

        try:
            return self.waitlist.index(member) + 1
        except ValueError:
            raise NotSignedUpError(member, self.title)