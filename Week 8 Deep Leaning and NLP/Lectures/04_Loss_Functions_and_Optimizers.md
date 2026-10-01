# 4. Loss Functions and Optimizers
### Loss Functions aur Optimizers

---

## Loss Functions

- A mathematical way to **quantify the deviation** of the predicted output from the expected output.
  *Predicted output aur expected output ke darmiyan **deviation ko quantify** karnay ka mathematical tareeqa.*
- It's the guide that tells the model how wrong it is.
  *Yeh wo rehnuma hai jo model ko batata hai ke wo kitna ghalat hai.*
- **Types / Aqsam:**
    - **Regression:** Mean Squared Error, Absolute Error.
    - **Binary Classification:** Binary Cross-Entropy, Hinge Loss.
    - **Multiclass Classification:** Multiclass Cross-Entropy.
- The choice of loss function depends on the project.
  *Loss function ka intekhab project par depend karta hai.*

---

## Optimizers

- **What they do:** They tie together the loss function and the model parameters (weights and biases).
  *Yeh loss function aur model parameters (weights aur biases) ko aapas mein jorte hain.*
- Their job is to **update the network** in response to the output of the loss function to make the model more accurate.
  *Inka kaam loss function ke output ke jawab mein **network ko update karna** hai taake model zyada accurate ho.*
- They shape and mold the model by adjusting weights and biases. The loss function tells the optimizer whether it's moving in the right direction.
  *Yeh weights aur biases adjust kar ke model ko shape detay hain. Loss function optimizer ko batata hai ke wo sahi sim mein ja raha hai ya nahi.*

### 1. Gradient Descent (The Granddaddy of Optimizers)
- **Analogy:** Imagine descending Mount Everest blindfolded. You take steps and use your feet to gauge if you're going up or down. You (the network) want to go down to minimize the error. Your feet are like the loss function, measuring if you're going the right way.
  *Tasawwur karein ke aap aankhon par patti bandh kar Mount Everest se neechay utar rahay hain. Aap qadam uthatay hain aur apnay paon se andaza lagatay hain ke upar ja rahay hain ya neechay. Aap (network) neechay jana chahtay hain taake error kam ho. Aapke paon loss function ki tarah hain.*
- **How it works / Kaam Kaisay Karta Hai:**
    1. Calculate what a small change in each individual weight would do to the loss function.
       *Har individual weight mein choti si tabdeeli loss function par kya asar dalegi, yeh calculate karna.*
    2. Adjust each weight based on its gradient (take a small step in the determined direction).
       *Har weight ko uske gradient ke mutabiq adjust karna.*
    3. Repeat until the loss function is as low as possible.
       *Jab tak loss function jitna mumkin ho kam na ho jaye, dohrana.*

#### Key Concepts / Ahem Concepts:
- **Gradient:** The vector of partial derivatives. It always points in the direction of the **steepest increase** in the function. To minimize loss, we take the **negative gradient**.
  *Partial derivatives ka vector. Yeh hamesha function ki **sabse tez badhotri** ki sim ki taraf ishara karta hai. Loss minimize karnay ke liye hum **negative gradient** lete hain.*
- **Learning Rate:** A small number (e.g., 0.1) that we multiply the gradients by. It ensures we change our weights at the right pace.
  *Ek chhota number jisay hum gradients se multiply kartay hain. Yeh yaqeeni banata hai ke hum sahi raftar se apni weights badalein.*
    - **Too large:** You might overshoot the optimal value and never converge. *(Bohot bara: Aap optimal value ko overshoot kar saktay hain.)*
    - **Too small:** You might get stuck in a local minimum. *(Bohot chhota: Aap local minimum mein phans saktay hain.)*

### 2. Stochastic Gradient Descent (SGD)
- Instead of using all training examples to calculate the gradient, SGD uses a subset (a batch) or a random example.
  *Gradient calculate karnay ke liye sabhi training examples istemal karnay ki bajaye, SGD ek subset (batch) ya random example istemal karta hai.*
- It's less computationally expensive. *(Yeh computationally kam kharcheela hai.)*
- It uses the concept of **Momentum** (accumulating gradients from past steps) to dictate future steps.
  *Yeh **Momentum** ka concept istemal karta hai (pichlay steps se gradients jama karna) taake aane walay steps tay ho sakein.*

### 3. Other Optimizers / Doosray Optimizers
- **Adagrad:** Adapts the learning rate for each individual feature. Good for sparse data, but learning rate can get very small over time.
  *Har individual feature ke liye learning rate adapt karta hai. Sparse data ke liye achha, magar waqt ke sath learning rate bohot chhota ho sakta hai.*
- **RMSprop:** A version of Adagrad that accumulates gradients in a fixed window.
  *Adagrad ka ek version jo ek fixed window mein gradients jama karta hai.*
- **Adam (Adaptive Moment Estimation):** Uses past gradients to calculate the current gradient and utilizes momentum. It's very popular and widely accepted for training neural networks.
  *Current gradient calculate karnay ke liye pichlay gradients istemal karta hai aur momentum ka faida uthata hai. Neural networks train karnay ke liye bohot popular hai.*

---

## Summary / Khulasa

- **Loss Function:** Measures the error. *(Error ko measure karta hai.)*
- **Optimizer:** Uses the error to update the weights and biases. *(Error ko istemal kar ke weights aur biases update karta hai.)*
- **Goal:** Minimize the loss function through trial and error. *(Trial and error ke zariye loss function ko minimize karna.)*
