import json

# New book to add
new_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 14.99,
    "in_stock": True
}

# ✅ Task 1 — Read inventory and count books
with open("inventory.json", "r") as file:
    inventory = json.load(file)

print("Total books:", len(inventory))


# ✅ Task 2 — Add new book and save (indent = 4)
inventory.append(new_book)

with open("inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)


# ✅ Task 3 — Read updated file and display books
with open("inventory.json", "r") as file:
    updated_inventory = json.load(file)

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")
