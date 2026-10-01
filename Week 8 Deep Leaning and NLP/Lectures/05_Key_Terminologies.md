# 5. Key Terminologies: Parameters, Hyperparameters, Epochs, and Batches
### Ahem Istalahaat: Parameters, Hyperparameters, Epochs, aur Batches

---

## Parameters vs. Hyperparameters

### Model Parameters
- **Definition:** Variables that are **internal** to the neural network and whose values are **estimated from the data**.
  *Wo variables jo neural network ke **andar (internal)** hotay hain aur jinki values **data se estimate** ki jaati hain.*
- They are required by the model to make predictions.
  *Model ko prediction karnay ke liye inki zaroorat hoti hai.*
- When you save a model, you are saving its parameters.
  *Jab aap model save kartay hain, to aap uske parameters save kar rahay hotay hain.*
- **Examples:** Weights and Biases.

### Model Hyperparameters
- **Definition:** Configurations that are **external** to the model and whose values **cannot be estimated from data**.
  *Wo configurations jo model ke **bahar (external)** hain aur jinki values **data se estimate nahi** ki ja saktin.*
- There is no way to know the best value for a hyperparameter for a given problem. You must search for them by trial and error or use rules of thumb.
  *Kisi bhi problem ke liye hyperparameter ki behtareen value pehlay se maloom karnay ka koi tareeqa nahi. Aapko trial and error se inhein dhoondna padta hai.*
- **Rule of Thumb:** If you have to specify a parameter manually, it is probably a hyperparameter.
  *Agar aapko koi parameter manually specify karna parta hai, to wo shayad hyperparameter hai.*
- **Examples:** Learning rate, number of hidden layers, type of activation function.

---

## Epochs, Batches, and Iterations

### The Problem / Masla
- Data is often too big to pass all of it to the computer at once.
  *Data aksar itna bara hota hai ke ek hi baar mein computer ko nahi diya ja sakta.*
- So, we divide the dataset into smaller chunks.
  *Isliye, hum dataset ko chhotay chhotay hisson (chunks) mein taqseem kartay hain.*

### 1. Batch
- A batch is a subset of the training examples used in one pass of forward and backward propagation.
  *Ek batch training examples ka wo subset hai jo forward aur backward propagation ke ek pass mein istemal hota hai.*
- **Batch Size:** The total number of training examples in a single batch.
  *Ek single batch mein training examples ki total tadaad.*
- **Example:** If you have 500 examples in one batch, your batch size is 500.
  *Agar aapke pas ek batch mein 500 examples hain, to aapka batch size 500 hai.*

### 2. Iteration
- **Definition:** The number of batches needed to complete **one epoch**.
  *Ek **epoch** poora karnay ke liye zaroori batches ki tadaad.*
- For one epoch, the number of batches = the number of iterations.
  *Ek epoch ke liye, batches ki tadaad = iterations ki tadaad.*

### 3. Epoch
- **Definition:** One complete pass of the **entire training dataset** forward and backward through the network.
  *Poore training dataset ka network se forward aur backward ek mukammal pass.*
- In most deep learning models, we use more than one epoch.
  *Aksar deep learning models mein hum ek se zyada epochs istemal kartay hain.*
- **Analogy:** Learning a song by its lyrics. You need to read the lyrics multiple times (epochs) before you can memorize it.
  *Kisi gaanay ke lyrics yaad karna. Yaad karnay se pehlay aapko lyrics ko kayi baar (epochs) parhna hoga.*
- **Too Many Epochs:** Leads to **overfitting**, where the model memorizes the training data and performs poorly on new data.
  *Bohot Zyada Epochs: **Overfitting** ki taraf le jatay hain, jahan model training data yaad kar leta hai aur naye data par kharab performance deta hai.*
- There is **no "right" number** of epochs. It depends on the dataset and the model.
  *Epochs ki koi "sahi" tadaad **nahi hoti**. Yeh dataset aur model par depend karta hai.*

### Example / Misaal
- **Dataset Size:** 34,000 examples.
- **Batch Size:** 500 examples.
- **Iterations per Epoch:** `34,000 / 500 = 68 iterations`.
- This means it will take 68 iterations to complete one epoch.
  *Iska matlab hai ke ek epoch poora karnay mein 68 iterations lagengay.*

---

## A Note on Making Choices / Faislay Karnay Ke Baaray Mein Note

> There are no clear-cut guidelines for choices like the number of hidden layers or which activation function to use. **Experimentation is key.** Try different combinations and see what works best for your project. This is part of the learning process.
>
> *Hidden layers ki tadaad ya konsa activation function istemal karna hai jaisay faislon ke liye koi wazeh guidelines nahi hain. Experimentation kunji (key) hai. Mukhtalif combinations try karein aur dekhein apnay project ke liye kya behtareen kaam karta hai.*
