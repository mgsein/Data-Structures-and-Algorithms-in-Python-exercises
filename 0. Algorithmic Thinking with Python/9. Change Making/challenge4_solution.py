def make_change(target_amount):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]  # Order is important!
    kyat_count = 0  # Initialise count
    values = []  # Store values here
    for kyat in denominations:
        while target_amount >= kyat:  # Use the current coin until its value is too large
            target_amount -= kyat  # Decrease the remaining amount
            values.append(kyat)  # Make a note of which coin was used
            kyat_count += 1  # Increase the coin count
    return kyat_count, values


print(make_change(24))  # 3: 20kyat + 2kyat + 2kyat
print(make_change(163))  # 5: 100kyat + 50kyat + 10kyat + 2kyat + 1kyat
