# 9. The 5 Steps to Every Deep Learning Model
### Deep Learning Model ke 5 Zaroori Qadam

---

## Step 1: Gathering Data / Data Jama Karna

- **Core Idea:** Your model is only as powerful as the data you bring. "Bad data implies a bad model."
  *Aapka model utna hi powerful hai jitna aapka data. "Kharab data ka matlab kharab model."*
- **Data Size:** Depends on the problem.
    - Small: Iris dataset (150 images).
    - Huge: Google Translate (trillions of data points).
- **Rule of Thumb:** The amount of data needed should be 10 times the number of parameters in the model. (This varies!)
  *Zaroori data ki miqdar model ke parameters ki tadaad se 10 guna honi chahiye.*
    - Regression: ~10 examples per predictor variable.
    - Image Classification: Minimum 1000 images per class.
- **Data Quality:** Matters as much as quantity.
  *Data ki Quality utni hi ahem hai jitni quantity.*
    - **Reliability:** Trust in the data. Are labels correct? Is the data noisy?
- **Where to Find Data / Data Kahan Se Milay:**
    - UCI Machine Learning Repository.
    - Kaggle.
    - Google Dataset Search.
    - Reddit (r/datasets).
    - Create your own using web scrapers like Beautiful Soup.

---

## Step 2: Preprocessing the Data / Data Preprocess Karna

1. **Data Splitting:** Usually split into three parts:
    - **Training Set:** Used to train the model. *(Model ko train karnay ke liye istemal hota hai.)*
    - **Validation Set:** Used to evaluate the model during tuning and hyperparameter optimization. (Provides feedback to prevent overfitting).
      *Tuning aur hyperparameter optimization ke doran model evaluate karnay ke liye istemal hota hai.*
    - **Test Set:** Used only once at the very end to test the final, optimized model.
      *Sirf aakhir mein, final optimized model test karnay ke liye ek baar istemal hota hai.*
    - **Why not just Training + Test?** Because tuning hyperparameters based on the test set is a form of learning. The test set must be completely unseen to give a true performance metric.
      *Kyunke test set ke bunyad par hyperparameters tune karna bhi ek qisam ki learning hai. Sahi performance metric denay ke liye test set ka bilkul andekha hona zaroori hai.*
    - **Cross-Validation:** A technique where you create multiple splits of training and validation sets within your training data. K-Fold Cross-Validation is popular.

2. **Formatting:** Ensuring data is in a compatible format (e.g., CSV, JSON).
   *Yaqeeni banana ke data compatible format mein hai.*

3. **Dealing with Missing Data / Missing Data se Nimatna:**
    - **Problem:** Most algorithms can't handle missing values (NaN, null).
      *Aksar algorithms missing values handle nahi kar saktay.*
    - **Solutions / Hal:**
        - Eliminate the samples or features with missing values (risk of losing information).
          *Missing values wale samples ya features ko khatam karna (information khonay ka khatra).*
        - Impute the missing values (e.g., replace with the mean value).
          *Missing values ko impute karna (misal: mean value se replace karna).*

4. **Data Imbalance:**
    - **Problem:** When a classification problem has skewed class proportions (e.g., 90% "spam" and 10% "not spam"). The model will be biased toward the majority class.
      *Jab classification problem mein classes ka tanasub tirchha ho. Model majority class ki taraf biased ho jayega.*
    - **Solution:** Downsampling and Upweighing.
        - **Downsampling:** Reduce the number of examples in the majority class.
          *Majority class mein examples ki tadaad kam karna.*
        - **Upweighing:** Assign a higher weight to the downsampled class to compensate, ensuring the model is still calibrated.
          *Downsampled class ko zyada weight dena taake compensate ho sakay.*

5. **Feature Scaling:**
    - **Problem:** Deep learning algorithms perform better when features are on the same scale.
      *Deep learning algorithms behtar kaam kartay hain jab features aik hi scale par hon.*
    - **Normalization:** Rescaling features to a range between 0 and 1 (MinMax Scaling).
    - **Standardization:** Centering the field at mean zero with standard deviation one (standard normal distribution).

---

## Step 3: Training Your Model / Apna Model Train Karna

- Feed the preprocessed data into the network. *(Preprocessed data ko network mein feed karein.)*
- The network performs forward propagation. *(Network forward propagation perform karta hai.)*
- The loss is compared against the expected output. *(Loss ko expected output se compare kiya jata hai.)*
- Backpropagation is used to adjust the weights and biases. *(Backpropagation weights aur biases adjust karnay ke liye istemal hoti hai.)*
- This process repeats for the specified number of epochs. *(Yeh amal specified tadaad ke epochs ke liye dohraya jata hai.)*

---

## Step 4: Evaluating Your Model / Apna Model Evaluate Karna

- Test the trained model's performance using the **validation set**.
  *Validation set istemal kar ke trained model ki performance test karein.*
- This data is "unseen" to the model and represents how the model will perform in the real world.
  *Yeh data model ke liye "andekha" hai aur yeh zahir karta hai ke model haqeeqi duniya mein kaisa perform karega.*
- If the model performs well on validation data but not on training, it might be overfitting.
  *Agar model validation data par achha lekin training par kharab perform kare, to yeh overfitting ho sakti hai.*

---

## Step 5: Optimizing Your Model's Accuracy / Model ki Accuracy Optimize Karna

- After evaluation, there's a high chance the model can be optimized further.
  *Evaluation ke baad, is baat ka bohot imkan hai ke model ko aur behtar banaya ja sakay.*

### Common Optimization Techniques / Aam Optimization Techniques:
1. **Tuning Hyperparameters:**
    - Increase the number of epochs. *(Epochs ki tadaad barhana.)*
    - Adjust the learning rate. *(Learning rate adjust karna.)*
    - Change the batch size. *(Batch size change karna.)*
    - *Note:* This is an experimental process. There is no single "best" combination.
      *Yeh ek experimental amal hai. Koi single "behtareen" combination nahi hota.*

2. **Addressing Overfitting (Using the techniques from the previous chapter):**
    - Get more data. *(Zyada data hasil karein.)*
    - Use Data Augmentation.
    - Apply Weight Regularization (L1 & L2).
    - Use Dropout.

3. **Addressing Underfitting:**
    - Increase the model's capacity (e.g., add more neurons or layers).
      *Model ki capacity barhayein (misal: zyada neurons ya layers).*
    - Train for more epochs. *(Zyada epochs ke liye train karein.)*

### Key Takeaway for Optimization / Optimization Ke Liye Ahem Baat

> Finding the right balance between underfitting and overfitting is an art. The process is experimental. You will develop a good intuition for it the more models you build.
>
> *Underfitting aur overfitting ke darmiyan sahi balance dhoondna ek fun (art) hai. Yeh amal experimental hai. Jitnay zyada models banayen gay, utni hi behtar intuition develop hogi.*
