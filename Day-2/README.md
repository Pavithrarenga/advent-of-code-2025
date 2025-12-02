# Day 2 - Gift Shop

This folder contains my solution to Advent of Code 2025 - Day 2: Gift Shop.

---

## Puzzle synopsis

The gift shop has several **ranges of product IDs**.
Some IDs are *invalid* because the young Elf typed silly repeating patterns.

### **What counts as an invalid ID?**

An ID is invalid if the **entire number** is made by repeating the same sequence of digits **at least twice**.

Examples:

* **11** → "1" repeated 2 times
* **6464** → "64" repeated 2 times
* **123123123** → "123" repeated 3 times
* **1111111** → "1" repeated 7 times
* **1010** → "10" repeated 2 times

IDs do **not** contain leading zeros.

### **Input Format**

Your puzzle input is one long line containing ranges like:

```
11-22,95-115,998-1012,...
```

Each range includes **all integers from the low end to the high end (inclusive)**.

---

## **Goal**

### **Part 1**

(Handled by helper function, but Part 2 supersedes it.)
Identify IDs where the number is exactly **one chunk repeated twice**.

### **Part 2**

Find **all** IDs that consist of any chunk repeated **two or more times**,
and **sum them** across all ranges.

This is the part the final script computes.

---

## **How I Solved It**

* I read the input line and split it into ranges.
* For each range, I check **every number**.
* For each number, I test every possible chunk size to see if repeating that chunk rebuilds the full number.
* If a number is made entirely of repeated chunks, it is **invalid** and added to the running total.
* Finally, the script prints the total for:

  * the example input
  * or a file such as `input1.txt`

The solution intentionally checks for numeric IDs that are made by repeating a digit-sequence two or more times (Part Two rules). The implementation includes helper functions to detect Part 1 and Part 2 invalid IDs; the main script demonstrates the example and reads `input.txt`.

Files

- `solution.py` - Python script that implements the Part Two checker and prints the example result and attempts to compute totals from `input.txt`.
- `input.txt` - puzzle input (single-line csv of ranges).

Result (my input)
- Part 1 answer: 23039913998
- Part 2 answer: 35950619148

