# day-8
Description:
 This projects analyzes students performance using marks ,attendance and assignments scores. It generates student data  classifies them into categories and performance statistical analysis using python.
 Features :
  Random data generation
  Student classification 
  Performance index calculation
  Statistical analysis 
  Data displayed using pandas Dataframe
Logic Used :
 generated students data using random
 stored records in lists and tuples
 Used dictionaries for classifiaction
 Converted data into DataFrame
 Calculated mean manually and used numpy for advance metrics
Personlization :
 Last digit:5 
 generated 5 students
sample output: 
  id  marks  attendance  assignment  performance catagories  normalized
0   1     63          59          48        32.74        avg    0.826667
1   2      3          65          43        14.95    at risk    0.026667
2   3      1          52          29         7.80    at risk    0.000000
3   4     76          26          19        12.35    at risk    1.000000
4   5     66          11          14         4.40    at risk    0.866667
{1: 'avg', 2: 'at risk', 3: 'at risk', 4: 'at risk', 5: 'at risk'}
(np.float64(41.8), np.float64(32.79), np.int64(76))
moderate academic system
