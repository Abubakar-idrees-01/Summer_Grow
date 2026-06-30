# Linear Algebra for Data Science — Concept Notes

*Companion notes to your topic/resource table — what each idea actually means, and where it shows up in real data science work.*

## Contents
1. Scalars & Vectors
2. Dot Product
3. Cross Product
4. Matrices
5. Matrix Multiplication
6. Systems of Linear Equations
7. Gaussian Elimination
8. Matrix Inverse
9. Determinants
10. Rank
11. Vector Spaces
12. Span, Basis & Dimension
13. Linear Independence
14. Orthogonality
15. Projections
16. Norms
17. Cosine Similarity
18. Linear Transformations
19. Eigenvalues & Eigenvectors
20. Positive Definite Matrices
21. Singular Value Decomposition (SVD)
22. PCA

---

## 1. Scalars & Vectors

A **scalar** is just a single number — magnitude, no direction: a temperature, a price, a count. A **vector** is an ordered list of numbers that carries both magnitude and direction, or more simply, a point in space described by its coordinates. In data science, this is the most basic and most important idea in the whole subject: every row in your dataset, every customer profile, every image's pixel grid, every word embedding — all of it is represented as a vector. A dataset with 10 features is just a collection of points living in 10-dimensional space. Once you see rows as vectors, almost everything else in this list (dot products, norms, projections) becomes a tool for measuring relationships *between* those points — how far apart they are, how similar they are, how they cluster. This is the foundation everything else builds on.

*Resource: 3Blue1Brown — search "3Blue1Brown vectors essence of linear algebra 1"*

---

## 2. Dot Product

The **dot product** of two vectors multiplies their corresponding entries and sums the results, producing a single number. Geometrically, it tells you how much two vectors point in the same direction — large and positive when they align, zero when they're perpendicular, negative when they point apart. In data science, the dot product is everywhere: it's the core arithmetic of a neural network (each neuron computes a weighted sum, which is literally a dot product of inputs and weights), it underlies cosine similarity for comparing text or recommendation vectors, and it's the basic operation that makes matrix multiplication possible. Understand the dot product well, and a huge fraction of what's "happening" inside a neural network or a similarity search suddenly makes intuitive sense — it's just vectors checking how aligned they are.

*Resource: 3Blue1Brown — search "3Blue1Brown dot product"*

---

## 3. Cross Product

The **cross product** is defined only for two 3D vectors and produces a third vector that's perpendicular to both — its length equals the area of the parallelogram the two original vectors span. It's less central to everyday data science than the dot product, but it shows up wherever you're working with genuine 3D geometry: computer vision (estimating surface normals, camera orientation), robotics (computing torques and rotations), and physics-informed ML models. You won't use it as often as the dot product, but knowing what it represents — perpendicularity and spanned area — is usually enough unless your work touches 3D point clouds or graphics directly.

*Resource: 3Blue1Brown — search "3Blue1Brown cross product"*

---

## 4. Matrices

A **matrix** is a rectangular grid of numbers arranged in rows and columns. It can represent three things at once, and learning to switch between these views is the key skill: a dataset (rows = samples, columns = features), a linear transformation (something that moves vectors around), or a system of equations. In data science, matrices are the default data structure — a pandas DataFrame is conceptually a matrix, a grayscale image is a matrix, a batch of training examples fed into a neural network is a matrix, and every weight layer in that network is also a matrix. Once you're comfortable with matrices, you can read an entire ML pipeline as a sequence of matrices being multiplied, reshaped, and decomposed.

*Resource: 3Blue1Brown — search "3Blue1Brown matrices"*

---

## 5. Matrix Multiplication

**Matrix multiplication** combines two matrices by taking dot products between the rows of the first and the columns of the second. The deeper meaning is composition: multiplying two matrices is the same as applying one linear transformation, then another, in sequence. In data science this is the single most computationally important operation in the field — the forward pass of a neural network is just a chain of matrix multiplications followed by activation functions, PCA projects data into a new space via matrix multiplication, and GPUs are essentially built to do this one operation extremely fast. Understanding matrix multiplication as "applying a transformation," rather than a mechanical row-times-column procedure, makes neural network layers and PCA projections click much faster.

*Resource: 3Blue1Brown — search "3Blue1Brown matrix multiplication"*

---

## 6. Systems of Linear Equations

A **system of linear equations** is a set of equations that must all be satisfied simultaneously — geometrically, you're looking for the point(s) where several lines, planes, or hyperplanes intersect. In data science, this is the mathematical backbone of linear regression: when you fit a line (or hyperplane) to data, you're solving — or more often approximately solving, since real data rarely fits exactly — a system of linear equations relating your features to your target variable. Many other algorithms also reduce to solving linear systems internally during optimization. Recognizing "I'm solving a system of linear equations" underneath a regression problem helps explain why things like needing more data points than features actually matter.

*Resource: 3Blue1Brown — search "3Blue1Brown systems of equations"*

---

## 7. Gaussian Elimination

**Gaussian elimination** is the systematic algorithm for solving a system of linear equations: you use row operations (adding, scaling, swapping rows) to reduce a matrix to a simpler triangular form, then solve by back-substitution. It's the "by-hand" method that every solver, inverse calculation, and rank computation builds on under the hood. In data science you'll rarely run it yourself — NumPy and scikit-learn handle it — but understanding it demystifies what `np.linalg.solve()` or a regression's closed-form solution is actually doing internally, and explains *why* certain matrices (singular ones) cause solvers to fail or throw non-invertibility errors.

*Resource: Khan Academy — search "Khan Academy Gaussian Elimination"*

---

## 8. Matrix Inverse

For a square matrix **A**, the **inverse** A⁻¹ is the matrix that "undoes" A, satisfying A·A⁻¹ = I (the identity matrix). If you can find it, solving Ax = b becomes as simple as x = A⁻¹b. In data science, the inverse appears explicitly in the closed-form solution to linear regression — the Normal Equation, β = (XᵀX)⁻¹Xᵀy — which directly gives you the best-fit coefficients. In practice, libraries often avoid computing a literal inverse (it's numerically unstable and slow) and use decompositions like SVD or QR instead — but the inverse is still the concept that explains what those decompositions are ultimately solving for.

*Resource: Khan Academy — search "Khan Academy matrix inverse"*

---

## 9. Determinants

The **determinant** of a square matrix is a single number that tells you two things at once: whether the matrix is invertible (a zero determinant means the transformation "squashes" space into a lower dimension and information is lost), and how much the transformation scales area or volume. In data science, determinants show up when checking whether a covariance matrix is invertible — needed for several statistical formulas, including the multivariate Gaussian density — and a vanishing or near-zero determinant is often a red flag for multicollinearity, meaning your features are too linearly dependent on each other for stable computation.

*Resource: 3Blue1Brown — search "3Blue1Brown determinant"*

---

## 10. Rank

The **rank** of a matrix is the number of linearly independent rows (or columns) it actually has — in other words, the true "dimensionality" of the information it contains, ignoring redundancy. In data science, rank is a diagnostic tool: a feature matrix with rank lower than its number of columns means some features are redundant combinations of others (multicollinearity), which breaks regression assumptions and inflates coefficient variance. Rank is also the core idea behind low-rank approximation — PCA and SVD both work by finding a lower-rank version of your data that keeps most of the important information while discarding noise, which is exactly how matrix-factorization recommender systems compress huge user-item matrices.

*Resource: StatQuest — search "StatQuest Matrix Rank"*

---

## 11. Vector Spaces

A **vector space** is a formal setting — a set of vectors, plus rules for adding and scaling them — that behaves "nicely" enough for all of linear algebra's tools to apply. It sounds abstract, but it's the thing that makes a statement like "your data lives in a 50-dimensional space" precise and meaningful. In data science, every feature space, embedding space (word vectors, image embeddings), and latent space inside a neural network is a vector space. Thinking in terms of vector spaces is what lets you reason about distances, directions, and subspaces in high-dimensional data the same way you'd reason about ordinary 2D or 3D geometry.

*Resource: MIT OpenCourseWare — search "MIT Linear Algebra Vector Spaces Gilbert Strang"*

---

## 12. Span, Basis & Dimension

The **span** of a set of vectors is everything you can reach by combining them (scaling and adding); a **basis** is the smallest set of vectors that spans a space without redundancy; and the **dimension** is simply how many vectors are in that basis. In data science, this trio explains what's really happening in dimensionality reduction: PCA finds a new basis for your data — the principal components — ordered by how much variance each direction captures, and reducing dimensions means keeping only the first few basis vectors of that new span while discarding the rest. Understanding span and basis is what makes "we reduced 100 features down to 10 principal components" a precise, motivated operation rather than a black box.

*Resource: MIT OpenCourseWare — search "MIT Basis Span Dimension Gilbert Strang"*

---

## 13. Linear Independence

A set of vectors is **linearly independent** if none of them can be written as a combination of the others — each one genuinely adds new information or a new direction. The moment one vector becomes a combination of the rest, it's redundant. In data science, this is the formal version of "multicollinearity": when two or more features are nearly linear combinations of each other, your regression coefficients become unstable and hard to interpret, because the model can't tell which of the redundant features deserves the "credit." Checking linear independence — or its near-violation — is a standard early step before trusting a linear model's coefficients.

*Resource: MIT OpenCourseWare — search "MIT Linear Independence Gilbert Strang"*

---

## 14. Orthogonality

Two vectors are **orthogonal** when their dot product is zero — geometrically, they sit at a right angle and share no overlapping direction, meaning they carry completely independent information. In data science, orthogonality is the property that makes many algorithms well-behaved: orthogonal matrices preserve lengths and angles (so transformations built from them don't distort your data), the principal components found by PCA are orthogonal to each other by construction (each captures variance the others don't), and orthogonal or near-orthogonal features make regression coefficients far easier to estimate and interpret reliably.

*Resource: 3Blue1Brown — search "3Blue1Brown orthogonality"*

---

## 15. Projections

**Projecting** one vector onto another (or onto a subspace) means finding the closest point in that subspace — splitting the original vector into a part that lies along the target direction and a leftover part (the error, orthogonal to it). This is, quite literally, what linear regression does: least-squares regression projects your target vector onto the subspace spanned by your features, and the leftover part is the residual error the model couldn't explain. PCA does the same thing in reverse — it projects high-dimensional data onto a smaller subspace (the top principal components) that captures as much of the original variance as possible.

*Resource: 3Blue1Brown — search "3Blue1Brown projection vectors"*

---

## 16. Norms

A **norm** measures the "size" or length of a vector. The most common are the **L2 norm** (ordinary Euclidean length), the **L1 norm** (sum of absolute values — "taxicab" distance), and the L∞ norm (the single largest entry). In data science, norms do constant, often invisible work: the L2 norm defines Euclidean distance used in k-NN and k-means clustering; L1 and L2 norms are the regularization penalties behind Lasso and Ridge regression, which shrink coefficients to fight overfitting (L1 can zero coefficients out entirely, giving automatic feature selection; L2 just shrinks them smoothly); and norms measure error sizes — RMSE, for instance, is built from an L2 norm.

*Resource: StatQuest — search "StatQuest L1 L2 Norm"*

---

## 17. Cosine Similarity

**Cosine similarity** measures how similar two vectors are based purely on the *angle* between them, ignoring magnitude — it's the cosine of that angle, ranging from -1 (opposite) to 1 (identical direction), with 0 meaning unrelated. It's calculated as the dot product divided by the product of the two vectors' norms. In data science, this is the workhorse similarity metric for anything involving embeddings: comparing documents or word vectors in NLP, matching users or items in recommender systems, and measuring similarity in semantic search. It's preferred over plain distance metrics in high-dimensional spaces because it cares about *direction* (meaning/content) rather than raw magnitude, which can just be an artifact of document length or vector scale.

*Resource: StatQuest — search "StatQuest Cosine Similarity"*

---

## 18. Linear Transformations

A **linear transformation** is any function that moves vectors around while preserving addition and scalar multiplication — in practice, this means it can always be represented as multiplication by a matrix. Rotations, scalings, reflections, shears, and projections are all linear transformations. In data science, this reframes a neural network layer for what it really is: before the activation function, every layer is just a linear transformation (a matrix multiply plus a bias shift) applied to the input. Standard preprocessing steps like feature scaling and whitening are also linear transformations. Seeing a model as "a sequence of linear transformations, interrupted by small nonlinear kinks" is one of the clearest ways to understand what deep learning is doing geometrically.

*Resource: 3Blue1Brown — search "3Blue1Brown linear transformations"*

---

## 19. Eigenvalues & Eigenvectors

For a square matrix **A**, an **eigenvector** is a special vector that doesn't change direction when the transformation is applied — it only gets scaled — and the scaling factor is its corresponding **eigenvalue**. These are the "natural axes" of a transformation. In data science, this is the engine behind PCA: the principal components are exactly the eigenvectors of your data's covariance matrix, and the eigenvalues tell you how much variance each component explains, which is why you can rank and discard the less important ones. Eigenvectors also power spectral clustering, Google's original PageRank algorithm, and stability analysis for systems that evolve over time, like recurrent neural networks.

*Resource: 3Blue1Brown — search "3Blue1Brown eigenvectors eigenvalues"*

---

## 20. Positive Definite Matrices

A symmetric matrix is **positive definite** if all of its eigenvalues are positive — equivalently, if xᵀAx > 0 for every nonzero vector x. Geometrically, it behaves like a smooth "bowl" shape rather than a saddle, which guarantees a single, well-defined minimum. In data science this property matters more than it sounds: a valid covariance matrix must be positive semi-definite by construction, and optimization algorithms rely on positive definiteness (e.g., in the Hessian matrix) to guarantee a loss function has one clear minimum rather than a saddle point. It's also the requirement for a function to be a valid kernel in kernel methods like SVMs, and for using the efficient Cholesky decomposition.

*Resource: StatQuest — search "StatQuest Positive Definite Matrix"*

---

## 21. Singular Value Decomposition (SVD)

**SVD** factorizes *any* matrix A, even non-square ones, into three pieces: A = UΣVᵀ, where U and V are orthogonal matrices and Σ is a diagonal matrix of "singular values" ranked by importance. It's effectively a generalization of eigendecomposition that works on any matrix. In data science, SVD is one of the most practically important tools in the field: it's the numerically stable way most libraries actually compute PCA, it powers matrix-factorization recommender systems (this is how the Netflix Prize was largely won — decomposing a giant, sparse user-item matrix into compact user and item factors), and it's used for image compression, noise reduction, and Latent Semantic Analysis in NLP for uncovering hidden topic structure in documents.

*Resource: StatQuest — search "StatQuest Singular Value Decomposition"*

---

## 22. PCA (Principal Component Analysis)

**PCA** ties almost everything above together. It finds a new set of axes — the principal components — ordered so the first captures the most variance in your data, the second captures the most *remaining* variance while staying orthogonal to the first, and so on. Mechanically, those components are the eigenvectors of your data's covariance matrix (or equivalently, computed via SVD for better numerical stability), and projecting your data onto just the first few of them gives you a lower-dimensional version that keeps most of the original information. In data science, PCA is a default tool for dimensionality reduction before modeling, visualizing high-dimensional data in 2D or 3D, removing noise, and easing multicollinearity in regression. If you've understood vectors, projections, eigenvectors, and SVD above, PCA is really just all of them working together.

*Resource: your table cut off before this row — StatQuest's "Principal Component Analysis (PCA), Step-by-Step" fits the same pattern as the rest; search "StatQuest PCA"*
