import boto3

access_key = "AKIAI6H6YNVHOFYTEL6Q"
access_secret = "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"
region ="us-east-1"
queue_url = "https://sqs.us-east-1.amazonaws.com/291631277305/IAN"

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': 'Simple',
                'title': "SessionSpeechlet - " + title,
                'content': "SessionSpeechlet - " + output
            },
            'repromt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': reprompt_text
                 }
            },
            'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
            'version': '1.0',
            'sessionAttributes': session_attributes,
            'response': speechlet_response
    }

def post_message(client, message_body, url):
    response = client.send_message(QueueUrl = url, MessageBody = message_body)

def lambda_handler(event, context):
    client = boto3.client('sqs',aws_access_key_id = access_key, aws_secret_key = access_secret, region_name = region)
    intent_name = event['request']['intent']['name']
    slots = event['request']['intent']['slots']
    if intent_name == "NavigateTo":
        destination = str(slots['Destination']['value'])
        post_message(client, 'navigate to ' + destination, queue_url)
        message = "Navigating to " + destination
    elif intent_name == "DisplayInformation":
        object = str(slots['Object']['value'])
        post_message(client, 'display info of ' + object, queue_url)
        message = "Displaying " + object + " information"
    else:
        message = "Unknown"

    speechlet = build_speechlet_response("ISAAC Status", message, "", "true")
    return build_response({}, speechlet)

