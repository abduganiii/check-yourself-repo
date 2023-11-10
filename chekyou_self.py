class Auto:
    def ride(self):
        print('Riding on a ground')

class Boat:
    def swim(self):
        print('Floating on water')

class Amphibian(Auto, Boat):
    pass

obj = Amphibian()
obj.ride()
obj.swim()




class ContactList(list):
    def search_by_name(self, name):
        return [contact for contact in self if name.lower() in contact.lower()]

all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan'])

results = all_contacts.search_by_name('Olya')
print(results)