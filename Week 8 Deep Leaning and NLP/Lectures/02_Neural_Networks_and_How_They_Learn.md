# 2. Neural Networks and How They Learn
### Neural Networks aur Unka Seekhne ka Amal

---

## Introduction to Neural Networks / Neural Networks ka Ta'aruf

- Neural networks form the basis of deep learning.
  *Neural networks, deep learning ki bunyad hain.*
- Inspired by the structure of the human brain.
  *Insaani dimagh ki structure se inspired hain.*
- The fundamental building block is a **neuron**.
  *Bunyadi building block ek **neuron** hai.*

---

## The 3 Core Components of a Neural Network / Neural Network ke 3 Bunyadi Ajza

1. **Input Layer:** Takes in the initial data.
   *Ibtidai data leti hai.*
2. **Hidden Layers:** Several layers between the input and output where computation happens. The "deep" in deep learning comes from having many hidden layers.
   *Input aur output ke darmiyan kayi layers jahan computation hoti hai. "Deep" learning ka naam isi wajah se hai — bohot saari hidden layers hoti hain.*
3. **Output Layer:** Produces the final prediction (e.g., probability of an image being a cat).
   *Aakhri prediction deti hai (misal: image ke cat honay ki probability).*

---

## The Learning Process: Forward & Back Propagation / Seekhne ka Amal

### 1. Forward Propagation
- Information travels from the input layer to the output layer.
  *Information input layer se output layer ki taraf safar karti hai.*
- **Step-by-step / Marhala ba marhala:**
    - Inputs (`X1...Xn`) are multiplied by associated **weights**.
      *Inputs (X1...Xn) ko unke mutalliqa **weights** se multiply kiya jata hai.*
    - The sum of these products is passed to a neuron in the hidden layer.
      *In products ka majmua (sum) hidden layer ke ek neuron ko diya jata hai.*
    - A **bias** is added to this sum.
      *Is sum mein ek **bias** add kiya jata hai.*
    - The result (weighted sum + bias) is passed through an **activation function**.
      *Natija (weighted sum + bias) ek **activation function** se guzarta hai.*
    - This process repeats until the output layer, which gives a final probability.
      *Yeh amal output layer tak dohraya jata hai, jo aakhri probability deta hai.*

#### Key Terms in Forward Propagation / Ahem Istalahat:
- **Weights:** Tell us how important a neuron's input is. Higher weight = more importance.
  *Batatay hain ke neuron ka input kitna ahem hai. Zyada weight = zyada ahmiyat.*
- **Bias:** Allows the neuron to have an "opinion," shifting the activation function left or right.
  *Neuron ko "apni raye" rakhne deta hai, activation function ko left ya right shift karta hai.*

### 2. Back Propagation (The Magic of Learning) / Seekhne ka Jadu
- Information passes backward from the output layer to the hidden layers.
  *Information output layer se hidden layers ki taraf ulti jaati hai.*
- **Purpose:** To adjust the weights and biases to make the network's predictions more accurate.
  *Maqsad: Weights aur biases ko adjust karna taake network ki predictions zyada sahi hon.*
- **How it works / Kaam Kaisay Karta Hai:**
    1. The network makes a prediction. *(Network ek prediction karta hai.)*
    2. It checks if the prediction is right or wrong. *(Yeh check karta hai ke prediction sahi hai ya ghalat.)*
    3. If wrong, it uses a **Loss Function** to quantify the error. *(Agar ghalat hai to Loss Function error ko measure karta hai.)*
    4. This error information is sent back through the network. *(Yeh error information network mein wapas bheji jaati hai.)*
    5. The weights and biases are adjusted to reduce the error. *(Error kam karnay ke liye weights aur biases adjust kiye jatay hain.)*

---

## Summary of the Learning Algorithm / Learning Algorithm ka Khulasa

1. **Initialize:** Start with random values for weights and biases.
   *Weights aur biases ki random values se shuruat.*
2. **Forward Pass:** Pass a set of input data through the network to get a prediction.
   *Input data ko network se guzar kar prediction hasil karna.*
3. **Calculate Loss:** Compare the prediction with the expected output using a loss function.
   *Prediction ko expected output se loss function ke zariye compare karna.*
4. **Backward Pass:** Perform back propagation to propagate the loss back to all weights and biases.
   *Loss ko sab weights aur biases tak wapas bhejnay ke liye back propagation.*
5. **Update:** Update the weights and biases (using an optimizer like Gradient Descent) to reduce the total loss.
   *Total loss kam karnay ke liye optimizer (misal: Gradient Descent) se weights/biases update karna.*
6. **Iterate:** Repeat steps 2-5 until the model is "good enough."
   *Steps 2-5 ko dohrana jab tak model "achha" na ho jaye.*

---

## Real-World Analogy: Car vs. Truck Classification / Haqeeqi Duniya ki Misaal

- **Data:** Vehicle weight, number of goods, and type (Car/Truck).
  *Gaari ka wazan, saaman ki tadaad, aur type (Car/Truck).*
- **Process / Amal:**
    - Network initializes with random weights/biases. *(Network random weights/biases ke sath shuru hota hai.)*
    - Input (weight=15, goods=2) passes through the network. *(Input network se guzarta hai.)*
    - Network predicts "Truck," but the correct label is "Car." *(Network "Truck" predict karta hai, lekin sahi label "Car" hai.)*
    - Loss function calculates the error. *(Loss function error calculate karta hai.)*
    - Back propagation adjusts the random weights/biases. *(Back propagation random weights/biases ko adjust karta hai.)*
    - The process repeats for all data entries, each time refining the weights. *(Yeh amal tamam data entries ke liye dohraya jata hai, har baar weights ko behtar karte huay.)*
