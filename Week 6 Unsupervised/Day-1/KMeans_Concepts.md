# K-Means Clustering — Concepts & Definitions

## 1. What is Unsupervised Learning?

In **supervised learning** (like the Heart Disease project), we have input features (X) *and* a known answer/label (y) — the model learns to map X to y.

In **unsupervised learning**, we only have input features (X) — there is **no label**. The model's job is to find hidden structure or patterns in the data on its own.

**K-Means Clustering** is one of the most common unsupervised learning algorithms. It groups similar data points together into clusters, without ever being told what the "correct" groups are.

---

## 2. What is K-Means?

K-Means is a **clustering algorithm** that partitions data into **K groups (clusters)**, where each data point belongs to the cluster with the nearest **centroid** (the center point of that cluster).

- **K** = the number of clusters you want to find (you choose this number beforehand)
- **Centroid** = the average position of all points in a cluster — think of it as the cluster's "center of mass"
- **Cluster** = a group of data points that are close to each other and far from points in other clusters

### Real-world analogy

Imagine you have a bag of mixed candies with no labels, and you want to sort them into 3 piles based on color and size alone (no one tells you the flavor). You'd naturally group similar-looking candies together. That's exactly what K-Means does with numeric data — it groups similar rows together based on how close their feature values are.

---

## 3. How K-Means Works (Step by Step)

1. **Choose K** — decide how many clusters you want (e.g., K = 3).
2. **Initialize centroids** — randomly place K centroid points in the data space.
3. **Assign step** — each data point is assigned to its **nearest centroid** (usually measured with Euclidean distance).
4. **Update step** — each centroid moves to the **average position** of all points assigned to it.
5. **Repeat** steps 3 and 4 until the centroids stop moving much (the algorithm has "converged").

This loop is why the algorithm is sometimes described as "assign, then average, repeat."

---

## 4. Key Concepts

### Euclidean Distance
The straight-line distance between two points, used to decide which centroid a point is closest to:

```
distance = sqrt((x1-x2)² + (y1-y2)²)
```

### Inertia (Within-Cluster Sum of Squares)
A measure of how tightly packed the points are within each cluster — the sum of squared distances between each point and its cluster's centroid. **Lower inertia = tighter, more compact clusters.**

### The Elbow Method
Since we must choose K ourselves, the Elbow Method helps pick a good value:
1. Run K-Means for a range of K values (e.g., 1 to 10)
2. Plot inertia against K
3. Look for the "elbow" — the point where inertia stops dropping sharply and starts flattening out
4. That K is usually a good choice

### Feature Scaling
K-Means relies on distance calculations, so features with larger numeric ranges (e.g., income in thousands vs. age in years) can dominate the result. **Always scale your features** (e.g., with `StandardScaler`) before applying K-Means.

---

## 5. Strengths and Limitations

**Strengths:**
- Simple to understand and fast to run, even on large datasets
- Works well when clusters are roughly round/spherical and similar in size

**Limitations:**
- You must choose K in advance
- Sensitive to the initial random centroid placement (though `k-means++` initialization, the scikit-learn default, helps a lot)
- Struggles with clusters of very different sizes, densities, or non-circular shapes
- Sensitive to outliers, since they pull the centroid average

---

## 6. Common Use Cases

- **Customer segmentation** — grouping customers by purchasing behavior for targeted marketing
- **Image compression** — reducing the number of colors in an image by clustering similar pixel colors
- **Document/topic grouping** — grouping similar articles or documents together
- **Anomaly detection** — points that don't fit well into any cluster may be outliers

---

## 7. Example Walkthrough (Conceptual)

Suppose you have data on mall customers with two features: **Annual Income** and **Spending Score**. Without any labels telling you customer "types," K-Means can automatically discover groups such as:

- Cluster 1: High income, high spending → "target premium customers"
- Cluster 2: Low income, high spending → "impulsive spenders"
- Cluster 3: High income, low spending → "cautious spenders"
- Cluster 4: Low income, low spending → "budget-conscious customers"

This is exactly the kind of pattern the accompanying practice notebook (`KMeans_Practice.ipynb`) demonstrates hands-on — first with simple generated data, then with the Elbow Method to pick K, and finally by visualizing the resulting clusters.

---

## 8. Quick Reference — scikit-learn Usage

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Always scale first
X_scaled = StandardScaler().fit_transform(X)

# Create and fit the model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# Get cluster assignments and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_
```

See `KMeans_Practice.ipynb` for a full hands-on example with visualizations.
