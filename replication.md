# Replication

This document provides the necessary details to replicate the experimental outcomes presented in the project report. 

### 1. Data Acquisition
The raw data used for this experiment consists of bug reports from five open-source deep learning frameworks. The datasets must be sourced from the following repository:

**Source URL:** [https://github.com/ideas-labo/ISE/tree/main/lab1](https://github.com/ideas-labo/ISE/tree/main/lab1)  

The following five files must be downloaded and placed within the `datasets/` folder in the project root:
* `tensorflow.csv`
* `pytorch.csv`
* `keras.csv`
* `incubator-mxnet.csv`
* `caffe.csv`

### 2. Experimental Parameters and Logic
To eliminate stochastic bias, both the baseline (Naive Bayes) and the proposed solution (SVM) are configured to run with a repetition constant of **30**. The replication script handles this through a controlled loop:

* **Loop Iterations:** `REPEAT = 30`
* **Random Seed Control:** To ensure identical data shuffling across different machines, the `random_state` parameter for the train-test split is mapped directly to the loop index (`random_state = repeated_time`). This ensures that seeds 0 through 29 are used sequentially, allowing for an exact reconstruction of every data partition.
* **Data Partitioning:** Each run utilizes a 70% training and 30% testing split.

### 3. Execution and Data Integrity
The scripts `br_classification.py` and `br_svm_classification.py` are designed to append results to existing CSV files in the `NB/` and `SVM/` directories respectively.

**Note:** Before initiating a replication run, the user must delete or clear any existing CSV files within the `NB/` and `SVM/` folders. Failure to do so will result in "data pollution," where old results are mixed with new entries.

### 4. Verification of Results
Upon completion of the 30 runs and the execution of `statistical_test.py`, the generated averages for Accuracy, Precision, Recall, F1-Score, and AUC should match the values presented in **Table 1** of the main report. Small variations may occur due to library versioning, but the observed trends and statistical significance ($p < 0.05$ for the majority of projects) will remain consistent.