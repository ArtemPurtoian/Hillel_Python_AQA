notes = []
actions = "Action options:\n" \
          "'add' to add a note\n" \
          "'earliest' to see from earliest to latest\n" \
          "'latest' to see from latest to earliest\n" \
          "'longest' to see from longest to shortest\n" \
          "'shortest' to see from shortest to longest\n" \
          "'exit' to exit the program"
print(actions)
user_question = "\nEnter an option to proceed: "
user_key = input(user_question)
no_notes = "There are no notes yet."

while True:
    if user_key == 'add':
        user_note = input("Enter your note: ")
        notes.append(user_note)
        # Using append to add each new note to the list.
        user_key = input(user_question)
    elif user_key == 'earliest':
        if len(notes) > 0:
            earliest_note = notes[:]
            print('; '.join(earliest_note))
            user_key = input(user_question)
            """ 
            Making a copy of the original list to operate with
            if there is at least 1 element in the list.
            Since each new note is added at the end of the list,
            a copy of the list is enough to display from earliest to latest.   
            """
        else:
            print(no_notes)
            """     
            Show an alert "no notes" if the list is empty yet.   
            """
            user_key = input(user_question)
    elif user_key == 'latest':
        if len(notes) > 0:
            latest_note = notes[:]
            latest_note.reverse()
            print('; '.join(latest_note))
            user_key = input(user_question)
            """ 
            Making a copy of the original list to operate with
            if there is at least 1 element in the list.
            Using reverse() to show reversed order of the copied list.   
            """
        else:
            print(no_notes)
            user_key = input(user_question)
    elif user_key == 'shortest':
        if len(notes) > 0:
            shortest_note = sorted(notes, key=len)
            print('; '.join(shortest_note))
            user_key = input(user_question)
            """        
            Sorting the list by length of the elements from shortest to
            longest if there is at least 1 element in the list.   
            """
        else:
            print(no_notes)
            user_key = input(user_question)
    elif user_key == 'longest':
        if len(notes) > 0:
            longest_note = sorted(notes, key=len, reverse=True)
            print('; '.join(longest_note))
            user_key = input(user_question)
            """        
            Sorting the list by length of the elements in reversed order
            from longest to shortest if there is at least 1 el-t in the list.   
            """
        else:
            print(no_notes)
            user_key = input(user_question)
    elif user_key == 'exit':
        """ If user enters 'exit' the program will stop. """
        break
    else:
        print("\n--- You can enter only a default option.\n")
        print(actions)
        user_key = input(user_question)
        """
        Displaying an alert if entered keyword is not default
        and reminding which the default options are.
        """
