# Text Detector 

## Description
Aim of this project is to develop a graphical user interface for text detection and text based application. I have used pyqt5 framework for developing a GUI. For the text detection from image, I have used pytesseract module for python. With the help of openCV module, image crop, cropped image visualization and bounding box over the detected word and character has been done. Moreover, Detected the paragraph in the image can be summarized using simple Natural Language Processing (NLP) algorithm. For implementing the NLP algo, I have used spaCy(an open source software library for advanced NLP) is used.
## Installation

### On Ubuntu

1. Set your python 3 as default if not.

    ```text
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
    sudo update-alternatives --config python
    ```

2. git clone https://gitlab.com/pprasathpp/text-detector.git
3. pip install virtualenv
4. enter command : virtualenv your_choice_env
5. source yout_choice_env/bin/activate
6. Check that you have a clean virtual environment

    ```text
    pip freeze
    ```

    you should get a empty line  if not check that your PYTHONPATH empty is, if not enter in your terminal PYTHONPATH="" and put the same command at the end of your .bashrc
7. python -m spacy download en_core_web_sm
8. pip install -r Requirements.txt
9. DONE  :blush:

## Usage

python3 textDetect.py

## samples
![Detection google image_2](/samples/sample_1.gif)


## Current work
1. Detection of text
2. Bounding box over words & box coordinates
3. Bounding box over each characters & box coordinates
4. Summarizing the text with NLP
5. Interested region of text selection with box and detecting text
