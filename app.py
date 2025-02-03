import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load your CSV file
file_path = 'ticket_questions.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Extract the 'Subject' column
questions = df['Subject'].dropna().tolist()

# Convert text to numerical data using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(questions)

# Apply KMeans clustering for 100 unique question groups
num_clusters = 100
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Assign cluster labels to each question
df['Cluster'] = kmeans.labels_

# Simplify questions by picking a representative from each cluster
refined_questions = []
for cluster, questions_list in df.groupby('Cluster')['Subject']:
    sample_question = questions_list.iloc[0]  # First question as a simple representative
    refined_questions.append({
        'Simplified Question': sample_question,
        'Original Questions Count': len(questions_list)
    })

# Save to a new CSV
refined_df = pd.DataFrame(refined_questions)
output_path = 'refined_customer_questions.csv'
refined_df.to_csv(output_path, index=False)

print(f"Refined questions saved to {output_path}")

