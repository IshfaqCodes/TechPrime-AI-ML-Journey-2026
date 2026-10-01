# 6. Types of Learning: Supervised, Unsupervised, Reinforcement
### Seekhne ki Aqsam: Supervised, Unsupervised, Reinforcement

---

## 1. Supervised Learning

- **Definition:** The most common subbranch of ML. The model learns by example from **well-labeled data**.
  *ML ki sabse mash'hoor subbranch. Model **acchi tarah labeled data** se misalon ke zariye seekhta hai.*
- **Analogy:** A human supervising the training process, providing the correct answers.
  *Ek insaan training process ki nigrani (supervise) kar raha hai, sahi jawabaat farahem kar raha hai.*
- **Process / Amal:**
    - Each example is a pair: an input object (e.g., image) and a desired output value (e.g., label "cat").
      *Har misaal ek jorra hai: ek input object aur ek matlooba output value.*
    - The algorithm searches for patterns in the data that correlate with the desired outputs.
      *Algorithm data mein aisay patterns dhoondta hai jo matlooba outputs se mutabiqat rakhtay hon.*
    - After training, it can take new inputs and determine the correct label.
      *Training ke baad, yeh naye inputs le kar sahi label muta'yyan kar sakta hai.*
- **Objective:** To predict the correct label for newly presented input data.
  *Naye pesh kardah input data ke liye sahi label predict karna.*
- **Equation:** `y = f(x)`, where `y` is the predicted output and `f` is a mapping function created by the model.

### Subcategories:
1. **Classification:** Assigns input data to a class or category. (e.g., Spam vs. Not Spam, MNIST digit recognition).
   *Input data ko ek class ya category assign karta hai.*
2. **Regression:** Predicts a continuous number. (e.g., Sales, Income, House Prices).
   *Ek continuous number predict karta hai.*

- **Popular Algorithms:** Linear Classifiers, SVMs, Decision Trees, K-Nearest Neighbors, Random Forest.
- **Applications:** Spam detection, speech recognition, face recognition.

---

## 2. Unsupervised Learning

- **Definition:** Used to manifest underlying patterns in data without using labeled data.
  *Labeled data istemal kiye baghair data mein maujood patterns ko zahir karnay ke liye istemal hota hai.*
- **Goal:** To analyze data and find important features, subgroups, or hidden patterns that a human observer might not pick up on.
  *Data ko analyze karna aur ahem features, subgroups, ya hidden patterns dhoondna jo shayad insaan na pehchan sakay.*

### Subcategories:
1. **Clustering:** The process of grouping given data into different clusters.
   *Diye gaye data ko mukhtalif clusters mein group karnay ka amal.*
   - **Goal:** Data in the same cluster are as similar as possible; data in different clusters are as dissimilar as possible.
     *Aik hi cluster ka data jitna mumkin ho ek doosray se milta julta ho; mukhtalif clusters ka data jitna mumkin ho mukhtalif ho.*
   - **Types:** Partitional (each data point belongs to only one cluster) and Hierarchical (data points can belong to multiple clusters).
   - **Algorithms:** K-means, Expectation Maximization, HCA.

2. **Association:** Finds relationships between different entities.
   *Mukhtalif entities ke darmiyan relationships dhoondta hai.*
   - **Classic Example:** **Market Basket Analysis.** Finding that people who buy potatoes and burgers often buy beer.
     *Yeh dhoondna ke jo log aloo aur burger khareedtay hain, wo aksar beer bhi khareedtay hain.*

- **Applications:** Airbnb (recommending stays based on a user's query), Amazon (recommending frequently bought-together products), Credit Card Fraud Detection (detecting unusual patterns).

---

## 3. Reinforcement Learning

- **Definition:** An agent learns in an interactive environment by **trial and error**.
  *Ek agent interactive environment mein **trial and error** se seekhta hai.*
- **Feedback:** Uses **rewards** (for positive behavior) and **punishments** (for negative behavior) as signals.
  *Signals ke tor par **rewards** aur **punishments** istemal karta hai.*
- **Goal:** To find a suitable action model that would maximize the total cumulative reward of the agent.
  *Aisa action model dhoondna jo agent ke total cumulative reward ko maximize karay.*

### Key Terms / Ahem Istalahaat:
- **Environment:** The physical world in which the agent operates. *(Wo physical duniya jismein agent kaam karta hai.)*
- **State:** The current situation of the agent. *(Agent ki current situation.)*
- **Reward:** Feedback received from the environment. *(Environment se milnay wala feedback.)*
- **Policy:** The method to map the agent's state to its actions. *(Agent ki state ko uske actions se map karnay ka tareeqa.)*
- **Value:** The future reward an agent will receive by taking an action in a particular state.
  *Wo future reward jo agent kisi khaas state mein koi action lay kar hasil karega.*

### Example (Pac-Man) / Misaal:
- **Agent:** Pac-Man.
- **Environment:** The grid world. *(Grid world.)*
- **Reward:** Eating food. *(Khana khana.)*
- **Punishment:** Getting killed by a ghost. *(Ghost se maara jana.)*
- **State:** Pac-Man's location in the grid. *(Pac-Man ki grid mein location.)*
- **Goal:** Win the game (maximize cumulative reward). *(Game jeetna.)*

- **Applications:** Robotics, Business Strategy Planning, Traffic Light Control.
