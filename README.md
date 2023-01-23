# Choosing the right experts for Biomedical QA Tasks

## Dataset
- Download the zipped datsets folder from [here](https://drive.google.com/file/d/1RvHVvznuin_egAMgWmtfv8klJJfTwVRH/view?usp=share_link)
- Uncompress the folder at the root of the project directory
- Make sure 'datasets' folder is at the root of the project directory

## Setup
### Create a python environment
- Setup environment with `pip install -r requirements.txt`.

## Run DistilBERT
```
python train.py --run-name baseline_distilbert --model-type distilbert
```

## Run BioBERT
```
python train.py --run-name baseline_distilbert --model-type biobert
```

## Train MoE
```
python train.py --run-name baseline_distilbert --model-type moe
```
MoE is set to 4 expert but it can be changed using the following command:
```
python train.py --run-name baseline_distilbert --model-type moe --num_experts 6
```