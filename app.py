import streamlit as st
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')  # use a local server
tool = language_tool_python.LanguageToolPublicAPI('en-US') # or use public API

def text_correction(text):
    return tool(text)

def main():
    st.header('Spelling and Grammer Correction App')
    text_area = st.text_area('Enter your text...')
    if text_area is not None:
         if st.button('Submit'):
            st.write('Input text is: ')
            st.success(text_area)
            corrected_text = text_correction(text_area)
            st.write(corrected_text)

if __name__ == '__main__':
    main()
