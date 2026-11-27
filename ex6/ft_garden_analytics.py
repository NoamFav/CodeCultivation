class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = (
            float(height) if self._validate(height, "Height") else 0.0
        )
        self._age = age if self._validate(age, "Age") else 0
        print(f"Plant created: {self}")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    def grow(self, rate: float, days: int = 1) -> None:
        self.age += days
        self.height = round(self.height + rate * days, 1)

    def _validate(self, value: float, name: str) -> bool:
        if value < 0:
            print(f"{self._name}: Error, {name} can't be negative ({value})")
            print(f"{name} updat rejected")
            return False
        return True

    @property
    def name(self) -> str:
        return self._name

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float) -> None:
        if self._validate(height, "Height"):
            self._height = float(height)
            print(f"Height updated: {self.height}cm")

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> None:
        if self._validate(age, "Age"):
            self._age = age
            print(f"Age updated: {age} days")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def __str__(self) -> str:
        return f"{super().__str__()}\n Color: {self.color}"

    def bloom(self, isblooming: bool) -> None:
        if isblooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    @property
    def color(self) -> str:
        return self._color


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def __str__(self) -> str:
        return f"{super().__str__()}\n Trunk diameter: {self.trunk_diameter}"

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of {self.height}"
            f"long and {self.trunk_diameter}cm wide"
        )

    @property
    def trunk_diameter(self) -> float:
        return self._trunk_diameter


class Vegetables(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int,
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def __str__(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"Harvest season: {self.harvest_season}\n"
            f"Nutritional value: {self.nutritional_value}"
        )

    def grow(
        self, rate: float, days: int = 1, *, nutritional_rate: float = 1.0
    ) -> None:
        super().grow(rate, days)
        self.nutritional_value = int(
            self.nutritional_value + nutritional_rate * days,
        )

    @property
    def harvest_season(self) -> str:
        return self._harvest_season

    @property
    def nutritional_value(self) -> int:
        return self._nutritional_value

    @nutritional_value.setter
    def nutritional_value(self, nutritional_value: int):
        if self._validate(
            nutritional_value,
            "Nutritional value",
        ):
            self._nutritional_value = nutritional_value
            print(
                f"Nutritional value updated: {nutritional_value}",
            )
