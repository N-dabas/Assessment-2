# Overview of the project

- `You can either run Assessment.py as python script or Assessment.ipynb as jupyter notebook.`
- I have first converted the tables into csv files and used Pandas library.
- I have taken USER,PRICE as a primary key for joining both the tables.
- Also changed Price column name for joining both the tables.
- The final_table shows the difference between the quantity that were to be executed and the quantity that were actually executed.


## Note:
- The quantity diff for two of the OrderREF is `negative` since the executed Qty is more than ordered Qty. Maybe, we are missing some entries in the order log.
