# Development-of-bhojpuri-chatbot

intent.json ::: training data
nltk_utils  ::: for tokenization,stemming,bags of words
train.py    ::: for traing the data
model.py    ::: model for training data
chat.py     ::: GUI for interacting with chatbot



#For running chatbot
step-1: we need to install python interpreter in your local machine.

step-2:create a local environment with pytorch 
  
  # Run a command 
  python3 -m venv envirn
  envirn\scripts\activate
  pip install --upgrade pip
  
step-3: install pytorch 
  #Run a command
   pip install pytorch
   
step-4: install nltk,numpy for tokenization,stemming,bags of words   

  #Run a command
   pip install nltk
   pip install numpy
      
 step-5: train your model on training dataset 
  
   #Run a command 
     python train.py
   
 step-6: After training run chat.py for interacting with chatbot
 
  #Run a command 
  python chat.py
  
