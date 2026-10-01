# 8. Neural Network Architectures: FNN, RNN, CNN
### Neural Network Architectures: FNN, RNN, CNN

---

## 1. Fully-Connected Feedforward Neural Network (FNN)

- **Definition:** The simplest type. *(Sabse saada qisam.)*
- **"Fully-connected":** Every neuron in one layer is connected to every neuron in the next layer.
  *Ek layer ka har neuron agli layer ke har neuron se connected hota hai.*
- **"Feedforward":** There are no cycles or loops. Information flows in one direction: from input to output.
  *Koi cycles ya loops nahi hotay. Information sirf ek sim mein behti hai: input se output tak.*
- **Layers:** Input, Hidden (one or more), Output.
- **Nonlinearity:** Uses nonlinear activation functions (Sigmoid, Tanh, ReLU) to model complex functions.
- **Trade-off:** More neurons = "wider" network; more hidden layers = "deeper" network. Increasing these increases the complexity and computational resources required.
  *Zyada neurons = "wider" network; zyada hidden layers = "deeper" network. Inhein barhanay se complexity aur zaroori computational resources barh jatay hain.*

---

## 2. Recurrent Neural Network (RNN)

- **Purpose:** Designed to handle **sequential data** (e.g., sentences, time series).
  *Sequential data (misal: sentences, time series) handle karnay ke liye design kiya gaya hai.*
- **The Problem with FNN for Sequences / Sequences ke liye FNN ka Masla:**
    - They cannot model sequential data because they don't "remember" past information.
      *Yeh sequential data model nahi kar saktay kyunke inhein guzashta (past) information "yaad" nahi rehti.*
    - They don't share parameters across time. A feature learned at the beginning of a sequence won't be recognized if it appears at the end.
      *Yeh waqt ke aar-paar parameters share nahi kartay. Sequence ki shuruat mein seekha gaya feature agar akhir mein dobara aaye to pehchana nahi jayega.*
- **The RNN Solution / RNN ka Hal:**
    - They use a **feedback loop** in the hidden layer, acting like a short-term memory.
      *Yeh hidden layer mein ek **feedback loop** istemal kartay hain, jo short-term memory ki tarah kaam karta hai.*
    - They pass information from one step of the sequence to the next.
      *Yeh sequence ke ek step se agle step tak information pass kartay hain.*
    - **Backpropagation Through Time (BPTT):** The algorithm used to train RNNs, where the backpropagation is applied for every sequence data point.
      *RNNs ko train karnay ka algorithm, jahan har sequence data point ke liye backpropagation apply ki jaati hai.*

### Analogy / Misaal:
- **FNN:** I show you a photo of a ball and ask you to predict its position in 2 seconds. You can't.
  *Main aapko ball ki ek tasveer dikhata hoon aur 2 second baad iski position predict karnay ko kehta hoon. Aap nahi kar saktay.*
- **RNN:** I give you a video of the ball's previous positions and ask you to predict its future trajectory. You can.
  *Main aapko ball ki pichli positions ki video deta hoon aur uski future trajectory predict karnay ko kehta hoon. Aap kar saktay hain.*
- **FNN:** I say "dog." You don't understand my intent. *(Main kehta hoon "dog". Aap meri niyyat nahi samajhtay.)*
- **RNN:** I say "I have a dog." Now you understand the context from the whole sentence.
  *Main kehta hoon "I have a dog". Ab aap poore sentence se context samajh jatay hain.*

### Key Issue: Vanishing/Exploding Gradients (Short-Term Memory) / Ahem Masla:
- As the RNN processes more words, it has trouble retaining information from the very beginning.
  *Jaisay jaisay RNN zyada words process karta hai, usay shuru se information yaad rakhnay mein mushkil hoti hai.*
- This leads to the **vanishing gradient problem**, where gradients become exponentially small, causing early layers to stop learning.
  *Isse **vanishing gradient problem** paida hota hai, jahan gradients exponentially chhotay ho jatay hain, jisse early layers seekhna band kar deti hain.*
- **Solutions:** Gated RNNs and LSTMs (Long Short-Term Memory), which use gates to control what information to add or remove from the memory.
  *Gated RNNs aur LSTMs, jo yeh control karnay ke liye gates istemal kartay hain ke memory mein kya add karna hai ya nikalna hai.*

- **Applications:** Natural Language Processing, Sentiment Analysis, Speech Recognition, Translation.

---

## 3. Convolutional Neural Network (CNN)

- **Purpose:** Designed specifically for tasks like **image classification**.
  *Khaas tor par **image classification** jaisay tasks ke liye design kiya gaya hai.*
- **Inspiration:** The organization of neurons in the visual cortex of the animal brain.
  *Janwaron ke dimagh ke visual cortex mein neurons ki tarteeb.*
- **Key Idea:** They use **convolution** and **pooling** instead of traditional matrix multiplication.
  *Yeh traditional matrix multiplication ki bajaye **convolution** aur **pooling** istemal kartay hain.*

### Core Components / Bunyadi Ajza:
1. **Convolutional Layer:**
    - Uses a **filter (kernel)** that moves across the input image.
      *Ek **filter (kernel)** istemal karta hai jo input image par move karta hai.*
    - The filter performs a mathematical operation (dot product) on small regions of the image, extracting features like edges and lines.
      *Filter image ke chhotay regions par ek mathematical operation karta hai, jisse edges aur lines jaisay features nikaltay hain.*
2. **Pooling Layer (Subsampling/Downsampling):**
    - Reduces the number of neurons in subsequent layers.
      *Baad ki layers mein neurons ki tadaad kam karta hai.*
    - **Max Pooling:** Picks the maximum value from a selected region.
    - **Min Pooling:** Picks the minimum value from a selected region.
    - **Goal:** Retain the most important information while reducing complexity.
      *Sabse ahem information rakhtay huay complexity kam karna.*
3. **Fully Connected Layers:** Used at the end to help classify the image.
   *Image classify karnay mein madad ke liye aakhir mein istemal hoti hain.*

### Typical CNN Architecture for Image Classification / Typical CNN Architecture:
1. Input Image (2D matrix of pixels, 3 color channels).
2. Convolutional Layer with multiple filters.
3. Pooling Layer.
4. Repeat Convolution + Pooling multiple times.
5. Flatten the data and add Fully-Connected Layers.
6. Output Layer with a final classification prediction.

- **Applications:** Image Recognition, Image Segmentation, Video Analysis, and Natural Language Processing.
