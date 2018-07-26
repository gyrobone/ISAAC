# ISAAC
InterStellar Astro-nAvigation Control

The main purpose of ISAAC is to provide a voice interface for a Digistar6 planetarium system. Using an Amazon Echo and a custom Alexa Skill, you can ask Alexa (on which I have changed the wake word to Computer since Alexa is a little weird and breaks the immersion aspect) any compatible command for ISAAC Control to perform, and it will then use some Python Magic(TM) to send that request to the Digistar6 system.

ISAAC is a Python script with two main parts.

The first part is the lambda_function.py which is hosted as a LambdaFunction on the AWS Developers Page. This function receives commands and input parameters (called slots in the Alexa Skill Kit) and it then takes the command and parameters and sends it as a message to an AWS SQS (SimpleQueueService). 

Next, while the function isaac.py is running on the Digistar6 system, it continuously checks for messages in the SQS, when one is detected, it retrieves the message and deletes it from the queue. Then, ISAAC will take the information in the message and will determine what command is being requested, running the appropriate script.

As of right now, ISAAC can only handle NavigateTo commands and DisplayInformation commands, but implementing new commands and command structures is incredibly simply and I will continue to add them as time goes on.
