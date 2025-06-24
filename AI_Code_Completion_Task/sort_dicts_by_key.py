# --- Manual Implementation ---
def sort_by_key(data, key):
    """
    Sorts a list of dictionaries by a specified key.

    Parameters:
        data (list): List of dictionaries.
        key (str): Key to sort by.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: x.get(key, None))


# --- AI-Suggested Implementation (via GitHub Copilot or Tabnine) ---
def copilot_sort(data, key):
    """
    Sorts dictionaries assuming all contain the given key (no error handling).
    """
    return sorted(data, key=lambda d: d[key])


# --- Sample Dataset to Test the Functions ---
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# --- Test Output ---
print("Manual Implementation:", sort_by_key(data, 'age'))
print("Copilot Implementation:", copilot_sort(data, 'age'))
