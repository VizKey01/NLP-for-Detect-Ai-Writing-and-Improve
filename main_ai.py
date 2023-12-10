import streamlit as st
import openai
import pandas as pd
import json
from Prompts_text import prompt1, prompt2, prompt3, prompt4, prompt5

# ex formatted: 
# [ { "before": "Hello world here", "after": "Hello, everyone! I am here.",
#  "category": "style", 
# "comment": "Added a greeting and made the sentence more expressive." } ]

def init():
    # Set up the streamlit app
    st.set_page_config(
        page_title='AI Text Analyzer',
        page_icon= '🤖'
    )

# def analyze_and_rewrite(api_key, user_input):


def main():
    init()
    st.header('AI Text Analyzer 🤖')
    st.markdown('Input the writing that you want to check.')

    # Set up key
    my_api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

    user_input = st.text_area("Enter the text to analyze:", placeholder="Your text here...")
    
    your_option = st.selectbox(
        "Which Function you want to do?",
        ('pnan', 'Rewriter', 'Translator', 'Auto-Corrector', 'Summarizer'),
        index=None,
        placeholder="Select Function...",
    )
    st.write('You selected:', your_option)

    #Function Selected
    if your_option == 'pnan': your_option = prompt1
    elif your_option == 'Rewriter': your_option = prompt2
    elif your_option == 'Translator': 
        lang_option = st.selectbox(
            "Which language do you want to translate to?",
            ("German", "French", "Spanish", "Italian", "Portuguese", "Japanese", "Chinese", "Russian", "Korean", "Arabic", "Hindi", "Turkish", "Thai"),
            index=None,
            placeholder="Select language...",
        )
        st.write('You selected:', lang_option)
        your_option = prompt3.format(lang_option)
    elif your_option == 'Auto-Corrector': your_option = prompt4
    elif your_option == 'Summarizer': your_option = prompt5
    
    
    client = openai.OpenAI(api_key=my_api_key)
    
    if st.button('Submit') and my_api_key:
        messages_so_far = [
            {"role": "system", "content": your_option},
            {'role': 'user', 'content': user_input},
        ]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages_so_far
        )
        # Show the response from the AI in a box
        st.markdown('**AI response:**')
        suggestion_answer = response.choices[0].message.content
        st.markdown("DEBUG answer:")
        st.markdown(suggestion_answer)
        st.markdown("--------------------------------")

        
        if your_option == 'Translater':
            st.markdown(sd[0])
            st.markdown("10 interesting vocabularies")
            sd = sd[1]
        
        sd = json.loads(sd)
        print (sd)
        suggestion_df = pd.DataFrame.from_dict(sd)
        print(suggestion_df)
        st.table(suggestion_df)


if __name__ == "__main__":
    main()


### Our journey through the diverse culinary landscapes of Southeast Asia, the Mediterranean, and South America has only scratched the surface of the world's gastronomic wonders. From street food stalls to elegant dining establishments, the global tapestry of flavors invites us to explore, savor, and appreciate the unique stories each dish tells. So, let your taste buds be your guide as you embark on a culinary adventure, discovering the extraordinary in the everyday delights of food.