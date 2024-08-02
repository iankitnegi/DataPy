# Program to split the str/email address into username & company name
# Example-> john@google.com -> john , google

def spliter(email):
    l=len(email)
    pos=0
    for i in range(l):
        if email[i]=='@':
            pos=i
    return email[:pos] , email[pos+1:]

u_name, company = spliter("john@google.com")
print("user_name\t company")
print(f"{u_name}\t {company}")
