# Unsupervised Learning — K-Means & PCA (Easy Concepts)

## 1. What is Unsupervised Learning?

In **supervised learning**, we have input data (X) *and* a known answer (y) — the model learns to map X to y.

In **unsupervised learning**, we only have input data (X) — there is **no answer given**. The model finds patterns or structure on its own.

Two common unsupervised techniques:
- **Clustering (K-Means)** — groups similar data points together
- **Dimensionality Reduction (PCA)** — reduces the number of features while keeping the important information

---

## 2. K-Means Clustering

K-Means groups data into **K clusters**, based on which points are closest to each other.

- **K** = number of groups you want (you choose this)
- **Centroid** = the center point of a cluster
- **Cluster** = a group of nearby, similar points

### How it works
1. Choose K (number of clusters).
2. Randomly place K centroids.
3. Assign each point to its nearest centroid.
4. Move each centroid to the average position of its assigned points.
5. Repeat steps 3–4 until centroids stop moving.

### Elbow Method (Choosing K)
Since we must pick K ourselves, we run K-Means for a range of K values and plot **inertia** (how tight the clusters are) against K. Look for the "elbow" — where the curve bends and flattens. That's usually a good K.

### Important
Always **scale your features** before K-Means, since it relies on distance.

### Real-world analogy
Sorting a bag of mixed candies into piles by color/size, with no one telling you the "correct" groups — you just group similar-looking ones together.

---

## 3. PCA (Principal Component Analysis)

PCA reduces data with many features down to a smaller number of new features (**principal components**), while keeping as much information as possible.

### Why use it?
- **Visualization** — humans can only see in 2D/3D, so PCA compresses many features down to 2–3 so we can plot them.
- **Removes redundancy** — many features are correlated; PCA combines them into fewer, more useful ones.
- **Speeds up other algorithms**, including clustering.

### Key terms
- **Principal Component (PC)** — a new feature made by combining the original features. PC1 captures the most variation, PC2 the next most, etc.
- **Explained Variance Ratio** — how much of the original information each component keeps.

### Important
Always **scale your features** before PCA too, since it's based on variance.

### Real-world analogy
Describing a person with 50 measurements (height, arm length, leg length...) — many are correlated, so PCA might combine them into 2–3 "super-features" like *overall size*.

---

## 4. Why Combine PCA + K-Means?

- Run PCA first to reduce many features down to 2 dimensions.
- Then run K-Means on the reduced data.
- This makes it possible to **visualize the clusters**, and can also make clustering cleaner and faster on datasets with lots of features.

```
Raw data (many features)
   → Scale features
   → Apply PCA (reduce to fewer components)
   → Apply K-Means on the reduced data
   → Plot the clusters
```

---

## 5. Common Use Cases

- Customer segmentation
- Image compression
- Grouping similar documents/articles
- Simplifying data with many features before further analysis

---

## 6. Quick Reference — scikit-learn

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Always scale first
X_scaled = StandardScaler().fit_transform(X)

# PCA — reduce to 2 components
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# K-Means — cluster the data
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_pca)
```

See `Unsupervised_Practice.ipynb` for a hands-on notebook covering both K-Means and PCA + Clustering.
