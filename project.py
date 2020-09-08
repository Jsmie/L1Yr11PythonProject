#variables

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
 while repeat == True:
   shopping_list = input("Please start your list here and type 'done' when finished").strip().lower()
if shopping_list == 'done':
         repeat= False
else:
    count = list_exe.count(shopping_list)


else:
    print("incorrect command")



