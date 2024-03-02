import time
import random

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
    response = random.choice(
        [
            "hello sally why are you stinky?",
            "sally is so stinky",
            "sally is a poo",
            "jiguneun pyeongpyeonghada"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.1)
        