import pandas as pd
import ast
from scipy import stats

projects = ['tensorflow', 'pytorch', 'keras', 'incubator-mxnet', 'caffe']

for project in projects:
    nb_file = f'NB/{project}_NB.csv'
    svm_file = f'SVM/{project}_SVM.csv' 
        
    # Read the CSV files
    df_nb = pd.read_csv(nb_file)
    df_svm = pd.read_csv(svm_file)
    
    # Extract the arrays of 30 AUC scores
    nb_auc_scores = ast.literal_eval(df_nb['CV_list(AUC)'].iloc[-1])
    svm_auc_scores = ast.literal_eval(df_svm['CV_list(AUC)'].iloc[-1])

    # Run the Wilcoxon signed-rank test for AUC
    _, p_value_auc = stats.wilcoxon(nb_auc_scores, svm_auc_scores)

    print(f"Project: {project}")
    print(f"AUC Score P-Value: {p_value_auc:.5f}")
    
    # The standard academic threshold for significance is 0.05
    if p_value_auc < 0.05:
        print("Result: p < 0.05\n")
    else:
        print("Result: p >= 0.05\n")

print("Statistical testing complete!")