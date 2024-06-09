**Use Case:**
The system aims to handle various customer service requests, such as order status inquiries, 
return processing and personalized product recommendations. Multiple agents collaborate to provide comprehensive and efficient customer support

#################################################################################################

**Agents and their Roles:**

  1. Query Categorizer Agent:
  
  Task: Analyze the customer's query to categorize it into one of the following categories: \
              order_tracking - used when someone is asking for information about shipment of their orders \
              returns_request - used when someone is enquiring about returns process \
              prod_recommendations
              
  Output: Customer intent (e.g., "order status inquiry", "return request", "product recommendation") and extracted details (e.g., order ID, product name).

  2. Order Management Agent:
  
  Task: Handle queries related to order status.
  Input: Intent and order details from the Query Categorizer agent.
  Output: Current status of the order and estimated delivery time.

  3. Returns and Refunds Agent:
  
  Task: Process return requests.
  Input: Intent and order details from the Query Categorizer agent.
  Output: Instructions for returning the product and processing the refund.

  4. Recommendation Agent:
  
  Task: Suggest products based on customer preferences and browsing history.
  Input: Customer profile data and current query context from the Query Categorizer agent.
  Output: Personalized product recommendations.

**Workflow**

<img width="583" alt="image" src="https://github.com/shaikasheesh/crew_ai_agents/assets/63601317/b789b978-f121-4934-9c03-6ecf6d885a4e">

_
**Sample Outputs**_

1. Order Tracking:

<img width="943" alt="image" src="https://github.com/shaikasheesh/crew_ai_agents/assets/63601317/d0b27499-5249-4b66-9de5-1c3aa3ebcb3c">

2. Returns Processing:

<img width="942" alt="image" src="https://github.com/shaikasheesh/crew_ai_agents/assets/63601317/2fa91ced-bf4c-4d49-a81e-286d9f541715">

3. Product Recommendations:

