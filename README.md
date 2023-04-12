# Sign-Detection-using-Machine-Learning

A Simple Python application that will recognize the American Signs and converts into text in realtime. It uses CNN to train the required models for prediction. The dataset is custom made.

---

![ASL[^1] signs]([https://github.com/nagarjun-Avala/Sign-Detection-using-Machine-Learning/sign.png](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FThe-26-letters-and-10-digits-of-American-Sign-Language-ASL_fig1_328396430&psig=AOvVaw3QzdwkYo6Ocjq0FcKCBDvu&ust=1681400253728000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCKiNhpnWpP4CFQAAAAAdAAAAABAE) "ASL[^1] signs")

### Steps

###### 1. Install all the libraries using this command

```bash
pip install -r requirements.txt
```

###### 2. Collecting data

1.  Run collect-data.py
1.  Take 50 photos of the ASL sings you needed

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
