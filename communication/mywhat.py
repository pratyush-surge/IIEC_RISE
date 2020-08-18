import os
from twilio.rest import Client

client = Client()
from_whatsapp-number ='whatsapp:+14155238886'
to_whatsapp_number ='whatsapp:+918174899193'
client.messages.create(body='Hello Word!',
			from_=from_whatsapp_number,
			to=to_whatsapp_number)