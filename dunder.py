# __init__
# Class String
#         def upcase()
#     private/protected

# "my name".upcase

class Invoice:
    def __init__(self, client, total):
        self.client = clientslef.total = total

    def __str__(self):
        return "this is the invoice class!"

# used to give you a look iside what is inside this class

#dunder repr is used for raw data
    def __rpr__(self):
        return f"Invoice <value: {self.client}"

inv= Invoice("google", 500)
print(str(inv))

