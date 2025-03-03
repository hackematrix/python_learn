from typing import List
import pandas as pd

def createDataframe(student_data:List[List[int]]) ->pd.DataFrame:
    student_id=[rows[0] for rows in student_data]
    age=[rows[1] for rows in student_data]
    
    data={'student_id':student_id,
          'age':age}
    frame=pd.DataFrame(data)
    return frame

def print_dataFrame(data_example:pd.DataFrame):
    print(data_example)

student_data=[[1,15],
              [2,11],
              [3,11],
              [4,20]]


   

if __name__=='__main__':
    frame=createDataframe(student_data)
    print_dataFrame(frame)
