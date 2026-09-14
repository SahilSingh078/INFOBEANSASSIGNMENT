def generate_bill():
    data = {}
    data["patient_id"] = input("eneter patient id :")
    data["consultation charge"] = int(input("enetr Consultation Charges"))
    data["medicine cost"] = int(input("enetr medicine cost :"))
    data["Test charges"] = int(input("enetr test charges :"))

    bill = data["consultation charge"] + data["medicine cost"] + data["Test charges"]

    return bill