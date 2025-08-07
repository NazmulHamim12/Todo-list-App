import firebase_admin
from firebase_admin import credentials, db

# Firebase Init (Make sure "new.json" is your service account key file)
cred = credentials.Certificate("new.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://api-project-84f93-default-rtdb.firebaseio.com/'
})



def sing_up():
    print("\n Please Sing up your id")
    name = input("Enter Your name:")
    password = input("Enter your password:")
    ref=db.reference(f'task-app/{name}')

    ref.set({
        'name':name,
        'pass':password,
        'count':0

    })
    print("Succesfully sing up")

def login():
    print("\n Login with your pass and name")
    name=input("Enter your name:")
    password=input("Enter your password:")

    ref=db.reference("task-app")
    name_data=ref.get()
    names=[]
    for x in name_data:
        names.append(x)

    if name in names:
        ref_2=db.reference(f'task-app/{name}')
        data=ref_2.get()

        if name==data['name'] and password==data['pass']:
            print("\n \n     You login successfully")

            ref=db.reference(f'task-app/{name}')
            data=ref.get()


            arr=[]
            for x in data:
                arr.append(x)

            if 'task' not in arr:
                print("No task available")
            else:
                print("\n Task----->>>")
                for x,y in data['task'].items():
                    print(f"{x}-->{y}")



            print("\n \n What your choice")
            print("1.Add task")
            print("2.Remove task")


            choice=input("Enter you choice:")

            if choice =='1':

                for_task = db.reference(f'task-app/{name}')
                data = for_task.get()
                count = data["count"]
                count += 1
                task_name = input("Enter your task name:")
                task_des = input("Enter your descrption:")

                task_ref = for_task.child("task")
                task_ref.update({
                    f'{task_name}': task_des
                })
            else:
                print("\n   For task removing enter detailes")
                key=input("Enter your task name:")
                name=input("Enter you id name:")

                dili=db.reference(f'task-app/{name}/task/{key}')
                dili.delete()






        else:
            print("You r name or pass  is incorrect")

    else:
        print("Your name or pass  is incorrect")





def start():
    print("\n       Welcome Your Todo-List")
    print("1.Sing up")
    print("2.Log in")
    chose=input("Choose one:")


    if chose == "1":
        sing_up()
    elif chose == "2":
        login()



start()
