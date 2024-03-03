import time
import random
import boto3

def getPosts(topic):
    # TODO: get the post numbers that match topic
    # Dummy function to get breeds based on the selected animal
    if topic == "Natural Recursion":
        return ["Labrador Retriever", "German Shepherd", "Golden Retriever"]
    elif topic == "template":
        return ["Persian", "Siamese", "Maine Coon"]
    elif topic == "office hours":
        return ["Parrot", "Canary", "Finch"]
    elif topic == "midterm":
        return ["Goldfish", "Betta", "Guppy"]
    else:
        return []


#-----------------------------------------------------------------------------
# Send question from front-end to llama2, retrieving the response and returning it
#-----------------------------------------------------------------------------
def getResponseFromModel(question):
    client = boto3.client('bedrock-agent-runtime')

    # modelArn = client.get_foundation_model(
    #     modelIdentifier = 'anthropic.claude-v2:1'
    # )

    # print(modelArn)
    print("The question is: " + question)

    response = client.retrieve_and_generate(
    input={
        'text': question
    },
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': 'MFOWUQRVFC',
            'modelArn': 'arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-v2:1',
        }
    },
    sessionConfiguration={
        'kmsKeyArn': 'arn:aws:kms:us-west-2:852069794117:key/8c816af9-92bc-4084-8db2-a27a83bb3d87'
    }
    )
    
    text = response["output"]["text"]
    print(text)

    return text

    # for word in response.split():
    #     yield word + " "
    #     time.sleep(0.1)
        