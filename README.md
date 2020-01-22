# Experiments for Celosia

### Required Python Version
* Python 2.7 is required, you can verify your environment using:
  ```
  python celosia.py verifyenv
  ```
### Dependencies
Celosia depends upon the following Python packages:
  * numpy
  * pickle
  * graphviz
  * random
  * math
  * warnings
  * sklearn
  * time
  * multiprocessing
  * modlamp
  * pandas
  * pylab

  
### Downloading Dataset
#### N-BaIoT Dataset
* URL: https://www.kaggle.com/mkashifn/nbaiot-dataset
* The directory structure should look like:<br>
  - datasets/nbaiot-dataset/1.benign.csv
  - datasets/nbaiot-dataset/1.gafgyt.combo.csv
  - ...
  - datasets/nbaiot-dataset/9.mirai.udpplain.csv
* Run the following command to verify if the dataset is valid
  ```
  python celosia.py verifydataset -d nbaiot
  ```
  Correct output:
  ```
  Success! 89 data files present in the N-BaIoT dataset.
  ```

### Running Experiments
##### Compute SOM accuracy vs chosen threshold:
  ```
  python celosia.py somaccth -d <device-id>
  ```
  ###### Device IDs:

  | Device ID| Device Name                              |
  |---------:|:-----------------------------------------|
  | 1        | Danmini_Doorbell                         |
  | 2        | Ecobee_Thermostat                        |
  | 3        | Ennio_Doorbell                           |
  | 4        | Philips_B120N10_Baby_Monitor             |
  | 5        | Provision_PT_737E_Security_Camera        |
  | 6        | Provision_PT_838_Security_Camera         |
  | 7        | Samsung_SNH_1011_N_Webcam                |
  | 8        | SimpleHome_XCS7_1002_WHT_Security_Camera |
  | 9        | SimpleHome_XCS7_1003_WHT_Security_Camera |

  Sample Output:
  ```
  python celosia.py somaccth -d 3
  Starting to compute SOM accuracy vs threshold for Ennio_Doorbell
  46 - Threshold=0.45
  ...
  Classification Report: 
                precision    recall  f1-score   support

           0.0       0.42      0.22      0.29       250
           1.0       0.95      0.98      0.97      4000

     micro avg       0.94      0.94      0.94      4250
     macro avg       0.69      0.60      0.63      4250
  weighted avg       0.92      0.94      0.93      4250


  ('Accuracy Score: ', 0.936235294117647)
  Confusion Matrix: 
  [[  55  195]
   [  76 3924]]
  ...
  ```
### Kaggle Notebooks

This following experiments has been moved to Kaggle. Please follow the links to access the complete code and output. Alternatively, you can also access the Jupyter notebook files in the snapshot directory of this repository. 

##### Zero-day attack detection:
  
  https://www.kaggle.com/mkashifn/celosia-zero-day-attack-detection

##### Dynamic network update:
  https://www.kaggle.com/mkashifn/celosia-dynamic-network-update