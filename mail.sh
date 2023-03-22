#!/bin/bash

# Set the email subject and recipient
subject="Test email"
recipient="user@example.com"

# Set the email message
message="This is a test email sent from a shell script."

# Send the email
echo "$message" | mail -s "$subject" "$recipient" 

# Set the email subject, sender, recipient, and body
subject="Test email with sender and recipient"
sender="sender@example.com"
recipient="recipient@example.com"
body="This is a test email with a specified sender and recipient."

# Send the email
echo "$body" | mail -s "$subject" -a "From: $sender" "$recipient"




# Email details
FROM="sender@example.com"
TO="recipient@example.com"
SUBJECT="Test email"
MESSAGE="This is a test email sent from a shell script."

# Send the email
echo "$MESSAGE" | mail -s "$SUBJECT" -r "$FROM" "$TO"

