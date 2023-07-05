import pathlib
import json

class ManageDb:
    __address_file = "{0}/Src/db/dbContacts.json".format(pathlib.Path().absolute())

    def read_contacts(self):
        with open(self.__address_file, "r") as data:
            print(data.read())
        
md = ManageDb()
md.read_contacts()

