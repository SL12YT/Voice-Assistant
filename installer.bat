echo off
pip install pypiwin32
pip install pywin32
pip install pyttsx3
pip install fuzzywuzzy
pip install python-Levenshtein
pip install speechrecognition
pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
pip install PyAudio-0.2.11-cp37-cp37m-win32.whl
xcopy /y /e pyowm %appdata%\Python\Python37\site-packages\
