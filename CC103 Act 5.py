
file_path = r"C:\Users\luzon\Documents\2ND SEM\CODES\Abs.txt"
#write
with open(file_path, "w") as file:
    file.write("202410021, Lance Dominic Luzong, BSIT 1-A\n")
    file.write("202410022, Kyle Arrold L.Nano, BSIT 1-A\n")
  
print("Initial student written successfully")

#append
with open(file_path, "a") as file:
    file.write("202410047, Jemark Tubat, BSIT 1-A\n")
    file.write("202410137, Kimrey Cunanan  , BSIT 1-A\n")
    
print("New student reocrds appended successfully")

    
    
#read
with open(file_path, "r") as file:
    file = file.read()
    print("--" * 20)
    print("\nStudent records:\n")
    print(file)
    print("--" * 20)
     