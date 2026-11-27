class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants: list[Plant] = [
        Plant("Lilith", 10, 10),
        Plant("Roses", 20, 10),
        Plant("Golden apple", 312, 323912),
    ]
    print(plant for plant in plants)
