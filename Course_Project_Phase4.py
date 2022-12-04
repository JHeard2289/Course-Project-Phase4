#Jerome Heard
#CIS261
#Phase 4 Project
def read_entries():
    user_id = []
    with open('users_data.txt','r') as f:
        for data in f.readlines():
            user_id.append(data.split('|')[0])
      
    # print(user_data)
    return user_id

def display_entries():
    with open('users_data.txt','r') as f:
        for data in f.readlines():
            for i in data.split('|'):
              print(i,end = " ")      

def add_entry(user_ids):
    while True:
        print('Enter user id:',end = " ")
        user_id = input()
        
        if user_id.lower() == 'end':
            break
        elif user_id in user_ids:
            print("User Id already exists")
        else:
            print('Enter password:',end = " ")
            password = input()
            print('Enter authorization code:',end = " ")
            code = input()
            
            if code != 'Admin' and code != 'User':
                print('Wrong authorization code')
            else:
                with open('users_data.txt','a') as f:
                    f.write(f'{user_id}|{password}|{code}\n')
                user_ids.append(user_id)

                print("Data Inserted.")
    display_entries()
            
    

            
      
    
         
with open('users_data.txt','a') as f:  #to create file if not exists
  pass    
user_ids = read_entries()
add_entry(user_ids)


def add_entry(user_ids):
    while True:
        print('Enter user id:',end = " ")
        user_id = input()
        
        if user_id.lower() == 'end':
            break
        elif user_id in user_ids:
            print("User Id already exists")
        else:
            print('Enter password:',end = " ")
            password = input()
            print('Enter authorisation code:',end = " ")
            code = input()
            
            if code != 'Admin' and code != 'User':
                print('Wrong authorization code')
            else:
                with open('users_data.txt','a') as f:
                    f.write(f'{user_id}|{password}|{code}\n')
                user_ids.append(user_id)
                print("Data Inserted.")


def display_entries():
    with open('users_data.txt','r') as f:
        for data in f.readlines():
            print(data.split('|')[0],end = " ")
            print(data.split('|')[2],end = " ")
            print()
                    

def read_entries():
    user_ids = []
    passwords = []
    auth_codes = []
    with open('users_data.txt','r') as f:
        for data in f.readlines():
            user_ids.append(data.split('|')[0])
            passwords.append(data.split('|')[1])
            auth_codes.append(data.split('|')[2].strip())


    print("Enter user Id:",end = " ")
    id = input()
    if id in user_ids:  
      index = user_ids.index(id)

      code = auth_codes[index]

      if code == 'Admin':
        print('Enter Opertation:\n1.Enter data\n2.Display data')
        option = int(input())
        if option == 1 :
          add_entry(user_ids)
        elif option == 2:
          display_entries()
        else:
          print("Ending the program")
      else:
        print('Enter Opertation:\n1.Display data')
        option = int(input())
        if option == 1 :
          display_entries()
        else:
          print("Ending the program")
          
    else:
      print('User Id does not exists')
    # print(user_data)
    return user_ids,passwords,auth_codes




            
    
with open('users_data.txt','a') as f:  #to create file if not exists
  pass    

read_entries()

