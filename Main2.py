import os
import shutil
import dropbox
from dropbox.files import WriteMode

# Creating the Transfer Class


class Transfer_Data:

    # Constructor for Class....
    def __init__(self, Folder_Path, Access_Token, Destination):
        self.Folder_Path  = Folder_Path
        self.Access_Token = Access_Token
        self.Destination  = Destination
                                                                                                                                                                              
    # Function for uploading
    def UploadToDropBox(self):

        # Creating The DropBox and passing the Token Value
        dbx = dropbox.Dropbox(self.Access_Token)

        # All Values renamed
        FolderPath = self.Folder_Path
        Token = self.Access_Token
        Destination = self.Destination

        # Using for loops for files,name and path
        for root, dirs, files in os.walk(FolderPath):
            for file_Name in files:

                #Joining the root and file_Name to create a new path 

                Local_Path = os.path.join(root, file_Name)
                print(Local_Path)
                
                #Using the relpath method
                RelativePath = os.path.relpath(Local_Path, FolderPath)
                DropBox_Path = os.path.join(Destination, RelativePath)
       
                #Opening file in read mode 'rb'
                f = open(Local_Path, 'rb')
                
                #Uploading the file in dropbox using the dbx we created using the dbx variable 
                #which we created earlier
                print(DropBox_Path)
                dbx.files_upload(f.read(), DropBox_Path, mode=WriteMode('overwrite'))

def main():

    Folder_Input = input("Please Enter File Path")
    Destination_Input = input("Please enter destination")

    Access_Token = 'nUanAJzDg-8AAAAAAAAAAQwUKz6WtbU-8aQnxGJl91XcP48z6xglTwatyGU28IGR'

    TransferFiles = Transfer_Data(
        Folder_Input, Access_Token, Destination_Input)
    TransferFiles.UploadToDropBox()


main()
                   