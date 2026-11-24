class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def show(plants: list[Plant]):
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Lilith", 10, 10),
        Plant("Roses", 20, 10),
        Plant("Golden apple", 312, 323912),
    ]
    show(plants)
