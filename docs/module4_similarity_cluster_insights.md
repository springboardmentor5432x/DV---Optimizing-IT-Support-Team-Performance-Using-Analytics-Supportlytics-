# Module 4: Similarity and Cluster Insights

## What was done
- Text column used for clustering: `Ticket Subject`
- Vectorization: TF-IDF (1-2 grams), max_features=5000
- Clustering: KMeans with k=6

## Key outputs
- Average similarity within each cluster
- Cluster size vs issue type composition
- Performance gaps (resolution duration + priority) across clusters

## Problem clusters (candidates)
Clusters with high median resolution time and/or high-priority ratio are flagged.

 cluster  size  avg_similarity  median_resolution_hours  high_priority_ratio
       1  1613        0.473219                 0.791667             0.510229
       5  1063        0.627067                 0.308333             0.494826
       0  2568        0.199979                 0.266667             0.493769
       3  1100        0.624351                -0.083333             0.500000
       2  1551        0.468294                -0.425000             0.508704
       4   574        1.000000                -0.750000             0.449477
