# BigBlueButton Participant Bot
This is a simple Python 3 program that allows you to test your BigBlueButton server/servers functionality and most importantly find out if your current server configuration is capable of handling a certain amount of participants.

## Requirements
- pip
- selenium
- chromedriver

## How to use
Simply adjust the *apiEndpoint*, *secuirtySalt* according to your own server's information and you're good to go.

## Further configuration
- Normally, there is no need to change the value of *meetingID*. But if you want to test multiple sessions on a server be sure to assign a unique meetingID to each instance of the program running.
- *botName* does not affect the functionality of the program and only defines the participants' names that join the session. Although you can change it to your desired value.
- *participantCount* is the number of participants that join the session. Note that there will be a chrome tab opened for each participant so adjust it carefully due to chrome's RAM usage and with your system resources in mind.
