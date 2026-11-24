"""HW2: the club and its chat bot."""

from collections import Counter

from errors import SignupError, UnknownEventError
from event import Event


class Club:
    """A student club."""

    def __init__(self, name: str):
        self.name = name
        self.events: dict[str, Event] = {}

    def add_event(self, title: str, capacity: int) -> Event:
        """Create and store a new event."""

        if capacity < 1:
            raise ValueError(
                f"capacity must be at least 1, got {capacity}"
            )

        if title in self.events:
            raise ValueError(f"event already exists: {title}")

        new_event = Event(title, capacity)
        self.events[title] = new_event

        return new_event

    def event(self, title: str) -> Event:
        """Find an event by title."""

        try:
            return self.events[title]
        except KeyError:
            raise UnknownEventError(title)

    def handle(self, line: str) -> str:
        """Answer one chat command."""

        parts = [part.strip() for part in line.split(",")]

        if len(parts) != 3:
            return f"Sorry, I don't understand {line!r}."

        command, title, member = parts
        command = command.lower()

        if command not in ("join", "leave"):
            return f"Sorry, I don't understand {line!r}."

        try:
            event = self.event(title)

            if command == "join":
                result = event.sign_up(member)

                if result == "seat":
                    return f"{member} has a seat at {title}."

                return f"{member} is on the waitlist for {title}."

            if command == "leave":
                promoted = event.cancel(member)

                if promoted is None:
                    return f"{member} left {title}."

                return (
                    f"{member} left {title}. "
                    f"{promoted} gets the seat."
                )

        except SignupError as error:
            return f"Sorry, {error}."

    def attendance(self) -> dict[str, int]:
        """Count how many event seats each member has."""

        counts = Counter()

        for event in self.events.values():
            counts.update(event.seats)

        return dict(counts)


if __name__ == "__main__":
    club = Club("Harbour.Space Bangkok club")

    club.add_event("Muay Thai basics", 2)

    for line in [
        "join, Muay Thai basics, Nino",
        "join, Muay Thai basics, Aung",
        "join, Muay Thai basics, Tashi",
        "leave, Muay Thai basics, Nino",
        "join, Chess night, Ploy",
    ]:
        print(club.handle(line))