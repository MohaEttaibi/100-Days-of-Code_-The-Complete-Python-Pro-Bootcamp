# Beginner 

# Grading Program
# student_score = {"harry":81, "Ron":78, "Hermione":99, "Draco":74,"Neville":62}

# student_grades = {}

# for student in student_score:
#     score = student_score[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# print(student_grades)


# Dictionary in List
# travel_log = [
#     {
#         "country":"France",
#         "visits":12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]

# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# Auction Program
# pthontutor.com
# Thonny IDE
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def find_max_bid(record):
    max_bid = 0
    winner = ""
    for bid in record:
        bid_amount = record[bid]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bid
    print(f"The winner is {winner} with a bid of ${max_bid}.")

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $ "))
    bids[name] = price
    bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if bidder == "no":
        bidding_finished = True
        find_max_bid(bids)
    # elif bidder == "yes":
    #     clear() # function in repl.it
    