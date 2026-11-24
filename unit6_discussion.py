
"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # The inventory dictionary uses product IDs as keys
    # and the quantity of each product as its value.
    # Python hashes each key to help locate its stored value.
    inventory = {}

    inventory["P100"] = 25
    inventory["P200"] = 10
    inventory["P300"] = 40
    inventory["P400"] = 15
    inventory["P500"] = 30

    print("\n=== INSERT OPERATIONS ===")
    print("Initial inventory:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    # Looking up a key allows the dictionary to locate its value
    # without searching through every inventory item.
    print("\n=== LOOKUP OPERATIONS ===")

    print("Quantity of P100:", inventory["P100"])
    print("Quantity of P300:", inventory["P300"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Inventory before update:")
    print(inventory)

    # Assigning a new value to an existing key replaces its old value.
    # It does not create a second entry with the same key.
    inventory["P200"] = 20

    print("Inventory after updating P200:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Inventory before deletion:")
    print(inventory)

    # The pop() method removes the specified key and its value.
    inventory.pop("P400")

    print("Inventory after deleting P400:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Looking up a product that does not exist.
    # get() returns the default message instead of causing a KeyError.
    missing_product = inventory.get("P999", "Product not found")
    print("Looking up P999:", missing_product)

    # Edge case 2: Removing a product that does not exist.
    # pop() with a default value prevents an error.
    removed_product = inventory.pop("P999", "Product was not found")
    print("Removing P999:", removed_product)

    # Edge case 3: Working with an empty dictionary.
    empty_inventory = {}
    print("Empty inventory:", empty_inventory)
    print("Looking up an item in empty inventory:",
          empty_inventory.get("P100", "No products available"))

    print("\n=== FINAL INVENTORY ===")
    print(inventory)


if __name__ == "__main__":
    main()
