# PCA & Clustering — Concepts & Definitions

## 1. Where This Fits in Unsupervised Learning

Unsupervised learning has two major families of techniques:

- **Clustering** (e.g., K-Means) — groups similar data points together
- **Dimensionality Reduction** (e.g., PCA) — reduces the number of features while keeping as much important information as possible

They're often used **together**: PCA first to simplify/compress the data, then clustering on the simplified data. This combination is what the practice notebook (`PCA_Clustering_Practice.ipynb`) demonstrates.

---

## 2. What is PCA (Principal Component Analysis)?

PCA is a technique that takes data with many features (dimensions) and compresses it into fewer new features, called **principal components**, while preserving as much of the original variation (information) as possible.

### Why do we need it?

- **Visualization** — humans can only see in 2D or 3D. If your data has 10, 30, or 100 features, you can't plot it directly. PCA can compress it down to 2 or 3 components so you *can* plot and visually inspect it.
- **Reducing noise/redundancy** — many real-world features are correlated with each other (e.g., height in cm and height in inches). PCA combines correlated features into fewer, more informative ones.
- **Speeding up other algorithms** — fewer features means faster training for downstream models, including clustering.
- **Fighting the "curse of dimensionality"** — distance-based algorithms like K-Means can behave poorly when there are too many features; PCA helps by reducing dimensions first.

### Key Concepts

**Principal Component (PC)**
A new, artificial feature created by PCA. It's a specific weighted combination (linear combination) of all the original features. PC1 (the first component) captures the *most* variation in the data; PC2 captures the *next most* (and is mathematically required to be independent/uncorrelated with PC1); and so on.

**Variance**
How spread out the data is. PCA works by finding the directions (components) along which the data varies the most — because more spread usually means more information.

**Explained Variance Ratio**
For each principal component, this tells you what percentage of the original data's total information (variance) that component captures. E.g., "PC1 explains 73% of the variance" means most of the story is captured in just that one new feature.

**Dimensionality Reduction**
The general idea of reducing the number of features (columns) while keeping the data as useful as possible. PCA is the most common technique for this.

### Important: Always Scale Before PCA

PCA is based on variance, and variance is affected by the scale of a feature. A feature measured in the thousands (like income) would dominate a feature measured in single digits (like age) purely because of its scale — not because it's actually more important. **Always apply `StandardScaler` before PCA.**

### Real-World Analogy

Imagine describing a person using 50 different measurements — height, weight, shoulder width, arm length, leg length, etc. Many of these are correlated (a taller person tends to have longer arms and legs too). PCA would notice this and might combine them into 2–3 new "super-features" like *overall body size* and *body proportion*, which capture most of what those 50 measurements were really telling you.

---

## 3. How PCA Works (Step by Step, Conceptually)

1. **Standardize the data** so all features are on the same scale.
2. **Find the direction of maximum variance** in the data — this becomes Principal Component 1 (PC1).
3. **Find the next direction of maximum variance**, that is perpendicular (uncorrelated) to PC1 — this becomes PC2. Repeat for as many components as needed.
4. **Project the original data** onto these new component axes — this gives you the transformed, lower-dimensional dataset.
5. **Choose how many components to keep**, usually by looking at the cumulative explained variance (e.g., "keep enough components to explain 90–95% of the variance").

---

## 4. What is Clustering (Recap)?

Clustering groups similar data points together without using any labels — see `KMeans_Concepts.md` for the full write-up on K-Means specifically. The most common algorithm is **K-Means**, which assigns points to the nearest of K centroids and updates those centroids iteratively.

---

## 5. Why Combine PCA + Clustering?

- **Better visualization of clusters** — you can run K-Means on the full, high-dimensional data, then use PCA (reduced to 2D) purely to *plot* the resulting clusters in a way humans can see.
- **Better clustering performance** — sometimes running PCA *before* K-Means (instead of just for visualization) removes noisy, redundant features and can produce cleaner, more meaningful clusters — especially on datasets with many features.
- **Faster clustering** — fewer dimensions mean K-Means has less work to do, which matters on large datasets.

### Typical Workflow

```
Raw data (many features)
   → Scale features (StandardScaler)
   → Apply PCA (reduce to fewer components)
   → Apply K-Means on the PCA-reduced data
   → Visualize the clusters using the first 2 principal components
```

---

## 6. Common Use Cases

- **Customer segmentation** with many behavioral features — PCA compresses them, then clustering finds segments
- **Image compression / facial recognition** — PCA on pixel data (this specific application is famously called "Eigenfaces")
- **Genomics** — reducing thousands of gene expression features down to a manageable number before clustering patients into subtypes
- **Exploratory data analysis** — quickly visualizing whether high-dimensional data has any natural grouping at all

---

## 7. Quick Reference — scikit-learn Usage

```python
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Always scale first
X_scaled = StandardScaler().fit_transform(X)

# 2. Apply PCA
pca = PCA(n_components=2)          # reduce to 2 components for visualization
X_pca = pca.fit_transform(X_scaled)

print(pca.explained_variance_ratio_)   # how much info each component captures

# 3. Cluster the PCA-reduced data
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_pca)
```

See `PCA_Clustering_Practice.ipynb` for a full hands-on example with visualizations, an explained-variance plot, and a comparison of clustering with vs. without PCA.
