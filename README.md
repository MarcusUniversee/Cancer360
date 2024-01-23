# Cancer360°

### Calhacks 10.0 Prize Winner: Hack on AI and Best use of Reflex

## 💥 - How it all started

Cancer is a disease that has affected our team quite directly. All of our team members know a relative or loved one that has endured or lost their life due to cancer. This makes us incredibly passionate about wanting to improve cancer patient care. We identi fied a common thread of roadblocks that our loved ones went through during their journey through their diagnosis/treatment/etc:

- **Diagnosis and Staging:** Properly diagnosing the type and stage of cancer is essential for determining the most appropriate treatment plan.
- **Treatment Options:** There are many different types of cancer, and treatment options can vary widely. Selecting the most effective and appropriate treatment for an individual patient can be challenging.
- **Multidisciplinary Care:** Coordinating care among various healthcare professionals, including oncologists, surgeons, radiologists, nurses, and others, can be complex but is necessary for comprehensive cancer care.
- **Communication:** Effective communication among patients, their families, and healthcare providers is crucial for making informed decisions and ensuring the patient's needs and preferences are met.

## 📖 - What it does

We built Cancer360° to create a novel, multimodal approach towards detecting and predicting lung cancer. We synthesized four modes of data qualitative (think demographics, patient history), image (of lung CT scans), text (collected by an interactive chatbot), and physicical (via the ZeppOS Smartwatch) with deep learning frameworks and large language models to copmute a holistic metric for patient likelihood of lung cancer. Through this data-driven approach, we aim to address what we view as "The BFSR": The 'Big Four' of Surmountable Roadblocks:

- **Diagnosis:** Our diagnosis system is truly multimodal through our 4 modes: quantitative (uses risk factors, family history, demographics), qualitative (analysis of medical records like CT Scans), physical measurements (through our Zepp OS App), and our AI Nurse.
- **Treatment Options:** Our nurse can suggest multiple roadmaps of treatment options that patients could consider. For accessibility and ease of understanding, we created an equivalent to Google's featured snippets when our nurse mentions treatment options or types of treatment.
- **Multidisciplinary Care:** The way Cancer360° has been built is to be a digital aid that bridges the gaps with the automated and manual aspects of cancer treatment. Our system prompts patients to enter relevant information for our nurse to analyze and distribute what's important to healthcare professionals.
- **Communication:** This is a major need for patients and families in the road to recovery. Cancer360's AI nurse accomplishes this through our emotionally-sensitive responses and clear/instant communication with patients that input their information, vitals, and symptoms.

## 🔧 - How we built it

To build our Quantitative Mode, we used the following:

- **numpy**: for general math and numpy.array
- **Pandas**: for data processing, storage
- **SKLearn**: for machine learning (train_test_split, classification_report)
- **XGBoost**: Extreme Boosting Trees Decision Trees

To build our Qualitative Mode, we used the following:

- **OpenCV** and **PIL** (Python Imaging Library): For Working With Image Data
- **MatPlotLib** and **Seaborn** : For Scientific Plotting
- **Keras**: Image Data Augmentation (think rotating and zooming in), Model Optimizations (Reduce Learning Rate On Plateau)
- **Tensorflow**: For the Convolutional Neural Network (CNN)

To build our AI Nurse, we used the following:

- **Together.ai:** We built our chatbot with the Llama2 LLM API and used tree of thought prompt engineering to optimize our query responses

To build the portal, we used the following:

- **Reflex:** We utilized the Reflex platform to build our entire frontend and backend, along with all interactive elements. We utilized front end components such as forms, buttons, progress bars, and more. More importantly, Reflex enabled us to directly integrate python-native applications like machine learning models from our quantitative and qualitative modes or our AI Nurse directly into the backend.

## 📒 - The Efficacy of our Models

**With Quantitative/Tabular Data:**

We collected quantitative data for patient demographic, risk factors, and history (in the form of text, numbers, and binary (boolean values)). We used a simple keyword search algorithm to identify risk keywords like “Smoking” and “Wheezing” to transform the text into quantitative data. Then we aggregated all data into a single Pandas dataframe and applied one-hot-encoding on categorical variables like gender. We then used SKLearn to create a 80-20 test split, and tested various models via the SKLearn library, including Logistic Regression, Random Forest, SVM, and K Nearest Neighbors. We found that ultimately, XGBoost performed best with the highest 98.39% accuracy within a reasonable 16-hour timeframe. Our training dataset was used in a research paper and can be accessed [here.](https://www.kaggle.com/datasets/nancyalaswad90/lung-cancer) This high accuracy speaks to the reliability of our model. However, it's essential to remain vigilant against overfitting and conduct thorough validation to ensure its generalizability, a testament to our commitment to both performance and robustness.

[View our classification report here](https://imgur.com/a/YAvXwyk)

**With Image Data:**
Our solution is well-equipped to handle complex medical imaging tasks. Using data from the Iraq-Oncology Teaching Hospital/National Center for Cancer Diseases (IQ-OTH/NCCD) lung cancer dataset, and deep learning frameworks from tensorflow and keras, we were able to build a convolution neural network to classify patient CT scans as malignant or benign. Our convolutional neural network was fine-tuned for binary image classification of 512x512 RGB images, with multiple convolutional, max-pooling, normalization, and dense layers, compiled using the Adam optimizer and binary crossentropy loss. We also used OpenCV, PIL, Matplotlib, and Numpy to deliver a commendable 93% accuracy over a 20-hour timeframe. The utilization of dedicated hardware resources, such as Intel developer cloud with TensorFlow GPU, accelerates processing by 24 times compared to standard hardware. While this signifies our technological edge, it's important to acknowledge that image classification accuracy can vary based on data quality and diversity, making the 93% accuracy an achievement that underscores our commitment to delivering high-quality results.

[Malignant CT Scan](https://imgur.com/a/8oGYz71)

[Benign CT Scan](https://imgur.com/a/3X3zb7k)

**AI Nurse:**
The AI Nurse powered by Together.ai and LLMs (such as Llama2) introduces an innovative approach to patient interaction and risk factor determination. Generating "trees of thoughts" showcases our ability to harness large language models for effective communication. Combining multiple AI models to determine risk factor percentages for lung cancer demonstrates our holistic approach to healthcare support. However, it's essential to acknowledge that the efficacy of this solution is contingent on the quality of language understanding, data processing, and the integration of AI models, reflecting our dedication to continuous improvement and fine-tuning.

## 🚩 - Challenges we ran into

- Challenges we fixed:
- Loading our neural network model into the Reflex backend. After using keras to save the model as a “.h5” extension, we were able to load and run the model locally on my jupyter notebook, however when we tried to load it in the Reflex backend, we kept getting a strange Adam optimizer build error. we tried everything: saving the model weights separately, using different file extensions like .keras, and even saving the model on as a .json file. Eventually, we realized that this was a [known issue with m1/m2 macs and tensorflow](https://github.com/tensorflow/tensorflow/issues/61915)
- Fixed the Get Started Button in Reflex header (Issue: button wouldn’t scale to match the text length) - Moved the button outside the inner hstack, but still the outer hstack
- Integrating together ai chatbot model into Reflex: A lot of our time was spent trying to get the integration working.
- Challenges we didn’t fix:
  - Left aligning the AI response and right aligning the user input in the chatbot
  - Fine tuning a second model to predict lung cancer rate from the chatbot responses from the first model - Could not get enough training data, too computationally taxing and few shot learning did not produce results
  - Fixing bugs related to running a virtual javascript environment within Python via PyV8

## 🏆 - Accomplishments that we're proud of

- Going from idea generation to working prototype, with integration of 4 data modalities - Qualitative Mode, Quantitative Mode, and our AI Nurse, and Smartwatch Data, within the span of less than two days
- Integrating machine learning models and large language models within our application in a way that is directly accessible to users
- Learning a completely new web development framework (Reflex) from scratch without extensive documentation and ChatGPT knowledge
- Working seamlessly as a team and take advantage of the component-centered nature of Reflex to work independently and together

## 📝 - What we learned

- Ameya: "I was fortunate enough to learn a lot about frameworks like Reflex and Together.ai."
- Marcus: "Using Reflex and learning its components to integrate backend and frontend seamlessly."
- Timothy: "I realized how I could leverage Reflex, Intel Developer Cloud, Together.ai, and Zepp Health to empower me in developing with cutting edge technologies like LLMs and deep learning models."
- Alex: "I learned a lot of front end development skills with Reflex that I otherwise wouldn’t have learned as a primarily back-end person."

## ✈️ - What's next for Cancer360°

Just like how a great trip has a great itinenary, we envision Cancer360° future plans in phases.

#### Phase 1: Solidifying our Roots

Phase 1 involves the following goals:

- Revamping our user interface to be more in-line with our mockups
- Increasing connectivity with healthcare professionals

#### Phase 2: Branching Out

View the gallery to see this. Phase 2 involves the following goals:

- Creating a mobile app for iOS and Android of this service
- Furthering development of our models to detect and analyze other types of cancers and create branches of approaches depending on the cancer
- Completing our integration of the physical tracker on Zepp OS

#### Phase 3: Big Leagues

Phase 3 involves the following goals:

- Expanding accessibility of the app through having our services be available in numerous different languages
- Working with healthcare institutions to further improve the usability of the suite

## 📋 - Evaluator's Guide to Cancer360°

##### Intended for judges, however the viewing public is welcome to take a look.

Hey! We wanted to make this guide in order to help provide you further information on our implementations of certain programs and provide a more in-depth look to cater to both the viewing audience and evaluators like yourself.

#### Sponsor Services We Have Used This Hackathon

##### Reflex

The founders (Nikhil and Alex) were not only eager to assist but also highly receptive to our feedback, contributing significantly to our project's success.

In our project, we made extensive use of Reflex for various aspects:

- **Project Organization and Hosting:** We hosted our website on Reflex, utilizing their component-state filesystem for seamless project organization.
- **Frontend:** We relied on Reflex components to render everything visible on our website, encompassing graphics, buttons, forms, and more.
- **Backend:** Reflex states played a crucial role in our project by facilitating data storage and manipulation across our components. In this backend implementation, we seamlessly integrated our website features, including the chatbot, machine learning model, Zepp integration, and X-ray scan model.

##### Together AI

In our project, Together AI played a pivotal role in enhancing various aspects:

- **Cloud Service:** We harnessed the robust capabilities of Together AI's cloud services to host, run, and fine-tune llama 2, a Large Language Model developed by META, featuring an impressive 70 billion parameters. To ensure seamless testing, we evaluated more than ten different chat and language models from various companies. This was made possible thanks to Together AI's commitment to hosting over 30 models on a single platform.

- **Integration:** We seamlessly integrated Together AI's feature set into our web app, combined with Reflex, to deliver a cohesive user experience.

- **Tuning:** Leveraging Together AI's user-friendly hyperparameter control and prompt engineering, we optimized our AI nurse model for peak performance. As a result, our AI nurse consistently generated the desired outputs at an accelerated rate, surpassing default performance levels, all without the need for extensive tuning or prompt engineering.

##### Intel Developer Cloud

Our project would not have been possible without the massive computing power of Intel cloud computers. For reference, [here is the CNN training time on my local computer.](https://imgur.com/a/rfYlVro)

And here is the [CNN training time on my Intel® Xeon 4th Gen ® Scalable processor virtual compute environment and tensorflow GPU.](https://imgur.com/a/h3ctSPY)

A remarkable 20x Speedup! This huge leap in compute speed empowered by Intel® cloud computing enabled us to re-train our models with lightning speed as we worked to debugg and worked to integrate it into our backend. It also made fine-tuning our model much easier as we can tweak the hyperparameters and see their effects on model performance within the span of minutes.

##### Zepp Health

We utilized the ZeppOS API to query real-time user data for calories burned, fat burned, blood oxygen, and PAI (Personal Activity Index). We worked set up a PyV8 virtual javascript environment to run javascript code within Python to integrate the ZeppOS API into our application. Using collected data from the API, we used an ensemble algorithm to compute a health metric evaluating patient health, which ultimately feeds into our algorithm to find patient risk for lung cancer.

##### GitHub

We used GitHub for our project by creating a GitHub repository to host our hackathon project's code. We also ensured that our use of GitHub stood out with a detailed ReadMe page, meaningful pull requests, and a collaboration history, showcasing our dedication to improving cancer patient care through Cancer360°. We leveraged GitHub not only for code hosting but also as a platform to collaborate, push code, and receive feedback.

##### .Tech Domains

We harnessed the potential of a .tech domain to visually embody our vision for Cancer360°, taking a step beyond traditional domains. By registering the website helpingcancerpatientswith.tech, we not only conveyed our commitment to innovative technology but also made a memorable online statement that reflects our dedication to improving the lives of cancer patients.
