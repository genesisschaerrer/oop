# class Invoice: 
#     def greeting(self):
#         return 'Hi there'

# inv_one = Invoice()
# print(inv_one.greeting())

# class AnotherInvoice:
#     def __init__(self, client, total):
#         self.client = client
#         self.total = total

class CompanyInvoice:
    def __init__ (self, company, total)
        self.company = company
        self.total = total

    def formatter(self):
        retrun f'{company} you owe ${total}'

google = CompanyInvoice("google", 100)

print(google.formatter())