import streamlit as st

from tasks import cust_tasks_obj
from agents import agents_lst
from crewai import Crew, Process

st.title("CrewAI Powered Customer Support Agents")

query = st.text_input("Enter your Query Here ")

if (query):
    Customer_Query_catergorize = cust_tasks_obj.categorize_query(query=query)
    Track_Orders = cust_tasks_obj.track_order_details(query = query)
    Track_Returns = cust_tasks_obj.track_returns_details(query = query)
    prod_recom = cust_tasks_obj.prod_recommendation_details(query)

    tasks_lst = [Customer_Query_catergorize,Track_Orders,Track_Returns,prod_recom]


    crew = Crew(
        agents=agents_lst,
        tasks=tasks_lst,
        process=Process.sequential,
        Verbose = 0,
        full_output=True
    )

    result = crew.kickoff()

    if Customer_Query_catergorize.output.exported_output == 'order_tracking':
        st.write(Track_Orders.output.exported_output)
    elif Customer_Query_catergorize.output.exported_output == 'returns_request':
        st.write(Track_Returns.output.exported_output)
    elif Customer_Query_catergorize.output.exported_output == 'prod_recommendations':
        st.write(prod_recom.output.exported_output)