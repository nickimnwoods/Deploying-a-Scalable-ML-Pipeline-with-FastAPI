# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model was created by Nicki Woods for the purpose of a Udacity Machine Learning Dev-Ops project. This represents version 1 of this model, September 2026. The model used is the Random Forest model and the hyperparameters used are n_estimators = 100, max_depth = 5 and random_state = 55.

## Intended Use
The intended use of this model is to predict whether an individual's income exceeds 50k per year based on census data. The intended use of this model is to be a learning and demonstration project. As it is an educational exercise, it is not vetted as a real-world deployment tool.

## Training Data
The dataset used for the training data was the UCI Census Income dataset. File used is census.csv with 32,561 rows and 15 columns. The dataset can be found here (https://archive.ics.uci.edu/dataset/20/census+income). For pre-processing, One-hot encoding was applied using OneHotEncoder, label binarization was applied using LabelBinarizer and an 80/20 train-test split was used.

## Evaluation Data
The evaluation was done using the 20% test split that was held out from the census.csv dataset. It was processed using the same fitted encoder. The training set was not independently sourced, but was just a random set from the same population. Due to this, there are implications for how much the results can be generalized.

## Metrics
The metrics used were Precision, Recall and F1/fbeta with beta = 1.
The overall values were (Precision 0.8383, Recall 0.4091, F1 0.5499)

## Ethical Considerations
One ethical consideration would be to acknowledge the sensitive attributes used in this dataset like race and sex. For example, as shown in the slice_output.txt file, recall was notably loer for Females (0.1399) versus Males (0.4579). Additionally, it should be noted that this model should not be used for real decision making like for loans, hiring or other individual classifications, given the known disparities, and the fact that this is not a current dataset.

## Caveats and Recommendations
As this dataset is from 1994, it does not represent current economic conditions. Additionally, a relatively shallow model was used with max_depth = 5, so it is likely underfitted. To improve this model, I would recommend the use of more current data and to use a larger max_depth to attempt to achieve better results.