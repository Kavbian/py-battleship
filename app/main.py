class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = False) -> None:
        self.row = row
        self.column = column

    def __eq__(self, other: tuple) -> bool:
        return self.row == other[0] and self.column == other[1]


class Ship:
    def __init__(
            self,
            start: tuple,
            end: tuple,
            is_drowned: bool = False
    ) -> None:
        # Create decks and save them to a list `self.decks`
        self.decks = []
        self.is_drowned = is_drowned
        self.alive_decks = 0

        for row in range(start[0], end[0] + 1):
            for column in range(start[1], end[1] + 1):
                self.decks.append(Deck(row, column))
                self.alive_decks += 1

    def get_deck(self, row: int, column: int) -> Deck:
        # Find the corresponding deck in the list
        deck_index = self.decks.index((row, column))
        return self.decks[deck_index]

    def fire(self, row: int, column: int) -> None:
        # Change the `is_alive` status of the deck
        # And update the `is_drowned` value if it's needed
        self.get_deck(row, column).is_alive = False
        self.alive_decks -= 1
        if self.alive_decks == 0:
            self.is_drowned = True


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        # Create a dict `self.field`.
        # Its keys are tuples - the coordinates of the non-empty cells,
        # A value for each cell is a reference to the ship
        # which is located in it
        self.field = {}
        for coordinates in ships:
            self.field[coordinates] = Ship(coordinates[0], coordinates[1])

    def fire(self, location: tuple) -> str:
        # This function should check whether the location
        # is a key in the `self.field`
        # If it is, then it should check if this cell is the last alive
        # in the ship or not.
        for ship_coordinates in self.field.keys():
            if (
                location[0] >= ship_coordinates[0][0]
                and location[0] <= ship_coordinates[1][0]
                and location[1] >= ship_coordinates[0][1]
                and location[1] <= ship_coordinates[1][1]
            ):
                self.field[ship_coordinates].fire(location[0], location[1])
                return (
                    "Sunk!" if self.field[ship_coordinates].is_drowned
                    else "Hit!"
                )

        return "Miss!"


battle_ship = Battleship(
    ships=[
        ((2, 0), (2, 3)),
        ((4, 5), (4, 6)),
        ((3, 8), (3, 9)),
        ((6, 0), (8, 0)),
        ((6, 4), (6, 6)),
        ((6, 8), (6, 9)),
        ((9, 9), (9, 9)),
        ((9, 5), (9, 5)),
        ((9, 3), (9, 3)),
        ((9, 7), (9, 7)),
    ]
)

print(battle_ship.fire((0, 4)))
print(battle_ship.fire((1, 7)))
print(battle_ship.fire((2, 0)))
print(battle_ship.fire((2, 1)))
print(battle_ship.fire((2, 2)))
print(battle_ship.fire((2, 3)))
print(battle_ship.fire((4, 3)))
print(battle_ship.fire((4, 5)))
print(battle_ship.fire((5, 5)))
print(battle_ship.fire((4, 6)))
print(battle_ship.fire((9, 5)))
print(battle_ship.fire((9, 6)))
