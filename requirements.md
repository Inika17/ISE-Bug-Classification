# Requirements Specification

### Environment
* **Python Version:** Python 3.11

### Required Libraries
| Library | Version |
| :--- | :--- |
| **pandas** | 3.0.2 |
| **numpy** | 2.4.2 |
| **scikit-learn** | 1.8.0 |
| **nltk** | 3.9.4 |
| **scipy** | 1.17.1 |

### Installation
All dependencies can be installed by running the following command in your terminal:

```bash
pip install pandas==3.0.2 numpy==2.4.2 scikit-learn==1.8.0 nltk==3.9.4 scipy==1.17.1
```
### Additional Setup
The NLTK stopwords corpus must be downloaded before running the scripts. This is handled automatically within the code via:

```bash
nltk.download('stopwords')
```