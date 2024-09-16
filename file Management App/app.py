import os
def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename}: created successflly!")
    except FileExistsError:
        print(F'File name{filename}: alreaady exists!')

    except Exception as E:
        print('An error ocurred!')

def view_all_files():
    files=os.listdir()
    if not files:
        print('File in directory!')
        for file in files:
            print(file)

def delect_file(filename):
    try:
        os.remove(filename)
        print(f'{filename}: has been deleted successfully!')
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print('An erroe occurred')

def read_file(filename):
    try:
        with open('file.txt' , 'r') as f:
            content=f.read() 
            print(f"content of '{filename}' :\n{content}")                                 
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print('An error ocurred!')

def edit_file(filename):
    try:
        with open('file.txt' , 'a') as f:
            content= input("Enter data to add= ") 
            f.write(content+"\n")                                 
            print('content added to{filename} successfully!')
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print('An error ocurred!')

def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1:create file')       
        print('2:view all files')     
        print('3:Delete fille')       
        print('4:Read file')        
        print('5:Edit fille')
        print('6:Exit')       
        
        choice=input('Enter your choice(1-6)= ')
        if choice=='1':
            filename=input("Enter the filename to creat=  ")
            create_file(filename)
        elif choice=='2':
            view_all_files()
        elif choice=='3':
            filename=input('Enter the name of file your')
            delect_file(filename) 
        elif choice=='4':
            filename=input('Enter the name to read = ')
            read_file(filename)
        elif choice=='5':
            filename=input('Enter the name to edit = ')
            edit_file(filename)
        elif choice=='6':
            print('closing the app......') 
            break
        else:
            print('in-valid syntex') 

if __name__=="__main__":
   main()            


     
     


            


