import pathlib
import json


class ManageDb:
    __address_file = "{0}/src/db/db.json".format(pathlib.Path().absolute())

    def read_contacts(self):
        with open(self.__address_file, "r") as data:
            return json.loads(data.read())


    def write_contacts(self, new_data):
        with open(self.__address_file, "w") as data:
            data.write(json.dumps(new_data))

# @app.get("/api/contacts")
# def get_all_contacts():
#     return md.read_contacts()

# @app.get("/api/contacts/{id_contact}")
# def get_single_contact(id_contact: int):
#     contacts = md.read_contacts()

#     for contact in contacts:
#         if contact["id"] == id_contact:
#             return contact
#         raise HTTPException(status_code=404, detail="Este man no existe")

# @app.post("/api/contacts")
# def add_contacts(new_contact: ContactModel):
#     contacts = md.read_contacts()
#     new_contact = new_contact.dict()

#     contacts.append(new_contact)

#     md.write_contacts(contacts)

#     return {
#         "Todo salio bien my friend"
#     }

# @app.put("/api/contacts{id_contact}")
# def update_contacts(id_contact: int, new_contact: ContactModel):
#     contacts = md.read_contacts()

#     for index, contact in enumerate (contacts):
#         if contact["id"] == id_contact:
#             contacts[index] = new_contact.dict()

#             if new_contact.name == "":
#                 return {
#                 "Campo name no debe estar vació"
#                 }
#             if new_contact.phone == "":
#                 return {
#                 "Campo phone no debe estar vació"
#                 }

#             md.write_contacts(contacts)

#             return {
#                 "Se ha editado correctamente"
#             }
#     raise HTTPException(status_code=404, detail="Este man no existe")

# @app.delete("/api/contacts/{id_contact}")
# def delete_contact(id_contact: int):
#     contacts = md.read_contacts()

#     for index, contact in enumerate (contacts):
#         if contact["id"] == id_contact:

#             contacts.pop(index)

#             md.write_contacts(contacts)

#             return {
#                 "Se ha eliminado correctamente"
#             }
#     raise HTTPException(status_code=404, detail="Este man no existe")
