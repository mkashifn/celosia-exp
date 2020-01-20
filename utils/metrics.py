# Performance Metrics
def get_accuracy(y_true, y_pred):
  '''Return accuracy of the prediction on a scale of 0-1.
     Parameters: y_true = true labels (1 = normal, 0 = anomalous)
                 y_pred = the predicted output obtained using label_data().'''
  #assert len(y_true) == len (y_pred), "y_true and y_pred are of different dimensions"
  total = len(y_pred)
  correct = 0
  fp = 0 # false positives (when prediction = normal, actual = anomalous)
  fn = 0 # false negatives (when prediction = anomalous, actual = normal)

  tp = 0 # total positives (normal)
  tn = 0 # total negatives (anomalous)

  for i in range(len(y_pred)):
    correct += (1 if y_true[i] == y_pred[i] else 0)
    fp += (1 if ((y_true[i] == 0) and (y_pred[i] == 1)) else 0)
    fn += (1 if ((y_true[i] == 1) and (y_pred[i] == 0)) else 0)
    tp += (1 if y_true[i] == 1 else 0)
    tn += (1 if y_true[i] == 0 else 0)
  offset = 1e-7 # add offset to avoid divide-by-zero exception
  total = float(total) + offset
  accuracy = float(correct)/ total
  print ('Accuracy:', accuracy, 'TP:', tp, 'FP:', fp, 'FN:', fn, 'TN:', tn)