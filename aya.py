import cohere
import os

def Translate(prompt, language="Arabic"):
    try :
        co = cohere.Client(os.environ["API_KEY"]) # This is your trial API key
    except:
        return "Error API_KEY"
    
    prompt = "Translate to {language} : {prompt}"

    response = co.generate(
        model='c4ai-aya',
        prompt=prompt,
        max_tokens=300,
        temperature=0.5,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return response.generations[0].text