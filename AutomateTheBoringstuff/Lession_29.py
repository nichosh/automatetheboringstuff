import pyperclip, re  

#phone number examples: 415-555-0000, (415) 555-0000, 555-0000, ext. 12345, x12345 

#creating a regex for phone numbers

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                       #area code (optional)
(\s|-|\.)?                               #first separator (might be dash or space)
(\d{3})                                  #first digits of core number
(\s|-|\.)?                               #2nd separator
(\d{4})                                  #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?           #extension (word-part)
)''' , re.VERBOSE)

#creating a regex for e-mails
emailRegex = re.compile(r''' 
[a-zA-Z0-9_.+]+  #name part
@                #@ symbol
[a-zA-Z0-9_.+]+  #domain part
''', re.VERBOSE)

text =  pyperclip.paste()

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail) 