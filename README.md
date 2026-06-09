## Phisherman: AI Phishing Analysis & Generation 


### What is it?

Phisherman is a fully offline AI tool that comes with two independent modules grouped together in a single webapp: 

- A Red Team generator that takes a given input and outputs convincing phishing text. 

- A Blue Team analyzer that takes a given input and outputs an analysis determining whether the text is a phishing attempt or not. Its report includes threat classifications and a justification score that indicates how confident the model is in its answer.

### How does it work?

Phisherman combines two separate Ollama LLMs through a single, simple-to-use UI powered by Python's Streamlit library. Each Ollama LLM has its own modelfile and can function completely independently of each other.

### Prerequisites:

In order to run Phisherman, you need to have Ollama set up on your machine. You also need to pull the `qwen2.5-coder:7b` model with this command:

```ollama pull qwen2.5-coder:7b```

Once you have done this, proceed to the setup guide.

### Setup Guide:

Clone the repository.
```cd``` into the repository.
Download all the Python libraries from the requirements.txt:

```pip install -r requirements.txt```

You may have noticed that the project folder has two modelfiles: one without an extension and one with .red extension. These are important to keep separate because they contain the system prompt that dictates the LLMs' behavior.

Open a terminal and run:

```ollama create phisherman -f Modelfile```

Then run:

```ollama create phisherman-red -f Modelfile.red```

Once this is complete, run:

```streamlit run phisherman.py```

And observe the results. 


If, after initial testing, you are unsatisfied with the LLM's behavior, you may choose to modify the modelfiles. In order to update the LLMs, you will need to remove the custom LLMs made previously, using this command:

```ollama rm [LLM-name]```

And then make a new one:

```ollama create [LLM-name] -f [Modelfile-Name]```

Repeat as many times as necessary. 


### Disclaimer:

All content in this project exists for educational purposes and is to be used solely for that purpose. The developer does not condone any form of illegal black hat hacking, and does not authorize or take responsibility for any such activities performed with this project.

