class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def grow(self):
        self.height += 1
        return f"{self.name} grew 1cm"


class FloweringPlant(Plant):
    def __init__(self, name, age, height, color):
        super().__init__(name, age, height)
        self.color = color

    def speciality(self):
        return "(blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, age, height, color, prize_points):
        super().__init__(name, age, height, color)
        self.prize_points = prize_points


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow())
            self.total_growth += 1

    def get_summary(self):
        return {
            "plants": self.plants,
            "total_growth": self.total_growth,
            "count": len(self.plants)
        }

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers {plant.speciality()}, Prize points: {plant.prize_points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flowers {plant.speciality()}")
            else:
                print(f"- {plant.name}: {plant.height}cm")


class GardenManager:
    def __init__(self):
        self.gardens = []
        self.stats = GardenManager.GardenStats()

    def add_garden(self, garden):
        self.gardens.append(garden)

    def show_scores(self):
        scores = {}
        for garden in self.gardens:
            scores[garden.owner] = self.stats.calculate_score(garden.plants)
        return scores

    @classmethod
    def create_garden_network(cls, *gardens):
        manager = cls()
        for garden in gardens:
            manager.add_garden(garden)
        return manager

    @staticmethod
    def validate_height(plant):
        return plant.height > 0

    class GardenStats:
        def count_plant_types(self, plants):
            regular = flowering = prize = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return regular, flowering, prize

        def calculate_score(self, plants):
            score = 0
            for plant in plants:
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.prize_points
            return score


def main():
    print("=== Garden Management System Demo ===")

    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    oak = Plant("Oak Tree", 50, 100)
    rose = FloweringPlant("Rose", 2, 25, "red")
    sunflower = PrizeFlower("Sunflower", 1, 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.help_plants_grow()
    alice_garden.report()

    manager = GardenManager.create_garden_network(alice_garden, bob_garden)

    summary = alice_garden.get_summary()
    regular, flowering, prize = manager.stats.count_plant_types(summary["plants"])

    print(f"Plants added: {summary['count']}, Total growth: {summary['total_growth']}cm")
    print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
    print(f"Height validation test: {GardenManager.validate_height(oak)}")

    scores = manager.show_scores()
    print(f"Garden scores - Alice: {scores['Alice']}, Bob: {scores['Bob']}")
    print(f"Total gardens managed: {len(manager.gardens)}")


if __name__ == "__main__":
    main()
