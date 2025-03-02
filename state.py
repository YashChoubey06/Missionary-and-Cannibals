class State:

    def __init__(self, missionaries, cannibals, boat, parent=None):

        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent


    def is_valid(self):

        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if (3 - self.missionaries) > 0 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True


    def is_goal(self):

        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0


    def get_possible_moves(self):

        moves = [
            (1, 0),
            (2, 0),
            (0, 1),
            (0, 2),
            (1, 1)
        ]
        children = []

        for missionaries_moved, cannibals_moved in moves:
            if self.boat == 1:
                new_state = State(
                    self.missionaries - missionaries_moved,
                    self.cannibals - cannibals_moved,
                    0,
                    self
                )
            else:
                new_state = State(
                    self.missionaries + missionaries_moved,
                    self.cannibals + cannibals_moved,
                    1,
                    self
                )

            if new_state.is_valid():
                children.append(new_state)

        return children


    def __str__(self):

        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {'Left' if self.boat else 'Right'}"