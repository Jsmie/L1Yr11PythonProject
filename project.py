#variables
#introduction
print("Welcome to your digital clock simulator")

time = input("""Commands you may use are !time, !temperature, !day, !date, and
!start_shopping_list
""")

#commands
if ("!time"):
#Time function
    from datetime import datetime
    now = datetime.now()
    print ("%s:%s:%s" % (now.hour,now.minute,now.second))
#date function
elif  "!date":

    from datetime import datetime
    now = datetime.now()
    print ("%s/%s/%s" % (now.day,now.month,now.year))
elif t =="start_shopping_list":
    print("yes")


else:
    print("incorrect command")



