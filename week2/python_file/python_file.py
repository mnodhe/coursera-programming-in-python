try:
    with open('newfile.txt',mode='w') as file:
        file.writelines(["this is a new file created!","\nthis is another line added."])
except FileNotFoundError  as e:
  print('File not found')