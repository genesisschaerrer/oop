class CompanyInvoice:
    def __init__ (self, company, total)
        self.company = company
        self.total = total

    def formatter(self):
        retrun f'{company} you owe ${total}'

google = CompanyInvoice("google", 100)

print(google.formatter())

#get and set
print(google.total)

#set 
#you are calling on google because in the instance
#the google object
google.client = "Yahoo"