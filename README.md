# to create virtual environment
python -m venv bilingual_env

# to activate virtual environment
bilingual_env\Scripts\activate

# to install all dependencies
pip install -r requirements.txt

# to train model
python scripts/train_model.py  

# to start the server
python app.py