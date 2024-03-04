

# Email Format   ---> a@gmail.com  or a@gmail.in

special_characters = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'
]

email = input("Enter Email Address to check validation...")

if len(email) >= 10:
    if email.lower():
        if email.count("@") == 1:
            if email[-3] == "." or email[-4] == ".":
                if email[0].isalpha():
                    if email.count(".") == 1:
                        valid = True
                        for cha in special_characters:
                            if cha in email:
                                valid = False
                                break
                        if valid:
                            print("Congratulations! Your Email is Verified.")
                        else:
                            print("Wrong Pattern.. Hint- You cannot use special characters in the email.")
                    else:
                        print("Wrong Pattern.. Hint- You cannot use (.) more than one time")
                else:
                    print("Wrong Pattern.. Hint - You cannot use first letter as numeric or other character.")
            else:
                print("Wrong Pattern.. Hint- (.) should be used in the last two or three characters before.")
        else:
            print("Wrong Pattern.. Hint- @ more than 1 times.")
    else:
        print("Wrong Pattern.. Hint- Use lowercase letters.")
else:
    print("Wrong Pattern.. Hint- Low Characters in the Mail.")
