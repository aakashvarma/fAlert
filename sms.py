import nexmo
import smtplib 

api_key = '38094c1f'
api_secret = '?? API KEY HERE ??'

client = nexmo.Client(key=api_key, secret=api_secret)

# client = nexmo.Client(application_id=application_id, private_key=private_key)

response = client.send_message({'from': 'Python', 'to': '918309594362', 'text': 'Fall has occurred at: https://www.google.com/maps/search/?api=1&query=12.9739537,79.1581631'})
# https://www.google.com/maps/search/?api=1&query=12.9739537,79.1581631


response = response['messages'][0]

if response['status'] == '0':
  print ('Sent message', response['message-id'])

  print ('Remaining balance is', response['remaining-balance'])
else:
  print ('Error:', response['error-text'])


s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
  
# Authentication 
s.login("aakashvarma18@gmail.com", "  ??Password here??  ") 
  
message = "\n Fall has occurred at https://www.google.com/maps/search/?api=1&query=12.9739537,79.1581631 "
s.sendmail("aakashvarma18@gmail.com", "aakashvarma18@gmail.com", message) 
  
# terminating the session 
s.quit()




















