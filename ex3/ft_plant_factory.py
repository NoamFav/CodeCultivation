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


def factory(name: str, height: float, age: int) -> None:
    print("=== Plant Factory Output ===")
    plant: Plant = Plant("Lilith", 10, 10)
    print(f"Created: {plant.show()}")


if __name__ == "__main__":
    factory("Lilith", 10, 10)
