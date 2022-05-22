import smtplib


# sending email function
def sending_email(type_trash):
    # email and password of eco friend
    garbage_sorter_email = "garbagesorter2022@gmail.com"
    password = "ISortGarbage123"
    # owner's email
    user_email = "harshnp2@gmail.com"

    # what the email will include in terms of text
    TEXT = f'The {type_trash} bin is full, please take it out!!!'
    SUBJECT = "Trash State"
    email_message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    # logins into eco friend account
    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(garbage_sorter_email, password)
    print("success")

    # sends email
    server.sendmail(garbage_sorter_email, user_email, email_message)
    print("Email has been sent")

    server.quit()
