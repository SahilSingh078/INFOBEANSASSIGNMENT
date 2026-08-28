'''
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--
A multi-specialty hospital is currently maintaining patient records manually in registers. As the number of patients is increasing, it has become difficult to search, update, and manage records efficiently.
The hospital management has decided to develop a simple Patient Record Management System using Python. The system should store patient information in a nested dictionary where:
Key → Patient ID
Value → Dictionary containing patient details
Each patient record should contain:
Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program
Display the following menu repeatedly until the user chooses Exit.
=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================
1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit
Functional Requirements
1. Add New Patient
Accept the following information from the user:
Patient ID
Patient Name
Age
Gender
Disease
Doctor Name
Store the record in the nested dictionary.
Validation:
If the Patient ID already exists, display:
Patient ID already exists.
2. Search Patient
Accept Patient ID from the user.
If the patient exists, display complete information.
Sample Output
Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma
If Patient ID is not found:
Patient Record Not Found
3. Update Patient Disease
Accept Patient ID.
If found:
Ask for new disease.
Update the disease information.
Sample Output
Disease Updated Successfully
4. Delete Patient Record
Accept Patient ID.
If found:
Remove the patient record.
Sample Output
Patient Record Deleted Successfully
Otherwise:
Patient Not Found
5. Display All Patients
Display all patient records in a formatted manner.
Sample Output
--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients
Display the total number of patients currently stored.
Sample Output
Total Patients : 25
7. Display Patients By Disease
Accept a disease name from the user.
Display all patients suffering from that disease.
Sample Output
Enter Disease : Fever
101  Ajay
108  Aman
115  Neha
If no patient is found:
No Patient Found
8. Display Oldest Patient
Find and display the patient having the highest age.
Sample Output
Oldest Patient Details
Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient
Find and display the patient having the minimum age.
Sample Output
Youngest Patient Details
Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit
Terminate the application.
Sample Output
Thank You For Using Hospital Patient Management System
'''

patients = {}
while True:
    print()
    print("1. ADD NEW PATIENT")
    print("2. SEARCH PATIENT")
    print("3. UPDATE PATIENT DISEASE")
    print("4. DELETE PATIENT RECORD")
    print("5. DISPLAY ALL PATIENTS")
    print("6. COUNT TOTAL PATIENTS")
    print("7. DISPLAY PATIENTS BY DISEASE")
    print("8. DISPLAY OLDEST PATIENT")
    print("9. DISPLAY YOUNGEST PATIENT")
    print("10. EXIT")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("\n1. ADD NEW PATIENT")
            n = int(input("Enter number of patients: "))
            for i in range(n):
                patient_id = int(input("Enter New Patient ID: "))
                while patient_id in patients:
                    print("Patient ID already exists.")
                    patient_id = int(input("Enter New Patient ID again: "))
                name = input("Enter Patient Name: ")
                age = int(input("Enter Age: "))
                gender = input("Enter Gender: ")
                disease = input("Enter Disease: ")
                dr_name = input("Enter Doctor Name: ")
                patients[patient_id] =  {"Name": name,"Age": age,"Gender": gender,"Disease": disease, "Doctor Name": dr_name}
                print("Patient Added Successfully")
        case 2:
            print("\n2. SEARCH PATIENT")
            if len(patients)==0:
                print("Please Add Patient First")
            else:
                search = int(input("Enter Patient ID to search: "))
                found = False
                for k, v in patients.items():
                    if search == k:
                        print("Patient ID :", k)
                        print("Name       :", v["Name"])
                        print("Age        :", v["Age"])
                        print("Gender     :", v["Gender"])
                        print("Disease    :", v["Disease"])
                        print("Doctor     :", v["Doctor Name"])
                        found = True
                if found == False:
                    print("Patient Record Not Found")
        case 3:
            print("\n3. UPDATE PATIENT DISEASE")
            if len(patients)==0:
                print("Please Add Patients First")
            else:
                patient_id = int(input("Enter Patient ID: "))
                while patient_id not in patients:
                    print("No Patient Found!!!!!!")
                    patient_id = int(input("Enter Patient ID: "))
                print("Patient's current disease:", patients[patient_id]["Disease"])
                disease_new = input("Enter New Disease: ")
                patients[patient_id].update({"Disease": disease_new})
                print("Disease Updated Successfully")

        case 4:
            print("\n4. DELETE PATIENT RECORD")
            if len(patients)==0:
                print("Please Add Patients First")
            else:
                patient_id = int(input("Enter Patient ID: "))
                while patient_id not in patients:
                    print("No Such Patient Record Found")
                    patient_id = int(input("Enter Patient ID: "))
                del patients[patient_id]
                print("Patient Record Deleted Successfully")

        case 5:
            print("\n5. DISPLAY ALL PATIENTS")
            if len(patients) == 0:
                print("No Patient Records Available")
            else:
                for k, v in patients.items():
                    print("--------------------------------")
                    print("Patient ID :", k)
                    print("Name       :", v["Name"])
                    print("Age        :", v["Age"])
                    print("Gender     :", v["Gender"])
                    print("Disease    :", v["Disease"])
                    print("Doctor     :", v["Doctor Name"])
                    print("--------------------------------")
        case 6:
            print("\n6. COUNT TOTAL PATIENTS")
            print("Total Patients :", len(patients))
        case 7:
            print("\n7. DISPLAY PATIENTS BY DISEASE")
            if len(patients)==0:
                print("Please Add Patients First")
            else:
                disease = input("Enter disease name: ")
                for k, v in patients.items():
                    if v["Disease"].lower() == disease.lower():
                        print(k, "  ", v["Name"])
        case 8:
            print("\n8. Dispaly Oldest Patient")
            if len(patients)==0:
                print("Please Add Patients First")
            else:
                old = 0
                for k,v in patients.items():
                    if v["Age"]> old:
                        old = v["Age"]
                        oldest = k
                print("--------------------------------")
                print("Patient ID :", old)
                print("Name       :", patients[oldest]["Name"])
                print("Age        :", patients[oldest]["Age"])
                print("Gender     :", patients[oldest]["Gender"])
                print("Disease    :", patients[oldest]["Disease"])
                print("Doctor     :", patients[oldest]["Doctor Name"])
                print("--------------------------------")
        case 9:
            print("\n9. Display Youngest Patient")
            if len(patients)==0:
                print("Please Add Patients First")
            else:
                young = 150
                for k,v in patients.items():
                    if v["Age"]<young:
                        young = v["Age"]
                        youngest = k
                print("--------------------------------")
                print("Patient ID :", youngest)
                print("Name       :", patients[youngest]["Name"])
                print("Age        :", patients[youngest]["Age"])
                print("Gender     :", patients[youngest]["Gender"])
                print("Disease    :", patients[youngest]["Disease"])
                print("Doctor     :", patients[youngest]["Doctor Name"])
                print("--------------------------------")
        case 10:
            print("\nThank You For Using Hospital Patient Management System")
            break
        case _:
            print("PLEASE CHOOSE APPROPRIATE OPTION!!!!!!!!!!")