def add_doctor():
    data = {}
    data["doc_id"] = input("enter doctor id:")
    data["doc_name"] = input("enter name :")
    data["Specialization"] = input("enter Specialization:")
    data["experince"] = input("enter experience :")
    data["consultation fees"] = int(input("enter fees :"))

    return data 

def diaplay_doctor(doctor_data):
    return doctor_data
   