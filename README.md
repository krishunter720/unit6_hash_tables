
# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment demonstrated how Python dictionaries worked as hash tables by using a store inventory management system.

## Learning Objectives

- Inserted key-value pairs
- Retrieved values efficiently
- Updated existing values
- Removed entries
- Tested edge cases
- Examined how hashing and collisions affected performance

## Application: Store Inventory System

I created a store inventory system using a Python dictionary. Product IDs were used as keys, and inventory quantities were stored as values.

## Completed Operations

1. Created an empty dictionary and added five products.
2. Retrieved quantities for existing product IDs.
3. Updated the quantity of product P200 from 10 to 20.
4. Deleted product P400 from the inventory.
5. Displayed the inventory before and after updates and deletions.

## Edge Case Testing

I tested several situations to make the program more reliable:

- Looked up a product ID that did not exist using `get()`.
- Attempted to remove a missing product using `pop()` with a default value.
- Created an empty dictionary and attempted to look up a product in it.

These tests showed how missing keys and empty dictionaries could be handled without causing the program to crash.

## Hash Tables and Performance

Python dictionaries used hash tables to store and retrieve key-value pairs. A hash function helped determine where a key was stored. A collision occurred when two different keys mapped to the same location. Collisions could require additional work to find the correct value and could reduce performance. Dictionary operations generally provided average O(1) insertion, lookup, and deletion times.

## Program Results

The program successfully completed the insertion, lookup, update, deletion, and edge case operations. The final inventory contained P100, P200, P300, and P500.
