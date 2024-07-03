#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# In[2]:


df = pd.read_csv('Transaction_data.csv', index_col=0)

df.head()


# In[3]:


df['TIME'] = df['TIME'].apply(lambda x: x.split(' ')[2])


# In[4]:


df['datetime'] = pd.to_datetime(df['recorded_date'] + ' ' + df['TIME'])
df.drop(['recorded_date','TIME'], axis=1, inplace=True)


# In[5]:


df.head()


# In[6]:


def categorize_time(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 22:
        return 'Evening'
    else:
        return 'Night'

df['time_of_day'] = df['datetime'].dt.hour.map(categorize_time)
df.head()


# In[7]:


df_nep = df[df['issuer_id'] != "b92056d9-092b-4374-a84f-89304b67dec1"]
df_npci = df[df['issuer_id'] == "b92056d9-092b-4374-a84f-89304b67dec1"]


# In[8]:


df_nep


# In[9]:


nep_grouped_stats = df_nep.groupby('merchant_id').agg({
    'amount': ['count', 'sum', 'min', 'max', 'mean', 'std'],
    'time_of_day': lambda x: pd.Series.mode(x).iloc[0]  
})


# In[10]:


nep_grouped_stats.columns = ['count','sum','min','max','mean','std','time_of_day']


# In[11]:


nep_grouped_stats


# In[12]:


npci_grouped_stats = df_npci.groupby('merchant_id').agg({
    'amount': ['count', 'sum', 'min', 'max', 'mean', 'std'],
    'time_of_day': lambda x: pd.Series.mode(x).iloc[0]  
})


# In[13]:


npci_grouped_stats.columns = ['count','sum','min','max','mean','std','time_of_day']


# In[14]:


npci_grouped_stats


# In[15]:


df_merged = pd.concat([nep_grouped_stats, npci_grouped_stats], keys=['nep', 'npci'], names=['source']).reset_index(level=0)


# In[66]:


merchant_stats = df_merged.groupby(['merchant_id', 'source']).agg({
    'count': 'mean',
    'sum': 'mean',
    'min': 'min',
    'max': 'max',
    'mean': 'mean', 
    'std': 'mean',   
    'time_of_day': lambda x: pd.Series.mode(x).iloc[0] 
}).unstack()

merchant_stats.columns = ['_'.join(col).strip() for col in merchant_stats.columns.values]
merchant_stats


# In[31]:


merchant_stats.dropna(inplace=True)


# In[32]:


merchant_stats.columns


# In[67]:


def compare_groups(data):
    results = {}
    nep_cols = ['count_nep', 'sum_nep', 'min_nep', 'max_nep', 'mean_nep','std_nep']
    npci_cols = ['count_npci', 'sum_npci', 'min_npci', 'max_npci', 'mean_npci','std_npci']
    
    for col1, col2 in zip(nep_cols, npci_cols):
        # Compare 'npci' > 'nep' and count True values
        npci_greater_count = sum(data[col2] > data[col1])
        total_count = len(data)
        
        # Calculate percentage where 'npci' is greater than 'nep'
        percentage_greater = (npci_greater_count / total_count) * 100
        
        results[(col1, col2)] = {
            'npci_greater_count': npci_greater_count,
            'total_count': total_count,
            'percentage_greater': percentage_greater
        }
    
    return results


# In[68]:


results = compare_groups(merchant_stats)


# In[69]:


for key, result in results.items():
    col1, col2 = key
    print(f"Comparison of {col1} and {col2}:")
    print(f"   Number of merchants where {col2} > {col1}: {result['npci_greater_count']} / {result['total_count']} ({result['percentage_greater']:.2f}%)")
    print()


# In[45]:


def plot_distributions(df):
    # Iterate through each column
    for col in merchant_stats.drop(columns = ['std_nep', 'std_npci', 'time_of_day_nep', 'time_of_day_npci'], axis = 1).columns:
        plt.figure(figsize=(8, 5))
        df[col].plot(kind='hist', bins=100, density=True, alpha=0.75, label=col + ' histogram')
        df[col].plot(kind='kde', color='red', linewidth=2, label=col + ' KDE')
        plt.xlabel(col)
        plt.title(f'Distribution of {col}')
        plt.legend()
        plt.show()


# In[46]:


plot_distributions(merchant_stats)


# In[77]:


merchant_stats_1 = merchant_stats.drop(columns=['time_of_day_nep', 'time_of_day_npci'])
merchant_stats_1.dropna(inplace=True)


# In[78]:


scaler = StandardScaler()
normalized_data = scaler.fit_transform(merchant_stats_1)


# In[88]:


inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(normalized_data)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), inertia, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.grid(True)
plt.show() 


# In[89]:


from sklearn.metrics import silhouette_score

silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(normalized_data)
    score = silhouette_score(normalized_data, kmeans.labels_)
    silhouette_scores.append(score)

plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for Optimal k')
plt.grid(True)
plt.show()


# In[79]:


kmeans = KMeans(n_clusters=4, random_state=42)  # Choose appropriate number of clusters
kmeans.fit(normalized_data)


# In[82]:


merchant_stats_1['cluster'] = kmeans.labels_


# In[91]:


from sklearn import metrics


wcss = []
silhouette_scores = []
max_clusters = 10

for i in range(1, max_clusters+1):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(normalized_data)
    wcss.append(kmeans.inertia_)  # inertia_ is the within-cluster sum of squares
    if i > 1:
        silhouette_scores.append(metrics.silhouette_score(normalized_data, kmeans.labels_))


# In[92]:


# Plotting the Elbow curve
plt.figure(figsize=(12, 5))

# Plotting the Elbow curve
plt.subplot(1, 2, 1)
plt.plot(range(1, max_clusters+1), wcss, marker='o', linestyle='--')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal k')
plt.grid()

# Plotting the Silhouette Score curve
plt.subplot(1, 2, 2)
plt.plot(range(2, max_clusters+1), silhouette_scores, marker='o', linestyle='--')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score for Optimal k')
plt.grid()

plt.tight_layout()
plt.show()


# In[169]:


# Choose the optimal number of clusters based on the Elbow and Silhouette Score plots
optimal_k = 3  # Adjust based on the Elbow and Silhouette Score plots

# Apply K-means clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(normalized_data)

# Add cluster labels to the dataframe
merchant_stats_1['cluster'] = kmeans.labels_

# Visualize clusters (Example with 2D PCA plot)


# In[170]:


plt.figure(figsize=(10, 6))

from sklearn.decomposition import PCA

# Reduce dimensions for visualization
pca = PCA(n_components=2)
principal_components = pca.fit_transform(normalized_data)

# Create a DataFrame for the reduced data
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# Add cluster labels to the reduced DataFrame
pca_df['Cluster'] = kmeans.labels_

for cluster in sorted(pca_df['Cluster'].unique()):
    cluster_data = pca_df[pca_df['Cluster'] == cluster]
    plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {cluster}')

plt.title('K-means Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.grid(True)
plt.show()


# In[172]:


cluster_centers = pd.DataFrame(scaler.inverse_transform(kmeans.cluster_centers_), columns=merchant_stats_1.columns[:-1])
print("\nCluster Centers:")
cluster_centers


# In[173]:


kmeans.cluster_centers_


# In[174]:


unique_values, _, counts = np.unique(kmeans.labels_, return_index=True, return_counts=True)

print("Unique values:", unique_values)
print("Counts of unique values:", counts)


# In[175]:


suspicious_clusters = []

for cluster_label, cluster_center in enumerate(kmeans.cluster_centers_):

    if cluster_center[9] > 2 and cluster_center[2] < cluster_center[3]:  
        suspicious_clusters.append(cluster_label)


suspicious_merchants = merchant_stats_1[merchant_stats_1['cluster'].isin(suspicious_clusters)]
print("\nSuspicious Merchants:")
suspicious_merchants


# In[154]:


# # Identify suspicious clusters based on unusual transaction patterns
# suspicious_clusters = []
# 
# for cluster_label, cluster_center in enumerate(kmeans.cluster_centers_):
#     # Extract NPCI and NEP metrics from the cluster center
#     sum_nep = cluster_center[2]
#     sum_npci = cluster_center[3]
#     count_nep = cluster_center[0]
#     count_npci = cluster_center[1]
#     
#     # Define criteria for suspicion
#     unusual_sum = sum_npci > sum_nep
#     unusual_mean = count_npci < count_nep
#     
#     # If any criteria are met, mark the cluster as suspicious
#     if unusual_sum or unusual_mean:
#         suspicious_clusters.append(cluster_label)
# 
# # Flag merchants in suspicious clusters
# suspicious_merchants = merchant_stats_1[merchant_stats_1['cluster'].isin(suspicious_clusters)]
# 
# print("\nSuspicious Merchants:")
# suspicious_merchants

