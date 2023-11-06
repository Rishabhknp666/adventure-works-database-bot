from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from sqlalchemy import create_engine
import streamlit as st

with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
     -[streamlit](https://streamlit.io/)
    -[Langchain](https://www.langchain.com/)
    -[OpenAI](https://openai.com/)
                

    ''')

    add_vertical_space(5)
    st.write('Made with love by [Rishabh]





st.title("Talk to your data")
api_key = st.text_input("api_key")
db_string = 'mssql+pyodbc://YourUsername:YourPassword@YourServerName/AdventureWorks?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(db_string)
db_string = st.text_input("db_string")

api_key:
    db = SQLDatabase.from_uri(db_string)
    toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0, openai_api_key=api_key))
    agent_executor = create_sql_agent(
        llm=OpenAI(temperature=0, streaming=True, openai_api_key=api_key),
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )



if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_executor.run(prompt, callbacks=[st_callback])
        
        st.write(response)



if __name__ == "__main__":
    main()
