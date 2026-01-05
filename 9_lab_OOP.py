class Animal:
    """Base animal class."""
    def __init__(self, name: str):
        self.name = name

    def sound(self) -> str:
        """Default sound."""
        return "Some sound"

class Dog(Animal):
    """Dog subclass."""
    def sound(self) -> str:
        """Overrides animal sound."""
        base_sound = super().sound()
        return f"{base_sound}: Woof!"

class TrainedEntity:
    """Represents a trained role."""
    def __init__(self, command: str):
        self.command = command

    def perform_action(self):
        """Performs a trick."""
        return f"Performing: {self.command}"

class ServiceDog(Dog, TrainedEntity):
    """Multiple inheritance example."""
    def __init__(self, name: str, command: str):
        Dog.__init__(self, name)
        TrainedEntity.__init__(self, command)

rescue_dog = ServiceDog("Buddy", "Search and Rescue")
print(rescue_dog.sound())
print(rescue_dog.perform_action())
print(f"MRO: {ServiceDog.mro()}")