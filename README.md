Dependencies: python 2.7, opencv 2.4.9, numpy, skpealn, scipy

how to use:
1. put your data files under a directory in the following structure
- <root_dir>
  - train
    - <class1_name>
      - ...images under the folder
    - <class2_name>
      - ...images under the folder
    ...
  - query
    - ...images under the folder
2. run the program by: 
   python complete_system.py <root_dir> <option>
   where option can be
   1. direct knn
   2. svm (eager learning)
   3. lamp svm
   4. cnn
   5. lamp cnn


