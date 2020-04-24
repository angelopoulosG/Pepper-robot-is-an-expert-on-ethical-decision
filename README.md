# Pepper robot is an expert on ethical decision 

The aim of this project is to construct an intelligent and integrated system on a Pepper robot that can solve ethical dilemmas and to evaluate the reaction of human observers to the competencies displayed by the robot. The types of dilemmas would be those faced by drivers when facing a choice between two evils. Some of these dilemmas will be inspired by the famous series of the Trolley Problem ethical dilemmas. Some of these would be adjusted to traffic situations and autonomous vehicles. 


[Universitat Pompeu Fabra, Barcelona, Spain.](https://www.upf.edu/)

## System Architecture
<img src="/images/system_architecture.png" width="600">

## Prerequisites 

#### Python 3 (On your computer/server)

With the following libraries installed:

*  SpeechRecognition, a library for performing speech recognition.
```
pip3 install SpeechRecognition
```

*  OpenCV, an open source computer vision software library.
```
pip3 install opencv-python
```

*  SpaCy, a library for advanced Natural Language Processing in Python.
```
pip3 install -U spacy
```

*  Thinc, the machine learning library powering spaCy.
```
pip3 install thinc
```

#### Pepper Robot
Pepper is a semi-humanoid robot manufactured by SoftBank Robotics (formerly Aldebaran Robotics).

## How to run it
* First, download all the code from the folder **Server** to your computer/server.
* Go to **thebrain.py** and change the **line 16** with your IP.
* Finally, Enable the "Brain":

```
python3 thebrain.py
```

* After enabling the server, SSH onto the robot and download all the code from the folder **Pepper**.
* Go to **ethical_pepper.py** and change the **line 16** with your server's IP.
* Finally, Enable Pepper:

```
python ethical_pepper.py
```

## Ethical Dilemmas

An example of an ethical dilemma which Pepper should answer.

<img src="/images/Dilemmas/case_no1.png" width="650">

## Master Student

[**Georgios Angelopoulos**](https://www.linkedin.com/in/george-angelopoulos/)


## Supervisor

[**Prof. Vladimir Estivill-Castro**](https://www.upf.edu/web/etic/entry/-/-/54009/409/vladimir-estivill)

<!--
* spaCy is compatible with 64-bit CPython 2.7 / 3.5+ and runs on Unix/Linux, macOS/OS X and Windows:
```
pip install -U spacy
```

* gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API:
```
pip install gTTS
```

* SpeechRecognition, Library for performing speech recognition, with support for several engines and APIs, online and offline:
```
pip install SpeechRecognition
```

-->
