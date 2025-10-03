# 1. Create list of 10 routes
routes = ["Nairobi-Mombasa", "Kisumu-Eldoret", "Nakuru-Nairobi", "Mombasa-Kilifi",
          "Thika-Nakuru", "Eldoret-Kakamega", "Nairobi-Kisumu", "Kakamega-Busia",
          "Garissa-Mombasa", "Nairobi-Naivasha"]

print("Routes:", routes)

# 2. Append & remove
routes.append("Isiolo-Marsabit")
routes.remove("Garissa-Mombasa")
print("\nUpdated Routes:", routes)

# 3. Sort alphabetically & reverse
routes.sort()
routes.reverse()
print("\nSorted & Reversed:", routes)

# 4. Count routes starting with "N"
count_N = sum(r.startswith("N") for r in routes)
print("\nRoutes starting with N:", count_N)

# 5. List comprehension: routes longer than 10 chars
long_routes = [r for r in routes if len(r) > 10]
print("\nRoutes longer than 10 characters:", long_routes)