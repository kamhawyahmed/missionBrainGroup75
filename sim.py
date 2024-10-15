def patient_view():
    health_questions = [
        "  - Are you experiencing any pain? (y/n): ",
        "  - Do you have any difficulty breathing? (y/n): ",
        "  - Are you feeling dizzy? (y/n): ",
        "  - Do you have any swelling? (y/n): ",
        "  - Are you experiencing any nausea? (y/n): "
    ]

    responses = {}
    for question in health_questions:
        response = input(question)
        responses[question] = response
    return responses


def doctor_view():
    patient_data = {}

    while True:
        mode = input("Enter mode (send/retrieve/exit): ").strip().lower()

        if mode == "send":
            patient_id = input("  - Enter patient ID: ").strip()
            firstName = input("  - Enter first name: ").strip()
            lastName = input("  - Enter last name: ").strip()
            phoneNumber = input("  - Enter phone number: ").strip()
            secondaryPhoneNumber = input(
                "  - Enter secondary phone number (optional): ").strip()
            email = input("  - Enter email (optional): ").strip()
            admissionDate = input(
                "  - Enter admission date (YYYY-MM-DD): ").strip()
            dischargeDate = input(
                "  - Enter discharge date (YYYY-MM-DD): ").strip()
            contactDate = input(
                "  - Enter contact date (YYYY-MM-DD): ").strip()
            admissionReason = input("  - Enter admission reason: ").strip()
            proceduresPerformed = input(
                "  - Enter procedures performed: ").strip()
            diagnosis = input("  - Enter diagnosis: ").strip()
            medicationsGiven = input("  - Enter medications given: ").strip()
            followupInstructions = input(
                "  - Enter follow-up instructions: ").strip()
            authCode = input("  - Enter authorization code: ").strip()
            needsFollowUp = input(
                "  - Needs follow-up? (yes/no): ").strip().lower() == "yes"

            patient_info = (firstName, lastName, phoneNumber,
                            secondaryPhoneNumber, email, admissionDate,
                            dischargeDate, contactDate, admissionReason,
                            proceduresPerformed, diagnosis, medicationsGiven,
                            followupInstructions, authCode, needsFollowUp)

            patient_data[patient_id] = patient_info
            print(f"Patient data for ID {patient_id} stored successfully.\n")

        elif mode == "retrieve":
            patient_id = input("Enter patient ID to retrieve: ").strip()
            if patient_id in patient_data:
                patient_info = patient_data[patient_id]
                print(f"Patient data for ID {patient_id}:")
                print(f"First Name: {patient_info[0]}")
                print(f"Last Name: {patient_info[1]}")
                print(f"Phone Number: {patient_info[2]}")
                print(f"Secondary Phone Number: {patient_info[3]}")
                print(f"Email: {patient_info[4]}")
                print(f"Admission Date: {patient_info[5]}")
                print(f"Discharge Date: {patient_info[6]}")
                print(f"Contact Date: {patient_info[7]}")
                print(f"Admission Reason: {patient_info[8]}")
                print(f"Procedures Performed: {patient_info[9]}")
                print(f"Diagnosis: {patient_info[10]}")
                print(f"Medications Given: {patient_info[11]}")
                print(f"Follow-up Instructions: {patient_info[12]}")
                print(f"Authorization Code: {patient_info[13]}")
                print(f"Needs Follow-up: {patient_info[14]}\n")
            else:
                print(f"No data found for patient ID {patient_id}.\n")

        elif mode == "exit":
            break
        else:
            print("Invalid mode. Please enter 'send', 'retrieve', or 'exit'.")


def main():
    while True:
        view = input("Enter view (patient/doctor/exit): ").strip().lower()

        if view == "patient":
            patient_responses = patient_view()
            print("\nPatient health check responses recorded.")
            for question, response in patient_responses.items():
                print(f"{question}: {response}")
            print("\n")

        elif view == "doctor":
            doctor_view()

        elif view == "exit":
            print("Exiting program.")
            break
        else:
            print("Invalid view. Please enter 'patient', 'doctor', or 'exit'.")


if __name__ == "__main__":
    main()
