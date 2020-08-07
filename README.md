# Pepper robot is an expert on ethical decision 

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4a2876b3a8cd47f4b15ab0cc5c4f4e4d)](https://app.codacy.com/manual/angelopoulosG/Pepper-robot-is-an-expert-on-ethical-decision?utm_source=github.com&utm_medium=referral&utm_content=angelopoulosG/Pepper-robot-is-an-expert-on-ethical-decision&utm_campaign=Badge_Grade_Dashboard)

The aim of this project is to construct an intelligent and integrated system on a Pepper robot that can solve ethical dilemmas and to evaluate the reaction of human observers to the competencies displayed by the robot. The types of dilemmas would be those faced by drivers when facing a choice between two evils. Some of these dilemmas will be inspired by the famous series of the Trolley Problem ethical dilemmas. Some of these would be adjusted to traffic situations and autonomous vehicles. 

[Universitat Pompeu Fabra, Barcelona, Spain.](https://www.upf.edu/)

## System Architecture
<img src="/images/system_architecture.png" width="600">

## Prerequisites 

### Python 3 (On your computer/server)

With the following libraries installed:

*   SpeechRecognition, a library for performing speech recognition.

```console
pip3 install SpeechRecognition
```

*   OpenCV, an open source computer vision software library.

```console
pip3 install opencv-python
```

*   SpaCy, a library for advanced Natural Language Processing in Python.

```console
pip3 install -U spacy
```

*   en_core_web_sm, English multi-task CNN trained on OntoNotes. 

```console
python3 -m spacy download en_core_web_sm
```

*   Thinc, the machine learning library powering spaCy.

```console
pip3 install thinc
```

*   console-menu, a simple Python menu-based UI system for terminal applications.

```console
pip3 install console-menu
```

*   pandas, a Python package that provides fast, flexible, and expressive data structures designed to make working with structured and time series data both easy and intuitive. 

```console
pip3 install pandas
```
*   scikit-learn, a Python module for machine learning built on top of SciPy and is distributed under the 3-Clause BSD license. 

```console
pip3 install -U scikit-learn
```

### Pepper Robot
Pepper is a semi-humanoid robot manufactured by SoftBank Robotics (formerly Aldebaran Robotics).

## How to run it
*   First, download all the code from the folder **Server** to your computer/server.
*   Finally, Enable the "Brain":

```console
python3 thebrain.py
```

*   After enabling the server, SSH onto the robot and download all the code from the folder **Pepper**.
*   Finally, Enable Pepper:

```console
python ethical_pepper.py
```

## Ethical Dilemmas

An example of an ethical dilemma which Pepper should answer.

<img src="/images/Dilemmas/case_no1.png" width="650">

## Master Student

[**Georgios Angelopoulos**](https://www.linkedin.com/in/george-angelopoulos/)

## Supervisor

[**Prof. Vladimir Estivill-Castro**](https://www.upf.edu/web/etic/entry/-/-/54009/409/vladimir-estivill)
