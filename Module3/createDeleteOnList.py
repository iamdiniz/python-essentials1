systems = ['debian', 'ubuntu', 'windows']

print("Diniz \n List: ", systems)
wannaStop = str(input("You wanna insert orr delete system? (yes/no): "))

if wannaStop == 'yes':
    for i in systems:
         wannaInsert = str(input("Do you wanna insert a new system ? (yes/no): "))
         if wannaInsert == 'yes':
             newSystem = str(input("Insert new system: "))
             systems.append(newSystem)
             print(systems)

         stop = str(input("stop? (yes/no): "))
         if stop == 'yes':
            break

         wannaDelete = str(input("Do wanna delete a system ? (yes/no): "))
         if wannaDelete == 'yes':
             positionToDelete = int(input("Type indice of system do you wanna delete: "))
             del systems[positionToDelete]
             print(systems)

         stop = str(input("stop? (yes/no): "))
         if stop == 'yes':
             break

print("Thanks, see you later! \n List of systems: ", systems)
