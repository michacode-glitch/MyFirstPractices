#Imports - datetime
import datetime

# Bienvenida al usuario
print("YOU ARE NOW IN ACCI'S OFFICIAL PAGE\n")
print("To start follow the next steps")
name = input("Please enter your full name: ").title()
print(f"~~~~Hi {name}!! Welcome to AACI~~~~\n")
print("Are you searching for help?\n")

#Ingreso de datos - condicionales
try:
    inp = input("If yes, type; Help\nIf not type; Continue\n").lower().strip()
    
    if inp == "help":
        print("-" * 40)
        print("Great! What are you looking for?\n")
        print("Write under the options, which one you need!!\n-GRADES\n-INSCRIPTION\n-OTHER")
        inp_1 = input().lower().strip()
    
        if inp_1 == "grades":
            
            print("If you want to know your grades on a recently exam")
            print("enter your ACCI-ID (ACCI-ID must be your ID and a 5 at the end)\n" \
            "Example: 12.345.678-5")
            print("-" * 40) 
            def get_acci_id():
                acci_id = input("Type in your ACCI-ID: ")

                #Chequear formato correcto
                if len(acci_id) == 12 and acci_id[2] == "." and acci_id[6] == "." and acci_id[10] == "-":
                    numbers_only = acci_id.replace(".", "").replace("-", "")

                    if numbers_only.isdigit() and len(numbers_only) == 9:
                        print(f"Valid ID: {acci_id}")
                        print("Great! Let us check your recent exams\n")
                        print("-" * 40) 
                        print("Your exam score is 100!!!\nWe are absolutely proud of you, you did really good!!\nNow go celebrate :)!")
                        return acci_id
                        
                    else:
                        print("Invalid format! Please use only numbers.")
                        return get_acci_id
                    
                else:
                    print("Invalid format! Please follow the pattern: 11.111.111-5")
                    return get_acci_id()   
            acci_id = get_acci_id()

        elif inp_1 == "inscription":
            print("On what level do you want to enroll in?\n")
            try:
                level = input("First Certificate or another level? (if another, specify)\n").strip().title()
                if level == "First Certificate" or level == "First":
                    print("-" * 40)
                    print("Great! You are in the final steps to have your degree!!\n")
                    print("We need you to follow the next steps in order to finish the incription\n")
                    print("-" * 40)
                    input("1st step: again, enter your full name bellow;\n")
                    
                    def get_user_id():
                        user_id = input("2nd step: enter your ID in format 11.111.111; ")

                        if len(user_id) == 10 and user_id[2] == "." and user_id[6] == ".":
                            numbers_only = user_id.replace(".", "")

                            if numbers_only.isdigit() and len(numbers_only) == 8:
                                print(f"Valid ID: {user_id}")
                                print(f"Here is your AACI-ID {user_id}-5. You can use it in the future to log in faster or check exam scores")
                                print("Congratulations!!! Now you are taking part in the First Certificate")
                                return user_id
                                
                            else:
                                print("Invalid format! Please use only numbers.")
                                return get_user_id
                    
                        else:
                            print("Invalid format! Please follow the pattern: 11.111.111")
                            return get_acci_id()
                        
                    user_id = get_user_id()
                elif level == "another level" or level == "another":
                    level = input("What level do you want to sign up for?")
                    print("We need you to follow the next steps in order to finish the incription\n")
                    print("-" * 40)
                    input("1st step: again, enter your full name bellow;\n")
                    
                    def get_user_id():
                        user_id = input("2nd step: enter your ID in format 11.111.111; ")

                        if len(user_id) == 10 and user_id[2] == "." and user_id[6] == ".":
                            numbers_only = user_id.replace(".", "")

                            if numbers_only.isdigit() and len(numbers_only) == 8:
                                print(f"Valid ID: {user_id}")
                                print(f"Congratulations!!! Now you are taking part in {level}")
                                return user_id
                                
                            else:
                                print("Invalid format! Please use only numbers.")
                                return get_user_id
                            
                    user_id = get_user_id()

                else:
                    print("Erro!! Must select one of the given options!")
                             
            except Exception as e:
                print(f"Error ocurred {e}")
    elif inp == "continue":
        print("Search around the page!\nIf you need help go back and select -help")
        exit ()

except Exception as e:
                print(f"Error ocurred {e}")

        






