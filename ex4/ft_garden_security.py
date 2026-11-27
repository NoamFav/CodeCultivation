class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height) if self._valid_height(height) else 0.0
        self._age = age if self._valid_age(age) else 0
        print(f"Plant created: {self}")

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, rate: float, days: int = 1) -> None:
        print(self)
        for i in range(days):
            print(f"=== Day {i + 1} ===")
            self.height = round(self._height + rate, 1)
            self.age = self._age + 1
            print(self)

    def _valid_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative ({height})")
            print("Height update rejected")
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
        if self._valid_height(height):
            self._height = float(height)
            print(f"Height updated: {self.height}cm")

    @property
    def age(self) -> int:
        return self._age

    def _valid_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, Age can't be negative ({age})")
            print("Age update rejected")
            return False
        return True

    @age.setter
    def age(self, age: int) -> None:
        if self._valid_age(age):
            self._age = age
            print(f"Age updated: {age} days")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("Lilith", 20, 1210)
    print()
    plant.height = 25.0
    plant.age = 30
    print()
    plant.height = -21
    plant.age = -10
    print()
    print(f"Current state: {plant}")
