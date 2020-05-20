import getpass

user = getpass.getuser()
print()
print('''   __  _  _                       __   __             
  / _|(_)| |  ___     ___  ___   / _| / _|  ___   ___ 
 | |_ | || | / _ \   / __|/ _ \ | |_ | |_  / _ \ / _ \\
 |  _|| || ||  __/ _| (__| (_) ||  _||  _||  __/|  __/
 |_|  |_||_| \___|(_)\___|\___/ |_|  |_|   \___| \___|
         
 ''')
print('You are currently on user [ ' + user + ' ]')
print('If that isn\'t the correct user, cancel the script right now.')
print()

# More later