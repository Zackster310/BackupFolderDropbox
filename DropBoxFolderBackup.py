import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def uploadFolder(self, origin, destination):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(origin):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relativePath = os.path.relpath(localPath, origin)
                dropboxPath = os.path.join(destination, relativePath).replace('\\', '/')

                print(relativePath)
                print(dropboxPath)

                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode = WriteMode('overwrite'))

def main():
    accessToken = 'JoFLlxHih0sAAAAAAAAAAWeqM1lQOXjDkjSWHeoOjH8t9Sq7L2qRbBvxOA51L3GL'
    transferData = TransferData(accessToken)

    origin = input("enter origin folder: ")
    destination = input("enter folder destination location: ")

    transferData.uploadFolder(origin, destination)

    print("Files have been moved")

main()