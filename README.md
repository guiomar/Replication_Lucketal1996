Main file: create_data.m

Create a list of data for Luck et al. 1996 Replication #EEGManyLabs
INPUT: 
- wordlist: MAT file with words for your language

OUTPUT:
- LuckList.csv
   * T0, T1, T2
   * lags: Lags generated, containing:
       * lagT1: random values between 7 and 10
       * lagT2: random (1, 3, or 7)
       * lagEnd: lagT0 + lagT1 + lagT2 = 20
   * response T1
   * response T2
   * related
- distractors.csv

Authors: Guiomar Niso, Instituto Cajal, 2024
