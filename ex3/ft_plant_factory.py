class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, rate: float, days: int) -> None:
        print(self)
        for i in range(days):
            print(f"=== Day {i + 1} ===")
            self.height = round(self.height + rate, 1)
            self.age += 1
            print(self)


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    Plant("Lilith", 10, 10)
