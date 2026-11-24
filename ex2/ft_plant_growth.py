class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def grow(plant: Plant, rate: float, days: int):
    print("=== Garden Plant Growth ===")
    plant.show()
    for i in range(days):
        print(f"=== Day {i + 1} ===")
        plant.height = round(plant.height + rate, 1)
        plant.age += 1
        plant.show()
    print(f"Growth this week: {rate * days}cm")


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Lilith", 10, 10),
        Plant("Roses", 20, 10),
        Plant("Golden apple", 312, 323912),
    ]
    grow(plants[0], 0.2, 10)
