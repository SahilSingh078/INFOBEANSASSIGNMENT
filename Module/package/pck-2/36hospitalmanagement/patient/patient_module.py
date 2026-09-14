def add_patient():
    data = {}
    data["patient_name"] = input("enter name :")
    data["age"] = int(input("enetr age :"))
    data["gender"] = input("enter gender :")
    data["disease"] = input("enter disease :")
    data["mo_no"] = input("enter mobile no. :")

    return data

def display_patient(patient_data):
    return patient_data

def search_patient(patient_data,id):
    if id in patient_data:
        return patient_data[id]
    else :
        return "Patient not found" 


        

