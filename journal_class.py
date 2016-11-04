import datetime



class Journal(object):

    def __init__(self, name="AlexJournal"):

        self.date_posted = str(datetime.datetime.now().date())

        self.journal_dict = {}

        self.name =name



    def create_journal_entry(self):

        author = str(raw_input('Enter your Name: '))

        title = str(raw_input('Enter the title: '))

        post = str(raw_input('Enter Entries/Thoughts:\n'))

        time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M %S"))

        self.journal_dict.update({time: {

            "author": author.upper(),

            "time": time,

            "title":title.upper(),

            "entry": post}})

        return self.journal_dict

        '''display all'''

    def list_of_entries(self):

        entries = self.journal_dict.keys()

        print "JOURNAL" + self.name

        print "TITLE \t TIME"

        for item in entries:

            print  self.journal_dict[item]["title"]+"\t"+self.journal_dict[item]["time"]

            

    def view_last(self):

        ourkeys=self.journal_dict.keys()

        ourkeys.sort()

        latest =ourkeys[len(ourkeys)-1]

        print "TITLE: " + str(self.journal_dict[latest]["title"])+ " TIME: " + str(self.journal_dict[latest]["time"])

        print "ENTRY \n" + str(self.journal_dict[latest]["entry"])









while True: 

    print("Choose an option:\n\t1:Create a new journal\n\t2:Make a new journal Entries\n\t3:Display Made Journal Entries\n\t4:View my last journal Entry\n\t Enter 0 to quit")

    try:

        choice = int(raw_input("Choice:"))

    except(ValueError):

        print("Invalid choice!!! Choose from available options")

        continue

    
    try:
        if choice ==1:

            name =str(raw_input("Enter Journal Name: "))

            journal=Journal(name)

        elif choice==2:

            journal.create_journal_entry()

        elif choice == 3:

            journal.list_of_entries()

        elif choice ==4:

            journal.view_last()

        elif choice ==0:

            break

        else:

            print("Invalid choice!!! Choose from available options")

            continue
    except(NameError):
        print "You have to create a journal first"
        continue
