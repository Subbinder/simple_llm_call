
import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv
import os
load_dotenv()

llm=ChatOpenAI(model="claude-3-haiku",
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"))

dataset_prompt=PromptTemplate.from_template("""You are a expert dataset builder
                                            Provide me the dataset for the {domain} for about 50 rows and 10 colums.
                                            
                                            dataset:
                                            """)

mltask_prompt=PromptTemplate.from_template("""you are a experienced ML engineer
                                        Decide which Machine learning task to be done based on the {domain}
                                        and explain in 2 lines
                                        
                                        ML_Task:
                                        """)

modelsug_prompt=PromptTemplate.from_template("""you are a experienced ML engineer
                                            Suggest me the ML model to based on the {domian} which gives me very accuracy 
                                            
                                            Model:
                                        """)

eval_prompt=PromptTemplate.from_template("""you are aexpert ML engineer 
                                        Suggest me the evaluation matrics based on the {domain}
                                        
                                        Evaluation_Metrics:
                                        """)

dataset_chain=dataset_prompt|llm
mltask_chain=mltask_prompt|llm
modelsug_chain=modelsug_prompt|llm
eval_chain=eval_prompt|llm

pipeline=RunnablePassthrough()|RunnableParallel(
    dataset=lambda x:dataset_chain.invoke(x).content,
    ml_task=lambda x:mltask_chain.invoke(x).content,
    model = lambda x: modelsug_chain.invoke(x).content,
    eval_metrics=lambda x:eval_chain.invoke(x).content
)

domian=st.text_input("Enter the domain:")

if st.button("Generate"):

    result=pipeline.invoke({domian})

    st.subheader("Dataset:")
    st.write(result['dataset'])
    
    st.subheader("ML Task:")
    st.write(result['ml_task'])

    st.subheader("Model:")
    st.write(result['model'])

    st.subheader("Evaluation Metrics")
    st.write(result['eval_metrics'])



