# 1. Create patient tuple
patient = ("John Doe", 45, "120/80", 72)
print("Patient tuple:", patient)

# 2. Access & print age and heart rate
print("\nAge:", patient[1], "| Heart Rate:", patient[3])

# 3. Why tuples? 
# Tuples are immutable, making them safe for storing unchangeable medical records.

# 4. Convert to list, update heart rate, back to tuple
patient_list = list(patient)
patient_list[3] = 75  # update heart rate
patient = tuple(patient_list)
print("\nUpdated patient tuple:", patient)

# 5. Tuple of 5 patients
patients = (
    ("John Doe", 45, "120/80", 75),
    ("Alice Smith", 50, "130/85", 80),
    ("Peter Kim", 60, "140/90", 70),
    ("Mary Ann", 35, "110/75", 68),
    ("David Lee", 40, "125/80", 72)
)

names = [p[0] for p in patients]
print("\nAll patient names:", names)