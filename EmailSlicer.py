# take user email address

email =input("Email address, please?:").strip()

# slice out user name

user = email[:email.index("@")]

#slice domain name

domain = email[email.index("@")+1 :]

# format message

output = "Your username is {} and domain name is {}".format(user, domain)

#display output message

print(output)
