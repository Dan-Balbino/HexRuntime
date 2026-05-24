# HEXRUNTIME

> Program reality. Cast magic.

A sandbox game where spells are not selected from a list — they are programmed by the player through an arcane scripting language.

Instead of learning predefined abilities, players create magical phenomena from scratch by combining:
- shapes
- elements
- movement
- logic
- behavior

A fireball is not a spell.  
It is the result of code.

---

# Concept

In **HexRuntime**, magic behaves like a programmable system.

Players write scripts such as:

```txt
create sphere
size 2
element fire
launch forward speed 10
```

The engine interprets the script and simulates the spell in real time.

Mana cost is calculated dynamically based on:
- commands used
- complexity
- size
- behavior
- computational cost

Efficient code creates efficient magic.

---

# Core Features

- Custom spell programming language
- Dynamic mana cost system
- Emergent gameplay
- Physics-based magic
- Runtime spell interpretation
- Save/load spell system
- Modular spell architecture

---

# Example Spells

## Fireball

```txt
create sphere
size 2
element fire
launch forward speed 10
```

---

## Ice Shield

```txt
create sphere
size 1
element ice
orbit self
```

---

## Meteor

```txt
create sphere
size 10
element fire
launch down speed 40
```

---

# Architecture

```txt
Player Script
↓
Parser
↓
Commands / AST
↓
Magic Runtime
↓
Entity Creation
↓
Physics Simulation
↓
Rendering
```

# Design Philosophy

The goal is NOT to create realistic programming.

The goal is to make programming feel like:
- writing rituals
- engineering magical systems
- hacking reality

The language should be:
- simple to learn
- hard to master
- expressive
- modular

---

# Long-Term Vision

Future systems may include:
- variables
- conditions
- loops
- spell libraries
- magical debugging
- spell corruption
- runtime instability
- recursive magic
- programmable familiars

---

# Example Internal Runtime

```txt
create sphere
```

↓

```txt
COMMAND_CREATE
TYPE_SPHERE
```

↓

```txt
Entity {
    shape: sphere
}
```

---

# Project Goal

To create a game where:
- creativity matters more than levels
- optimization matters more than stats
- players invent spells the developers never predicted

---

# Status

Early prototype / pre-production.

---

# Author

Danilo Balbino
