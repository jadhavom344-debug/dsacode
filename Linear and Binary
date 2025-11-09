# Program: Linear and Binary Search for Customer Account IDs

# Linear Search Function
def linear_search(customer_ids, target_id):
    for i in range(len(customer_ids)):
        if customer_ids[i] == target_id:
            return f"Customer ID {target_id} found at position {i}"
    return f"Customer ID {target_id} not found"

# Binary Search Function
def binary_search(customer_ids, target_id):
    low = 0
    high = len(customer_ids) - 1

    while low <= high:
        mid = (low + high) // 2

        if customer_ids[mid] == target_id:
            return f"Customer ID {target_id} found at position {mid}"
        elif customer_ids[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return f"Customer ID {target_id} not found"

# Main Program
customer_ids = [101, 105, 110, 120, 125, 130, 140]
target_id = int(input("Enter the customer ID to search: "))

print("\n--- Linear Search ---")
print(linear_search(customer_ids, target_id))

print("\n--- Binary Search ---")
# Binary search works on sorted data
print(binary_search(sorted(customer_ids), target_id))
