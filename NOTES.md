# HW2 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?
I implemented the three files: errors.py, event.py, and club.py. I created custom exceptions, used a dataclass for Event, and implemented seat registration, cancellation, and waitlists. I also used Counter to calculate attendance.

## What broke, and how did you fix it?
At first, the methods contained NotImplementedError, so the main functionality was not implemented yet. I followed the assignment instructions and completed each method. I then ran python -m pytest to check my code. All 20 tests passed successfully.

## What would you do differently next time?
Next time, I would work on one function at a time and test it before moving to the next function. I would also read the assignment requirements more carefully and test different cases, especially errors, empty lists, and waitlists.
