import streamlit as st
import ollama
 

#config 

OLLAMA_HOST = "http://localhost:11434"


#initialize the Ollama client 
client = ollama.Client(host=OLLAMA_HOST)

#UI

st.set_page_config(page_title="Phisherman", page_icon="🐟", layout="wide")
st.title("Phisherman")
st.subheader(f"Connected to: ({OLLAMA_HOST})")


#columns for UI division

red_col, blue_col = st.columns(2)


#for red team 
with red_col:
    st.header("🔴 Phishing Text Generator")

    #input for the generator
    scenario = st.text_input(
        "What scenario do you need text for?",
        placeholder="e.g., IT department multi-factor authentication reset"
    )

    if st.button("Generate Text"):
        if scenario:
                try:
                    response = client.generate(
                        model="phisherman-red",  #this is where we enter the name of the Ollama LLM
                        prompt=scenario
                    )
                    # Store in session state so it stays on screen
                    st.session_state.red_output = response['response']
                except Exception as e:
                    st.error(f"Error calling red model: {e}")
        else:
            st.warning("Please enter a scenario first.")

# Display the output in a text area so the user can easily copy it
    red_text = st.text_area(
        "Generated Simulation Output:",
        value=st.session_state.get("red_output", ""),
         height=350,
         help="Copy this text to test it in the Blue Team analyzer, or modify it yourself."
    )


#for blue team

with blue_col:
    st.header("🔵 Phishing Text Analyzer")

    # Input for the analyzer (User can paste anything here)
    text_to_analyze = st.text_area(
        "Paste text here to analyze:",
        placeholder="Paste an email, text message, or previously generated text here...",
        height=200
    )
    
    if st.button("Analyze Text"):
        if text_to_analyze:
            with st.spinner("Analyzing..."):
                try:
                    response = client.generate(
                        model="phisherman", #LLM goes here
                        prompt=text_to_analyze
                    )
                    st.session_state.blue_output = response['response']
                except Exception as e:
                    st.error(f"Error calling blue model: {e}")
        else:
            st.warning("Please paste some text to analyze.")

    # Display the analysis results
    st.markdown("### Analysis Results")
    if "blue_output" in st.session_state:
        st.info(st.session_state.blue_output)
    else:
        st.write("No analysis performed yet.")



