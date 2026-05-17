# Object-Oriented Programming & Design Patterns (MOD_07)

## 📋 Description

MOD_07 teaches advanced OOP concepts through a fantasy card game system. Learn classes, inheritance, composition, design patterns (Factory, Strategy), interfaces, and building complex object-oriented systems.

## ✨ Features

- **Class Hierarchies** - Base classes and inheritance
- **Card System** - Multiple card types (Creature, Spell, Artifact, Elite)
- **Factory Pattern** - CardFactory and FantasyCardFactory
- **Strategy Pattern** - GameStrategy and AggressiveStrategy
- **Interface Implementation** - Magical, Combatable, Rankable interfaces
- **Game Engine** - Complex game logic and state management
- **Tournament Platform** - Multi-player tournament system
- **Deck Management** - Card collection and shuffling

## 🏗️ Architecture

```
Card System
    ├── Card (Base Class)
    │   ├── CreatureCard
    │   ├── SpellCard
    │   ├── ArtifactCard
    │   └── EliteCard (Combatable + Magical)
    │
    ├── Deck Management
    │   └── Deck (Collection of cards)
    │
    ├── Factories
    │   ├── CardFactory (Abstract)
    │   └── FantasyCardFactory (Concrete)
    │
    ├── Strategies
    │   ├── GameStrategy (Abstract)
    │   └── AggressiveStrategy (Concrete)
    │
    ├── Interfaces
    │   ├── Magical (Spellcasting ability)
    │   ├── Combatable (Combat mechanics)
    │   └── Rankable (Ranking system)
    │
    └── Game Engine
        ├── Game State
        └── Turn Management
```


## 💡 REVISION

### Create a Card

```python
from ex0.Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int | float, rarity: str, 
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
    
    def play(self, game_stat: dict) -> dict:
        game_stat['creatures'].append(self)
        return game_stat
    
    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({'attack': self.attack, 'health': self.health})
        return info

creature = CreatureCard("Dragon", 5, "Rare", 7, 5)
print(creature.get_card_info())
```

### Deck Management

```python
from ex1.Deck import Deck

deck = Deck("My Deck")
deck.add_card(creature)
deck.add_card(spell)
deck.shuffle()

for card in deck.draw(5):
    print(card.name)
```

### Card Factory

```python
from ex3.FantasyCardFactory import FantasyCardFactory

factory = FantasyCardFactory()
dragon = factory.create_creature("Dragon", 5, "Rare", 7, 5)
lightning = factory.create_spell("Lightning", 2, "Uncommon", 4)
```

### Game Strategy

```python
from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy

engine = GameEngine(player_deck, opponent_deck)
strategy = AggressiveStrategy()
next_move = strategy.decide_action(engine.game_state)
```

## 📁 Folder Structure

```
MOD_07/
├── ex0/
│   ├── __init__.py
│   ├── Card.py               # Base Card class
│   ├── CreatureCard.py
│   └── main.py
├── ex1/
│   ├── __init__.py
│   ├── Deck.py
│   ├── SpellCard.py
│   ├── ArtifactCard.py
│   └── main.py
├── ex2/
│   ├── __init__.py
│   ├── Combatable.py         # Interface for combat
│   ├── Magical.py            # Interface for magic
│   ├── EliteCard.py
│   └── main.py
├── ex3/
│   ├── __init__.py
│   ├── CardFactory.py        # Abstract factory
│   ├── FantasyCardFactory.py # Concrete factory
│   ├── GameStrategy.py       # Strategy pattern
│   ├── AggressiveStrategy.py
│   ├── GameEngine.py
│   └── main.py
├── ex4/
│   ├── __init__.py
│   ├── TournamentCard.py
│   ├── TournamentPlatform.py
│   ├── Rankable.py           # Ranking interface
│   └── main.py
├── tools/
│   ├── __init__.py
│   └── card_generator.py     # Utility functions
├── __init__.py
├── README.md
└── tests/
```
## 🚢 Deployment

### Use Card System in Application

```python
from MOD_07.ex3.FantasyCardFactory import FantasyCardFactory
from MOD_07.ex1.Deck import Deck

factory = FantasyCardFactory()

# Create decks
player_deck = Deck("Player")
for _ in range(20):
    card = factory.create_creature("Goblin", 1, "Common", 1, 1)
    player_deck.add_card(card)

opponent_deck = Deck("Opponent")
for _ in range(20):
    card = factory.create_spell("Fireball", 3, "Uncommon", 4)
    opponent_deck.add_card(card)

# Start game
from MOD_07.ex3.GameEngine import GameEngine
engine = GameEngine(player_deck, opponent_deck)
engine.play_turn()
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Can't instantiate Card | Card is abstract; create CreatureCard, SpellCard, etc. |
| AttributeError on card | Check card type before accessing specific attributes |
| Factory returns None | Verify factory implementation matches CardFactory interface |
| Strategy errors | Ensure game_state has required keys |

**Key Learning Outcomes:**
- ✅ Class hierarchies and inheritance
- ✅ Abstract classes and interfaces
- ✅ Composition and aggregation
- ✅ Factory design pattern
- ✅ Strategy design pattern
- ✅ Polymorphism and method overriding
- ✅ Complex object-oriented systems
