import imaplib

"""
import base64
email_user = input('Email:sreerajms4you@gmail.com')
email_pass = input('Password:Sree@9001')

M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    rv, data = M.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
except imaplib.IMAP4.error:
    print("Login failed.")

M.login(email_user, email_pass)
M.select()

typ, data = M.search(None, 'ALL')

for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')   # data is being redefined here, that's probably not right
    num1 = base64.b64decode(num1)          # should this be (num) rather than (num1) ?
    data1 = base64.b64decode(data)
    print('Message %s\n%s\n' % (num, data[0][1]))  # don't you want to print num1 and data1 here?

M.close()
M.logout()
"""

EMAIL_ACCOUNT = input('Email:sreerajms4you@gmail.com')
EMAIL_PASSWORD = input('Password:Sree@9001')

M = imaplib.IMAP4_SSL('imap.gmail.com')
M.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
M.select('inbox')

result, data = M.uid('search', None)
print(data)
