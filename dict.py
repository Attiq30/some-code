
d = {}

while True:
    try:
        i = int(input("Enter 1 to add an email, enter 2 to delete, enter 3 to show all data, or enter 4 to exit: "))
        
        if i == 1:
                    email = input("Enter email you want to add: ")
                    if email in d:
                        print("Email already exists.")
                    else:
                        info = {}
                        name = input("Enter name: ")
                        age = input("Enter age: ")
                        gender = input("Enter gender: ")

                        info["name"] = name
                        info["age"] = age
                        info["gender"] = gender

                        
                        d[email] = info

                        print(f"User information added for {email}.")

        elif i == 2:
                    e = input("Enter email to delete: ")
                    if e in d:
                        del d[e]
                        print(f"User information for {e} deleted.")
                    else:
                        print(f"Email {e} not found in the dictionary.")

        elif i == 3:
                    
                    print("All data in the dictionary:")
                    for email, info in d.items():
                        print(f"Email: {email}, User Information: {info}")

        elif i == 4:
                
                    break
    except Exception as e:
           print("error")



        
                


