"""HW2: the club's own exceptions."""


class SignupError(Exception):
    """The parent of every sign-up problem."""


class NotSignedUpError(SignupError):
    """The member has no seat and is not on the waitlist."""

    def __init__(self, member: str, event: str):
        super().__init__(f"{member} is not signed up for {event}")
        self.member = member
        self.event = event


class AlreadySignedUpError(SignupError):
    """The member is already signed up."""

    def __init__(self, member: str, event: str):
        super().__init__(
            f"{member} is already signed up for {event}"
        )
        self.member = member
        self.event = event


class UnknownEventError(SignupError):
    """The club has no event with this title."""

    def __init__(self, title: str):
        super().__init__(f"there is no event called {title!r}")
        self.title = title