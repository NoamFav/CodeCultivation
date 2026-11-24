class Plant:
    name: str
    height: float
    age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def show(plants: list[Plant]):
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    plants: list[Plant] = [
        Plant("Lilith", 10, 10),
        Plant("Roses", 20, 10),
        Plant("Golden apple", 312, 323912),
    ]
    show(plants)
