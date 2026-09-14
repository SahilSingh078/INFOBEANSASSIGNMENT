def book_appointment():
    data = {}
    data["appointment_id"] = input("enter appointment id :")
    data["patient_id"] = input("enter patientid id :")
    data["doctor_id"] = input("enter doctor id :")
    data["Appointment Date"] = input("enter Appointment Date (DD-MM-YYYY) :")
    data["Appointment Time"] = input("enter Appointment time (HH:MM) :")

    return data

def show_appointments(appointment_data):
    return appointment_data