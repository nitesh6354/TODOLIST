tasks=[]

def addtask():
    task=input("\n Enter you task !")
    tasks.append(task)
    print(f"\n {task} is added to list !")

def listoftask():
    print("----------------------------------------------------------------------------------------------------------")
    print(" Current tasks !")

    for index,i in enumerate(tasks):
        print(f"\n #{index + 1}.{i}")
    
    print("===================================================================================================")

def deletetask():
    listoftask()

    try:
        tasktodelete=int(input('\n Enter task to delete !'))
        if tasktodelete>=0 and tasktodelete<len(tasks):
            tasks.pop(tasktodelete)
            print(f"\n {tasktodelete} task delete from the tasks !")
    except:
        print(f"\n {tasktodelete} was not found !")

    else:
        print("\n invalide input !")

if __name__=='__main__':

    while True:
        print("\n Enter first to add task !")
        print("\n Enter secound to delete task !")
        print('\n Enter third to watch list of task !')
        print("\n quite ")

        choice=int(input("\n Enter your choice "))

        if choice==1:
            addtask()
        elif choice==2:
            listoftask()
        elif choice==3:
            deletetask()
        elif choice==4:
            break
        else:
            print("\n invalide input please reenter the input !")
    
    print('\n good bye !')