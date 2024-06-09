from crewai_tools import FileReadTool

# Initialize the tool with a specific file path, so the agent can only read the content of the specified file
order_details_data = FileReadTool(file_path='F:/LLM_Project/CrewAI_Duplicate/sample_data/order_management_data.csv')
returns_data = FileReadTool(file_path='F:/LLM_Project/CrewAI_Duplicate/sample_data/returns_and_refunds_data.csv')
recommendation_data = FileReadTool(file_path='/F:/LLM_Project/CrewAI_Duplicate/sample_data/recommendation_data.csv')