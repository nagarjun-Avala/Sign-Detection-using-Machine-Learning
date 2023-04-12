# Sign-Detection-using-Machine-Learning

A Simple Python application that will recognize the American Signs and converts into text in realtime. It uses CNN to train the required models for prediction. The dataset is custom made.

---

![plot](./sign.png)

### Steps

###### 1. Install all the libraries using this command

```bash
pip install -r requirements.txt
```

###### 2. Collecting data

1.  Run collect-data.py
1.  Take 50 photos of the ASL[^1] sings you needed

###### 3. Pre-Processing

1.  Run preprocessing.py
1.  This will transform all the RGB[^2] images to gray scaled images to improve the model training

###### 4. Training the Model

1.  Run train.py

###### 5. Application

1.  Run app.py and you can show sing to the camera and the model will detect the corresponding Letter

---

### dataset :

- train : We will update soon
- test : We will update soon


[^1]: ASL - American Sign Language
[^2]: RGB - Red Green Blue colors
