# TODO Найдите количество книг, которое можно разместить на дискете
V_disk = 1.44  # Мб
pages = 100
lines_for_pages = 50
symbol_for_lines = 25
bytes_for_symbol = 4

disk_bytes = V_disk * 1024 * 1024  # объем дискеты в байтах
book_bytes = pages * lines_for_pages * symbol_for_lines * bytes_for_symbol

books_on_disk = int(disk_bytes // book_bytes)  # целое число книг

print("Количество книг, помещающихся на дискету:", books_on_disk)
