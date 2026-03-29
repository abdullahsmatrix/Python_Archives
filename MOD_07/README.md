# DataDeck Game Engine - MOD_07

A sophisticated card game engine demonstrating the **Abstract Factory Pattern** combined with the **Strategy Pattern** in Python.

---

## 📋 Table of Contents

1. [Game Overview](#game-overview)
2. [How the Game Works](#how-the-game-works)
3. [Game Flow](#game-flow)
4. [Design Patterns](#design-patterns)
5. [Project Structure](#project-structure)
6. [Running the Game](#running-the-game)
7. [Card Types](#card-types)
8. [Strategy Types](#strategy-types)

---

## 🎮 Game Overview

**DataDeck** is a turn-based card game where:
- You start with **10 mana** per turn
- You have **10 cards in your hand**
- You play cards strategically to deal **damage to your opponent**
- Different **strategies** determine how cards are played
- Different **card factories** provide unique card types

The game demonstrates how to create flexible, extensible systems using design patterns.

---

## 🎯 How the Game Works

### **Simple Analogy: Shopping with a Budget**

Think of the game like **shopping with limited money**:

```
Budget: $10 (your mana)
Shopping List: 10 items (your hand)

Aggressive Strategy: "Buy the cheapest, most powerful items!"
├─ Item 1: Costs $2, gives 1 damage
├─ Item 2: Costs $3, gives 5 damage
├─ Item 3: Costs $3, gives 5 damage
└─ Money Left: $2 (can't afford more items)

Total Spent: $8
Total Power Gained: 11 damage
Items Bought: 3
Items Left in Store: 7
```

---

## 🔄 Game Flow

### **Step 1: Game Setup**

```python
factory = FantasyCardFactory()      # Create card source
strategy = AggressiveStrategy()      # Choose how to play
engine = GameEngine()               # Create game engine
engine.configure_engine(factory, strategy)  # Initialize
```

**What happens:**
- Factory generates 10 random fantasy cards
- Cards are loaded into your hand
- Mana pool is set to 10

### **Step 2: Turn Simulation**

```
Initial State:
├─ Hand: 10 cards
├─ Mana: 10
└─ Battlefield: 0 creatures

Strategy Decision Phase:
├─ Sort hand by cost (cheapest first)
└─ Play cards as long as mana allows

Execution Phase:
├─ Remove played cards from hand
├─ Creatures deployed to battlefield
├─ Calculate total damage
└─ Update game state

Final State After 1 Turn:
├─ Hand: 7 cards (3 were played)
├─ Mana: 2 remaining (spent 8)
├─ Battlefield: 3 creatures
└─ Total Damage: 11
```

### **Step 3: Turn Example**

**Your Hand:**
```
1. Goblin Warrior (2 mana) → 1 damage
2. Shadow Assassin (3 mana) → 5 damage  ⭐
3. Shadow Assassin (3 mana) → 5 damage  ⭐
4. Fire Dragon (5 mana) → 7 damage
5. Ice Wizard (4 mana) → 3 damage
6. Fireball (4 mana) → 0 damage (spell, not creature)
... and 4 more cards
```

**Aggressive Strategy Plays:**
```
Mana: 10/10 ✓

Play Goblin Warrior (2 mana)
├─ Cost: 2
├─ Mana Left: 8
├─ Damage Added: 1
├─ Placed on Battlefield ✓

Play Shadow Assassin (3 mana)
├─ Cost: 3
├─ Mana Left: 5
├─ Damage Added: 5
├─ Placed on Battlefield ✓

Play Shadow Assassin (3 mana)
├─ Cost: 3
├─ Mana Left: 2
├─ Damage Added: 5
├─ Placed on Battlefield ✓

Cannot Play Fire Dragon (needs 5, have 2) ✗
Cannot Play Ice Wizard (needs 4, have 2) ✗
Cannot Play Fireball (needs 4, have 2) ✗

Turn Complete:
├─ Cards Played: 3
├─ Total Damage: 11
├─ Mana Wasted: 2
```

---

## 🏗️ Design Patterns

### **1. Abstract Factory Pattern**

**Purpose:** Create different types of cards without the engine knowing specifics

```
CardFactory (Abstract)
    ↓
FantasyCardFactory (Concrete)
    ├─ Creates: Fire Dragon, Fireball, Mana Crystal
    └─ Theme: Fantasy/Magic

Alternative Implementations:
    SciFiCardFactory
    ├─ Creates: Laser Drone, Ion Blast, Energy Core
    └─ Theme: Sci-Fi/Technology

    MedievalCardFactory
    ├─ Creates: Knight, Sword Strike, Tower Shield
    └─ Theme: Medieval/Fantasy
```

**Key Benefits:**
- Swap factories without changing GameEngine
- Easy to add new card types
- Centralized card data management

### **2. Strategy Pattern**

**Purpose:** Decide how to play cards without hardcoding logic

```
GameStrategy (Abstract)
    ↓
AggressiveStrategy (Concrete)
    └─ Play cheapest, strongest cards
    └─ Attack enemy directly
    └─ Focus on damage output

Alternative Implementations:
    DefensiveStrategy
    └─ Play expensive, durable creatures
    └─ Build fortress on battlefield
    └─ Focus on surviving attacks

    BalancedStrategy
    └─ Mix of offense and defense
    └─ Play mid-cost cards
    └─ Adaptive to opponent
```

**Key Benefits:**
- Swap strategies without changing GameEngine
- Multiple playstyles possible
- Easy to add new decision-making logic

---

## 📁 Project Structure

```
MOD_07/
├── README.md                          # This file
├── __init__.py
├── __pycache__/
├── ex0/                               # Exercise 0: Card Base Classes
│   ├── Card.py                        # Abstract base card class
│   ├── CreatureCard.py                # Creature with attack/health
│   └── main.py
├── ex1/                               # Exercise 1: Card Types
│   ├── ArtifactCard.py                # Artifact cards with durability
│   ├── Deck.py                        # Deck management
│   ├── SpellCard.py                   # Spell cards with effects
│   └── main.py
├── ex2/                               # Exercise 2: Abstract Classes
│   ├── Combatable.py                  # Combat interface
│   ├── Elitecard.py                   # Elite creature type
│   ├── Magical.py                     # Magic interface
│   └── main.py
├── ex3/                               # Exercise 3: GAME ENGINE ⭐
│   ├── CardFactory.py                 # Abstract Factory interface
│   ├── FantasyCardFactory.py          # Concrete factory (creates cards)
│   ├── GameEngine.py                  # Main orchestrator
│   ├── GameStrategy.py                # Abstract Strategy interface
│   ├── AggressiveStrategy.py          # Concrete strategy (plays aggressively)
│   ├── main.py                        # Run the game
│   └── __pycache__/
├── ex4/                               # Exercise 4: Ranking System
│   ├── Rankable.py
│   └── main.py
└── tools/
    ├── card_generator.py              # Predefined card data
    └── __pycache__/
```

---

## 🚀 Running the Game

### **Run the Game Engine (EX3)**

```bash
cd /nfs/homes/amamun/42-Cursus/Python/Python_Archives/MOD_07
python3 -m ex3.main
```

**Output:**
```
=== DataDeck Game Engine ===

Configuring Fantasy Card Game...
Factory: FantasyCardFactory
Strategy: AggressiveStrategy
Available types: {'creatures': [...], 'spells': [...], 'artifacts': [...]}

Simulating aggressive turn...
Hand: [Fire Dragon (5), Goblin Warrior (2), Meteor (8), ...]

Turn execution:
Strategy: AggressiveStrategy
Actions: {'cards_played': ['Goblin Warrior', 'Shadow Assassin', ...], 
          'mana_used': 8, 'damage_dealt': 12}

Game Report:
{'turns_simulated': 1, 'strategy_used': 'AggressiveStrategy', 
 'total_damage': 12, 'cards_created': 10}

Abstract Factory + Strategy Pattern: Maximum flexibility!
```

---

## 🃏 Card Types

### **Creatures**
- **Cost:** Mana to play
- **Attack:** Damage dealt to opponent
- **Health:** Durability on battlefield
- **Example:** Fire Dragon (5 mana, 7 attack, 5 health)

```python
creature = factory.create_creature("Fire Dragon")
# Creates: CreatureCard(name="Fire Dragon", cost=5, rarity="Legendary", 
#                       attack=7, health=5)
```

### **Spells**
- **Cost:** Mana to cast
- **Effect:** Special abilities (damage, healing, buffs)
- **Example:** Fireball (4 mana, "damage" effect)

```python
spell = factory.create_spell("Fireball")
# Creates: SpellCard(name="Fireball", cost=4, rarity="Uncommon", 
#                    effect_type="damage")
```

### **Artifacts**
- **Cost:** Mana to equip
- **Durability:** Uses before breaking
- **Effect:** Permanent bonus effects
- **Example:** Mana Crystal (2 mana, 5 durability, "+1 mana per turn")

```python
artifact = factory.create_artifact("Mana Crystal")
# Creates: ArtifactCard(name="Mana Crystal", cost=2, rarity="Common", 
#                       durability=5, effect="+1 mana per turn")
```

---

## ⚔️ Strategy Types

### **AggressiveStrategy**

**Decision Logic:**
1. Sort hand by mana cost (cheapest first)
2. Play cards sequentially while mana allows
3. Prioritize creatures with high attack
4. Attack opponent directly

**Result:** Fast, high-damage turns with potential mana waste

```python
strategy = AggressiveStrategy()
# Plays: Goblin (2) + Shadow Assassin (3) + Shadow Assassin (3)
# Damage: 11 total
# Efficiency: 8 mana spent, 2 wasted
```

### **Future Strategies**

You can implement additional strategies:

```python
class DefensiveStrategy(GameStrategy):
    """Play expensive creatures with high health"""
    def execute_turn(self, hand, battlefield):
        # Sort by health (highest first)
        # Play defensive creatures
        # Minimize damage taken
        
class BalancedStrategy(GameStrategy):
    """Mix offense and defense"""
    def execute_turn(self, hand, battlefield):
        # Play 60% creatures, 40% spells
        # Calculate optimal mana usage
        
class ControlStrategy(GameStrategy):
    """Use spells and artifacts to control board"""
    def execute_turn(self, hand, battlefield):
        # Prioritize spells over creatures
        # Maximize special effects
```

---

## 📊 Game State Example

**Starting Position:**
```
Hand: [Fire Dragon (5), Goblin (2), Shadow Assassin (3), ...]
Mana: 10/10
Battlefield: []
Total Damage: 0
```

**After AggressiveStrategy Turn:**
```
Hand: [Fire Dragon (5), ...]                               (7 cards remain)
Mana: 2/10                                                 (8 spent, 2 wasted)
Battlefield: [Goblin, Shadow Assassin, Shadow Assassin]   (3 creatures)
Total Damage: 11                                           (damage dealt)

Opponent Health: Original - 11
```

---

## 🎓 Learning Outcomes

This project teaches:

✅ **Abstract Factory Pattern**
- Separating object creation from consumption
- Creating families of related objects
- Ensuring consistency across card types

✅ **Strategy Pattern**
- Encapsulating algorithms
- Making strategies interchangeable
- Supporting new strategies without modifying existing code

✅ **Game Design**
- Turn-based game mechanics
- Resource management (mana)
- Decision-making systems

✅ **Python Concepts**
- Abstract Base Classes (ABC)
- Dictionary comprehensions
- Type hints
- Object composition

---

## 🔧 How to Extend

### **Create a New Card Factory**

```python
class SciFiCardFactory(CardFactory):
    def __init__(self):
        self.generator = CardGenerator()  # Reuse generator
        self.creatures = {...}  # Sci-Fi creatures
        self.spells = {...}     # Sci-Fi spells
        self.artifacts = {...}  # Sci-Fi artifacts
```

### **Create a New Strategy**

```python
class DefensiveStrategy(GameStrategy):
    def execute_turn(self, hand, battlefield):
        # Sort by health instead of attack
        # Play to maximize defense
        
    def get_strategy_name(self):
        return "DefensiveStrategy"
        
    def prioritize_targets(self, available_targets):
        # Prioritize enemy creatures
```

---

## 📝 Summary

**DataDeck** is a flexible, extensible card game engine that:
- Uses **Abstract Factory** to create different card types
- Uses **Strategy** to implement different playstyles
- Demonstrates how design patterns enable clean, maintainable code
- Shows game engine concepts like hand management, mana pools, and turn simulation

**The key insight:** Once the patterns are in place, you can:
- Add new card types (just create a new factory)
- Add new playstyles (just create a new strategy)
- Change game rules (modify GameEngine once, works with all factories/strategies)

---

**Made by:** amamun  
**Date:** March 25, 2026  
**Pattern:** Abstract Factory + Strategy Pattern
