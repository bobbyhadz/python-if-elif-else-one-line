# If-Elif-Else statement on one line in Python

my_str = 'bobby hadz'


result = ("Anonymous" if not my_str else my_str.upper()
          if len(my_str) > 2 else my_str.capitalize())

print(result)  # 👉️ 'BOBBY HADZ'