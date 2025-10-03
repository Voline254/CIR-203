routes = ["Nairobi-Mombasa", "Kisumu-Eldoret", "Nakuru-Nairobi", "Mombasa-Kilifi",
          "Thika-Nakuru", "Eldoret-Kakamega", "Nairobi-Kisumu", "Kakamega-Busia",
          "Garissa-Mombasa", "Nairobi-Naivasha"]

print("Routes:", routes)

routes.append("Isiolo-Marsabit")
routes.remove("Garissa-Mombasa")
print("\nUpdated Routes:", routes)

routes.sort()
routes.reverse()
print("\nSorted & Reversed:", routes)

count_N = sum(r.startswith("N") for r in routes)
print("\nRoutes starting with N:", count_N)

long_routes = [r for r in routes if len(r) > 10]

print("\nRoutes longer than 10 characters:", long_routes)
