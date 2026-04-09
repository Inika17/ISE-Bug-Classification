# User Manual: Bug Report Classification Tool

This tool implements an automated Support Vector Machine (SVM) pipeline designed to identify rare performance bugs within large-scale software projects.

### Operational Steps

1. **Clone the Repository:** Download the project source code to your local environment.
2. **Install Dependencies:** Ensure your environment meets the specifications listed in the `requirements.pdf` file.
3. **Verify Datasets:** Ensure the five project CSV files (**TensorFlow, PyTorch, Keras, MXNet, and Caffe**) are located within a directory named `datasets/` in the project root.
4. **Prepare Output Directories:** If not already created, manually create two empty folders named `NB/` and `SVM/` in the root directory. These folders are required to store the results, as the scripts do not generate them automatically.
5. **Execute Baseline Model:** Run `python br_classification.py` to generate the Naive Bayes baseline results. The output will be saved automatically to the `NB/` directory.
6. **Execute Proposed Solution:** Run `python br_svm_classification.py` to train and evaluate the SVM model. These results will be saved to the `SVM/` directory.
7. **Perform Statistical Analysis:** Once both models have been run, execute `python statistical_test.py`. This script will process the generated CSV files to calculate the Wilcoxon signed-rank test results and confirm statistical significance.

### Output Description
The outputs in the `NB/` and `SVM/` folders are stored as CSV files containing the performance metrics (Accuracy, Precision, Recall, F1-Score, and AUC) for each of the 30 experimental runs. These files serve as the raw data source for the summary tables and statistical p-values presented in the final report.