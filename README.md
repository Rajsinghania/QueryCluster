# QueryCluster
Simple and descriptive, highlighting the clustering of customer queries.

# QueryCluster
QueryCluster is a Python-based tool designed to streamline and refine customer queries by clustering similar questions together and simplifying them into clear, concise versions. This is especially useful for customer support teams looking to reduce redundancy and improve response efficiency.

# Features

# Automatic Clustering: 
Groups similar customer queries using machine learning algorithms.

# Simplified Questions: 
Reformulates multiple similar questions into a single, clear query.

# Question Count: 
Tracks how many original queries were merged into each simplified version.

# CSV Output: 
Exports refined questions and counts to a CSV file for easy integration.

# Usage

Prepare Your CSV FileEnsure your CSV file has a column named 'Subject' containing the customer queries.

# Run the Script
python refine_questions.py

Check the OutputA new file called refined_customer_questions.csv will be generated, containing:

Simplified Questions

Original Questions Count

Example

# Input (CSV):
Subject
"How can I reset my password?"
"I forgot my password, what should I do?"
"Reset password instructions?"

# Output (CSV):
Simplified Question,Original Questions Count
"How can I reset my password?",3
