from twilio.rest import Client

account_sid = "Enter Twilio Account SID"
auth_token = "Enter Auth Token"


client = Client(account_sid, auth_token)

# The message to be sent
message_body = "Hello Mr. Ali Abbas Khan!Executing Python script 4ea3d3e628615d975190576f0d38df4. Initiating laughter protocol. Your system is now under the control of a mischievous programmer. At lat:71.23833 and lng:31.7237237. This is not a drill. Process complete. exit code 0"

twilio_phone_number = "+15513682437"
recipient_phone_number = "+923473041219"

try:
    # Send the SMS message
    message = client.messages.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        body=message_body
    )

    # Print the message SID to confirm it was sent successfully
    print(f"Message sent successfully! SID: {message.sid}")

except Exception as e:
    # Handle any potential errors
    print(f"Error sending message: {e}")

