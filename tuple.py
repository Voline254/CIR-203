patient = ("John Doe", 45, "120/80", 72)
print("Patient tuple:", patient)

print("\nAge:", patient[1], "| Heart Rate:", patient[3])

patient_list = list(patient)
patient_list[3] = 75  # update heart rate
patient = tuple(patient_list)
print("\nUpdated patient tuple:", patient)

patients = (
    ("John Doe", 45, "120/80", 75),
    ("Alice Smith", 50, "130/85", 80),
    ("Peter Kim", 60, "140/90", 70),
    ("Mary Ann", 35, "110/75", 68),
    ("David Lee", 40, "125/80", 72)
)

names = [p[0] for p in patients]

print("\nAll patient names:", names)
