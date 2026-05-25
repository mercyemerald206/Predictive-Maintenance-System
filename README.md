# Predictive Maintenance

## Run
pip install -r requirements.txt

python pipelines/preprocess.py
python pipelines/train.py

uvicorn api.main:app --reload
