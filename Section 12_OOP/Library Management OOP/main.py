from book_management import *

admin1 = Admin("Zannatul")
admin1.add_book("DS1", "Zane1", "SciFi1", 1, 20)
admin1.add_book("DS2", "Zane2", "SciFi2", 2, 20)
admin1.add_book("DS3", "Zane3", "SciFi3", 3, 20)

update_list = {"title": "DS100", "author": "Zane1", "genre": "SciFi1", "copies": 20}
admin1.update_book(update_list, 1)
# admin1.book_storage()
admin1.delete_book(1)
admin1.book_storage()
admin1.search_book("2")
