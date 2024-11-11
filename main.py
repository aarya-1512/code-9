class Patient:
    def __init__(self, name, age, gender, blood_pressure, temperature):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_pressure = blood_pressure
        self.temperature = temperature

    def display_patient_info(self):
        """Displays the patient's information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Blood Pressure: {self.blood_pressure}")
        print(f"Temperature: {self.temperature:.1f}°C")
        print()

    def is_hypertensive(self):
        """Checks if the patient is hypertensive."""
        systolic, diastolic = self.blood_pressure
        return systolic >= 140 or diastolic >= 90

    def is_feverish(self):
        """Checks if the patient has a fever."""
        return self.temperature >= 37.5


# Function to take user input and create a Patient object
def get_patient_info():
    # Get patient details from user
    name = input("Enter patient's name: ")
    age = int(input("Enter patient's age: "))
    gender = input("Enter patient's gender (Male/Female): ")
    
    # Get systolic and diastolic pressure in a single input, split by comma
    blood_pressure_input = input("Enter blood pressure: ")
    systolic, diastolic = map(int, blood_pressure_input.split(','))  # Split and convert to integers
    blood_pressure = (systolic, diastolic)
    
    temperature = float(input("Temperature: "))
    
    # Return a Patient instance with the input data
    return Patient(name, age, gender, blood_pressure, temperature)

# Get information for two patients from the user
print("Enter details for Patient 1:")
patient1 = get_patient_info()

print("\nEnter details for Patient 2:")
patient2 = get_patient_info()

# Display patient information and health conditions in a more compact format
# Displaying results together for both patients

print(f"\nPatient 1 is Hypertensive: {patient1.is_hypertensive()}")
print(f"Patient 1 is Feverish: {patient1.is_feverish()}")
print()  # Blank line between patients

print(f"Patient 2 is Hypertensive: {patient2.is_hypertensive()}")
print(f"Patient 2 is Feverish: {patient2.is_feverish()}")
