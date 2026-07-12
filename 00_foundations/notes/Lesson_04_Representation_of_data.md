# Lesson 4: Representation of Data

> **Big Idea:** A computer understands only binary (0 and 1). Everything else—letters, images, emojis, videos, and audio—is represented as numbers.

---

# Learning Objectives

After this lesson, I should be able to:

* Explain why computers only understand binary.
* Explain how characters are represented.
* Explain how images are stored.
* Understand that meaning comes from interpretation, not from bits themselves.
* Relate these ideas to Artificial Intelligence.

---

# 1. Everything Becomes Numbers

Although humans see:

* Letters
* Images
* Emojis
* Music
* Videos

A computer stores all of them as binary.

Example:

| Human Sees | Computer Stores            |
| ---------- | -------------------------- |
| A          | 65 → Binary                |
| 😊         | Unicode Number → Binary    |
| Image      | Millions of Pixel Values   |
| Music      | Sound Sample Values        |
| Video      | Sequence of Images + Audio |

---

# 2. Bits Have No Meaning

A binary sequence has **no meaning by itself**.

Example:

01000001

Depending on the program reading it, it may represent:

* Number 65
* Character 'A'
* Part of an image
* Part of a machine instruction

**Meaning comes from interpretation.**

---

# 3. Characters

ASCII assigns numbers to characters.

Example:

| Character | Decimal | Binary   |
| --------- | ------- | -------- |
| A         | 65      | 01000001 |
| B         | 66      | 01000010 |
| C         | 67      | 01000011 |
| a         | 97      | 01100001 |

Modern computers use **Unicode**, which supports almost every language and emoji.

---

# 4. Fonts

The computer does **not** store the visual appearance of a letter.

Instead:

Character Code

↓

Font File

↓

Drawing Instructions

↓

Pixels

↓

Screen

Different fonts draw the same character differently.

Example:

* Arial
* Times New Roman
* Cascadia Code

All display the character "A" differently even though the stored character is the same.

---

# 5. Images

An image is **not** stored as a picture.

It is stored as numbers.

Example (Grayscale):

255 255 255 255

255   0   0 255

255   0   0 255

255 255 255 255

Where:

* 255 = White
* 0 = Black

Changing one number changes one pixel.

---

# 6. RGB Images

Each pixel consists of three values:

* Red
* Green
* Blue

Each channel uses **8 bits**.

Therefore:

8 + 8 + 8 = 24 bits per pixel

Possible values per channel:

2⁸ = 256

Total possible colors:

256 × 256 × 256 = 16,777,216

---

# 7. Keyboard to Screen

When a key is pressed, the following happens:

Finger

↓

Keyboard Matrix

↓

Keyboard Controller

↓

Scan Code

↓

USB

↓

Operating System

↓

Unicode Character

↓

Application (VS Code, Browser, etc.)

↓

Font File

↓

GPU

↓

Pixels

↓

Monitor

↓

Human Eyes

↓

Brain Recognizes the Character

**Important:** The keyboard does **not** send ASCII or Unicode directly. It first sends a **scan code** representing the physical key that was pressed.

---

# 8. AI Connection

Humans see:

🐱

The computer receives:

Pixel Values

↓

Matrix of Numbers

↓

Neural Network

↓

Prediction

AI does **not** understand cats directly.

It discovers mathematical patterns in numerical data.

---

# Key Takeaways

* Computers only understand binary.
* Everything inside a computer is represented as numbers.
* Bits have no meaning without interpretation.
* Characters are represented using numerical codes (ASCII/Unicode).
* Fonts determine how characters are drawn.
* Images are matrices of numbers.
* AI operates on numerical representations, not on human concepts.

---

# Research Questions

* How does the operating system translate scan codes into characters?
* How are decimal numbers stored inside a computer?
* How does the GPU convert drawing instructions into pixels?
* How does an AI convert numbers into meaning?
* Why do neural networks use vectors instead of raw numbers?

---

# My Insights

Today I realized that:

* A computer never actually "sees" the letter **A**.
* A computer never actually "sees" a cat.
* Everything inside a computer is transformed into numbers.
* The meaning of those numbers exists because software interprets them and humans understand the final output.
* AI is not magic; it is a sophisticated system that learns patterns from numerical representations.

---

# Summary

**The computer stores numbers.**

**Software interprets those numbers.**

**The monitor displays pixels.**

**The human brain gives those pixels meaning.**
