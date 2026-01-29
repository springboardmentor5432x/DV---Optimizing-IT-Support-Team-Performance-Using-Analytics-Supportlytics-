# =====================================================
# Exploratory Data Analysis (Module 3)
# =====================================================

def bar_plot(series, title):
    series.plot(kind='bar')
    plt.title(title)
    plt.tight_layout()
    plt.show()


print("Generating EDA plots...")

bar_plot(df['Type'].value_counts(), "Ticket Type Distribution")
bar_plot(df['Category'].value_counts().head(10), "Top Ticket Categories")
bar_plot(df['Priority'].value_counts(), "Tickets by Priority")
bar_plot(df['Assigned_To'].value_counts().head(10), "Tickets by Assigned Queue")
bar_plot(df.groupby('Priority')['Resolution_Duration'].mean(),
         "Average Resolution Time by Priority")


# =====================================================
# Clustering (Module 4)
# =====================================================

print("Applying KMeans clustering...")

cluster_data = df[['Priority_Score', 'Resolution_Duration']].copy()

max_duration = cluster_data.loc[
    cluster_data['Resolution_Duration'] >= 0, 'Resolution_Duration'
].max()

cluster_data['Resolution_Duration'] = cluster_data['Resolution_Duration'].replace(
    -1, max_duration + 24
)

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(cluster_data)


# =====================================================
# Similarity Score
# =====================================================

scaler = StandardScaler()
scaled = scaler.fit_transform(cluster_data)

centroids = scaler.transform(
    df.groupby('Cluster')[['Priority_Score', 'Resolution_Duration']].mean()
)

distances = [
    np.linalg.norm(scaled[i] - centroids[int(c)])
    for i, c in enumerate(df['Cluster'])
]

df['Similarity_Score'] = 1 / (1 + np.array(distances))


# =====================================================
# Cluster Visualizations
# =====================================================

print("Generating cluster visualizations...")

# Boxplot
df.boxplot(column='Similarity_Score', by='Cluster')
plt.title("Similarity Scores by Cluster")
plt.suptitle("")
plt.show()


# Stacked bar
cluster_issue = pd.crosstab(df['Cluster'], df['Category'])
cluster_issue.plot(kind='bar', stacked=True)
plt.title("Cluster Size vs Issue Type")
plt.tight_layout()
plt.show()


# Scatter
cluster_size = df.groupby('Cluster').size()
avg_similarity = df.groupby('Cluster')['Similarity_Score'].mean()

plt.scatter(cluster_size, avg_similarity)
plt.xlabel("Cluster Size")
plt.ylabel("Average Similarity Score")
plt.title("Cluster Size vs Average Similarity")
plt.grid(True)
plt.show()


# Heatmap
plt.imshow(cluster_issue.values, aspect='auto')
plt.colorbar(label='Frequency')
plt.xticks(range(len(cluster_issue.columns)), cluster_issue.columns, rotation=45)
plt.yticks(range(len(cluster_issue.index)), cluster_issue.index)
plt.title("Cluster vs Issue Type Heatmap")
plt.show()
