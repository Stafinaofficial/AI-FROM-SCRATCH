# Lesson 5: Vectors – The Language of AI

> **Big Idea:** A vector is a numerical representation of an object. AI understands objects by representing them as vectors of numbers.

---

# Learning Objectives

After completing this lesson, I should be able to:

* Explain what a vector is from an AI perspective.
* Understand why vectors are used in Artificial Intelligence.
* Represent real-world objects as vectors.
* Explain how vectors become the input to AI models.
* Understand the concept of feature engineering.

---

# 1. What is a Vector?

Traditional mathematics defines a vector as a quantity with magnitude and direction.

In Artificial Intelligence, it is more useful to think of a vector as:

> **A collection of numbers that describes an object.**

Examples:

Location

(12.8415, 80.1532)

Person

(170, 60, 19)

These numbers represent information.

The computer only sees the numbers.

Humans assign meaning to each value.

---

# 2. Why Does AI Use Vectors?

Computers cannot understand concepts like:

* Cat
* Dog
* Doctor
* Student

Instead, everything is converted into numbers.

Example:

Person

↓

(Height, Weight, Age)

↓

(170, 60, 19)

The AI processes only the numerical values.

---

# 3. Objects Can Be Represented as Vectors

Examples:

Person

(Height, Weight, Age)

House

(Area, Bedrooms, Bathrooms, Age)

Movie

(Action Score, Romance Score, Rating, Duration)

Patient

(Age, Genetics, Scan Score, Sugar Intake)

Every object becomes a vector.

---

# 4. Feature Engineering

Choosing which values should be included in a vector is called **Feature Engineering**.

Example:

For diabetes prediction, possible features include:

* Age
* Family History
* Blood Glucose
* HbA1c
* BMI
* Blood Pressure
* Sugar Intake

Different engineers may choose different features depending on the problem.

There is often more than one correct representation.

---

# 5. AI Connection

When a user types:

Robot

The data goes through several stages.

Text

↓

Unicode

↓

Tokens

↓

Token IDs

↓

Embedding Vectors

↓

Transformer

↓

Prediction

The transformer never directly understands the word "Robot."

It operates on vectors.

---

# 6. Similarity

Objects with similar vectors are often considered similar.

Example:

Dog

(1.2, 0.8, 2.1)

Wolf

(1.3, 0.9, 2.0)

These vectors are close together.

The AI interprets them as similar.

One of the main goals in AI is learning useful vector representations.

---

# 7. Hands-on Exercise

Python Code:

```python
person = [170, 60, 19]

print("Person Vector:", person)

print("Height:", person[0])
print("Weight:", person[1])
print("Age:", person[2])
```

Observation:

Python stores only a list of numbers.

The meaning of each number comes from the programmer.

---

# 8. Key Takeaways

* A vector is a numerical description of an object.
* AI understands vectors instead of human concepts.
* Everything can be represented as vectors.
* Choosing useful features is called Feature Engineering.
* Better feature representation often leads to better AI models.

---

# AI Research Insight

Modern AI models represent words, images, videos, sounds, and even proteins as vectors.

These vectors may contain hundreds or thousands of numerical values.

Learning good vector representations is one of the most important problems in Artificial Intelligence.

---

# Research Questions

* How does AI compare two vectors?
* What makes two vectors similar?
* Why do ChatGPT and other LLMs convert words into vectors?
* How many numbers should a vector contain?
* How are embedding vectors learned automatically?

---

# My Insights

Today I realized that:

* AI never understands objects directly.
* Everything must first become a vector.
* A vector is simply a structured collection of numbers.
* Designing a good vector representation is itself an engineering challenge.
* Machine Learning begins with representing the real world as numerical data.

---

# Summary

Objects

↓

Features

↓

Vectors

↓

Mathematics

↓

AI Models

↓

Predictions

**Every modern AI system begins by converting the world into vectors.**
