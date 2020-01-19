# Experiments for Celosia

### Required Python Version
* Python 3.7 is required, you can verify your environment using:
  ```
  python celosia.py verifyenv
  ```

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
