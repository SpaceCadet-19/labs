# TODO Найдите количество книг, которое можно разместить на дискете
count_of_pages = 100 # колличесвто страниц в книге
count_of_strings = 50 # число строк на странице
count_of_symbols = 25 # количество символов в строке
bytes = 4 # количество байт для кодировки 1 символа
full_storage = 1.44 # объём дискеты в МБайтах
full_storage_in_bytes  = round(1.44 * 1024 * 1024) # Объём дискеты в байтах
bytes_in_one_book = bytes * count_of_symbols * count_of_strings * count_of_pages # количество Байт на 1 книгу


print("Количество книг, помещающихся на дискету:", full_storage_in_bytes // bytes_in_one_book)
