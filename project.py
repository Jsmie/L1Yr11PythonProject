#variables
list_exe = []
#introduction
print("Welcome to your digital clock simulator")

answer = input("""Commands you may use are !time, !temperature, !day, !date, and
!start_shopping_list
""")

#commands
if ("!time") == answer :
#Time function
    from datetime import datetime
    now = datetime.now()
    print("%s:%s:%s" % (now.hour,now.minute,now.second))

#date function
elif ("!date") == answer :
    from datetime import datetime
    now = datetime.now()
    print("%s/%s/%s" % (now.day,now.month,now.year))

#List function
elif ("!start_shopping_list") == answer :
 repeat=True


 #repeating function of list
repeat = True
while repeat == True:
  shopping_list = input("Please enter a item for the list or 'done' to end input: ").strip().lower()

  #Check if user has entered done so that loop can be stopped if so
  if shopping_list == 'done':
    repeat = False
  else:
    #Check if item is already in list
    count = list_exe.count(shopping_list)

    #If so, give user error message, otherwise add the item and give success message
    if count > 0:
      print("Sorry {} is already on the list!".format(shopping_list))
    else:
      list_exe.append(shopping_list)
      print("{} has been added!".format(shopping_list))

#Once user is done, print out their list for them
print("Your list contains : ")

for shopping_list in list_exe:
  print(shopping_list.title())





