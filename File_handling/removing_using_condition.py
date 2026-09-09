import os
if os.path.exists("demo.py"):
    os.remove("demo.py")
    print("The file has been removed")
else:
    print("It does not exist")