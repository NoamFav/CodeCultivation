def garden_intro(name: str, plant: str, height: int, age: int) -> None:
    print(f"=== Welcome to {name} ===")
    print(f"Plant: {plant}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    garden_intro("Eden", "Lilith", 23, 1231)
