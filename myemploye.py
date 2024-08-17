import json
import csv

class Employee:
    def __init__(self, name, age, department, email, phoneno):
        self.name = name
        self.age = age
        self.department = department
        self.email = email
        self.phoneno = phoneno

    def write_file(self):
        
        with open("myemployee.txt", "a") as file:
            file.write(f'Name: {self.name}\n')
            file.write(f'Age: {self.age}\n')
            file.write(f'Department: {self.department}\n')
            file.write(f'Email: {self.email}\n')
            file.write(f'Phoneno: {self.phoneno}\n')
            file.write('\n')  

       
        with open("myemployee.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.name, self.age, self.department, self.email, self.phoneno])

       
        try:
            with open('employee.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []

        data.append({
            "Name": self.name,
            "Age": self.age,                        # i have appended detain by detail a dict in list
                                                     #so that i can delete dict when i give name parameter
            "Department": self.department,
            "Email": self.email,
            "Phoneno": self.phoneno
        })

        with open('employee.json', 'w') as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def read_txt():
        with open("myemployee.txt", "r") as file:
            print(file.read())

    @staticmethod
    def read_csv():
        with open("myemployee.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    @staticmethod
    def read_json():
        with open("employee.json", "r") as file:
            data = json.load(file)
            for entry in data:
                print(entry)

    @staticmethod
    def update_file(old, new):
        with open("myemployee.txt", "r") as file:
            lines = file.readlines()

        with open("myemployee.txt", "w") as file:
            for line in lines:
                file.write(line.replace(old, new))

        with open("myemployee.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open("myemployee.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow([new if cell == old else cell for cell in row])

        with open("employee.json", "r") as file:
            data = json.load(file)

        for entry in data:
            for key in entry:
                if entry[key] == old:
                    entry[key] = new

        with open("employee.json", "w") as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def delete_items(namee):
        
        with open("myemployee.txt", "r") as file:
            lines = file.readlines()

        with open("myemployee.txt", "w") as file:
            skip = False
            for line in lines:
                if line.startswith(f'Name: {namee}'):
                    skip = True
                elif skip and line.strip() == '':
                    skip = False
                elif not skip:
                    file.write(line)       #written nly lines of user not mentioned in parameter

        with open("myemployee.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row and row[0] != namee] 

        with open("myemployee.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)


        with open("employee.json", "r") as file:
            data = json.load(file)

        data = [entry for entry in data if entry.get("Name") != namee]

        with open("employee.json", "w") as file:
            json.dump(data, file, indent=2)

def main():
    print("1 is to write \n2 is to read from text \n3 is to read from csv \n4 is to read from json \n5 is to update files \n6 is to delete a record")
    user_input = int(input("Enter 1/2/3/4/5/6:"))

    if user_input == 1:
        name = input("Enter your name :")
        age = int(input("Enter your age:"))
        department = input("Enter your department:")
        email = input("Enter your email:")
        phoneno = input("Enter your phone number:")
        employee = Employee(name, age, department, email, phoneno)
        employee.write_file()
    elif user_input == 2:
        Employee.read_txt()
    elif user_input == 3:
        Employee.read_csv()
    elif user_input == 4:
        Employee.read_json()
    elif user_input == 5:
        key1 = input("Enter key to change: ")
        value1 = input("Enter value to write:")
        Employee.update_file(key1, value1)
    elif user_input == 6:
        name1 = input("Enter the name of the person whose details you want to delete:")
        Employee.delete_items(name1)

main()








# import json
# import csv
# class Employee:
 
#     def __init__(self, name, age, department, email, phoneno):
#         self.name = name
#         self.age = age
#         self.department = department
#         self.email = email
#         self.phoneno = phoneno
       
 
#     def write_file(self):
#         with open("myemployee.txt","a") as file:
#             file.write(f'Name: {self.name}\n')
#             file.write(f'Age: {self.age}\n')
#             file.write(f'Department: {self.department}\n')
#             file.write(f'Email: {self.email}\n')
#             file.write(f'Phoneno: {self.phoneno}\n')
#         with open("myemployee.csv","a") as file:
#             writer = csv.writer(file)
#             writer.writerow([self.name,self.age,self.department,self.email,self.phoneno])
        
#         person_dict = {"Name": self.name,
#                         "Age": self.age,
#                         "Department": self.department,
#                         "Email":self.email,
#                         "Phoneno":self.phoneno,
#                         }
#         with open('employee.json', 'w') as file:
#             json.dump(person_dict,file)  
            
#     @staticmethod      #i have done this so that i donot need to make any object of Employee
#                        #it doesnot need self
#     def read_txt():
#         with open("myemployee.txt","r") as file:
#             a=file.read()
#             print(a)
    
#     @staticmethod
#     def read_csv():
#         with open("myemployee.csv","r") as file:
#                 reader = csv.reader(file)
#                 for row in reader:
#                    print(row)
    
#     @staticmethod
#     def read_json():
#         with open("employee.json","r") as file:
#             data=json.load(file) 
#             print(data)    
            
#     def update_file(old_value,new_value):
#         with open("myemployee.txt","r") as file:
#             content=file.read()
#             updated_content = content.replace(old_value,new_value)
#         with open("myemployee.txt","w")as file:     
#             file.write(updated_content)
            
#         with open("myemployee.csv", mode='r', newline='') as file:
#             reader = csv.reader(file)
#             rows = list(reader)
#             for row in rows:
#                 row[:]=[new_value if cell == old_value else cell for cell in row]
#         with open("myemployee.csv", mode='w', newline='') as file:
#                 writer = csv.writer(file)
#                 writer.writerows(rows)     
#         with open("employee.json", "r") as file:
#             data = json.load(file)
#         for key in data:
#            if data[key] == old_value:
#             data[key] = new_value
#         with open("employee.json", "w") as file:
#            json.dump(data, file,indent=2) # i provided indent ---provides indentation prettyprint
           
           
#     def delete_items(namee):
        
#         with open("myemployee.txt",mode='r')as file:
#             file.read()
            
#         with open("myemployee.csv", mode='r') as file:
#             reader = csv.reader(file)
#             rows = list(reader)
#         with open("myemployee.csv", mode='w') as file:
#             writer = csv.writer(file)
#             for row in rows:
#                if row and row[0] != namee:
#                   writer.writerow(row)

    
#         with open("employee.json", "r") as file:
#             data = json.load(file)
    
#         if data.get("Name") == namee:
#             data.clear() 
        
#         with open("employee.json", "w") as file:  
#             json.dump(data, file, indent=4) 
            
        
#         with open("myemployee.txt", "r") as file: # i have basically enumerate lines(next line)
#             lines = file.readlines()             #The if not condition ensures t (the current line or the previous line ) are excluded from the new list
#         lines = [line for i, line in enumerate(lines)
#              if not (line.startswith(f"Name: {namee}") or 
#                      (i > 0 and lines[i-1].startswith(f"Name: {namee}")))]           
                   
#         with open("myemployee.txt", "w") as file:
#             file.writelines(lines)

                            
            
# def main():
#     print("1 is to write \n 2 is to read from text \n 3 is to read from csv \n 4 is to read from json \n 5 is to update to files \n 6 is to delete a record")
#     user_input=int(input("Enter 1/2/3/4/5/6:"))
    
#     if user_input == 1:
#         name=input("Enter your name :")
#         age=int(input("Enter your age:"))
#         department=input("Enter your department:")
#         email=input("Enter your email")
#         phoneno=input("Enter your phoneno:")
#         employee = Employee(name,age,department,email,phoneno)
#         employee.write_file() 
#     if user_input== 2:
#         Employee.read_txt()
#     if user_input== 3:
#         Employee.read_csv()  
#     if user_input==4:
#         Employee.read_json()     
#     if user_input==5:
#         key1=input("Enter key to change: ")
#         value1=input("Enter value to write:")
#         Employee.update_file(key1,value1)  
#     if user_input==6:
#         name1=input("Enter name whoes details which you want to del :")    
#         Employee.delete_items(name1)       
# main()
        
   

            
            
        
        
        
        
        
    