# Report_1033_Project

## Table of Contents
- [Project Goal](#project-goal)
- [Project Description](#project-description)
- [How to Reproduce](#how-to-reproduce)
- [Initial Questions](#initial-questions)
- [Data Dictionary](#data-dictionary)
- [Project Plan](#project-plan)
    - [Wrangling](#wrangling)
    - [Exploration](#exploration)
    - [RFM Analysis](#rfm-analysis)
    - [Deliverables](#deliverables)
    - [Final Report](#final-report)
    - [Modules](#modules)
- [Summary and Recommendations](#summary-and-recommendations)

## Project Goal
The goal of this project is to offer summary analysis on the '1033 Program' data regarding the acquisition of DoD military equipment by State and Local agencies across the US States and territories. An overview of what equipment and values are being acquired and by who. A State/Region and Agency overview of militarization is provided in the hope of forming some baseline understanding of where and who is being militarized.

## Project Description
This data is open-source from the dla.mil website and this dataset was acquired from a cleaned version from: 
https://www.kaggle.com/datasets/jpmiller/military-equipment-for-local-law-enforcement?select=dod_all_states.csv

This project gives a summary overview of the data and then does an RFM (Recency, Frequency, Monetary) segmentation of the Agencies to provide context of who is most active in the program. Understanding this program and the Federal, State, and Local involvement can help paint a picture of the militarization of America's Police forces and if paired with additional data (moving forward) answers as to 'why' may manifest. This project does not currently account for if these acquisitions are proactive or reactive, push or pull, but may provide a baseline for such inquiries moving forward. 

## How to Reproduce 
To reproduce the outcomes in this project:
1. Acquire the initial .csv file from the above Kaggle profile. 
2. Clone this repo and ensure you have all of the necessary modules and notebooks.
3. Use of these libraries: pandas, numpy, matplotlib, seaborn, sklearn.
4. Be able to run the 'Report_1033_Program' jupyter notebook file. 
   - Supplemental workbooks may also be useful in identifying some of the steps taken prior to the cleaner final code 

## Initial Questions 
_Initial Data Centric Questions_
1. What is the overall distribution of equipment?
2. What States/Regions are acquiring the most equipment?
3. What equipment is being acquired the most?
4. What agencies are acquiring the most equipment?
5. Inside each State/Region what is the highest value acquisition?
6. Is there an overlap for timelines of acquisition by State/Region?
7. What is the breakdown of key categories of equipment?
8. Is the distribution proactive or reactive? (Federal-push or Agency-pull)
9. Which States/Regions have higher average acquisitions?
10. What equipment is generally the largest acquisition value?

## Data Dictionary
| Attribute                             | Definition                                             | Data Type | Additional Info                 |
|:--------------------------------------|:-------------------------------------------------------|:---------:|:--------------------------------|
| State                                 | State/Territory (abbreviation)                         | object    | 53 Unique State/Territory       |
| Agency_Name                           | State/Local Agency                                     | object    | 5632 Unique                     |
| NSN                                   | Unique identifier for equipment                        | object    | Serial identifier               |
| Item_Name                             | Item Name description                                  | object    |                                 |
| Quantity                              | Quantity of item                                       | int       | Per transaction                 |
| UI                                    | Description of unit size                               | object    | Example: Each, Kit, Pair        |
| Acquisition_Value                     | Monetary value ($) per unit                            | Float     |                                 |
| DEMIL_Code                            | Code to classify DoD DEMIL property                    | object    |                                 |
| DEMIL_IC                              | Integrity code for status of DEMIL_Code                | object    |                                 |
| Ship_Date                             | Date equipment was shipped                             | datetime  | Index of main dataframe         |
| total_value                           | Total monetary value of transaction (target)           | float     | Quantity * Acquisition_Value    |


## Project Plan
This project will start with some initial planning and question exploration before we even access the data. The question exploration has been delved out in the _Initial Questions_ section. 
Additionally let us detail what is to be provided at the conclusion of this project:
 - This README.md
 - Report_1033_Program.ipynb 
 - Workbooks and modules used

Moving forward we will **wrangle (acquire/prepare)** our data, **explore** for insights and to provide a deeper understanding of just what we are looking at, and create a **RFM** dataframe to segment and rank the Agencies that are utilizing the program. 

For a more detailed breakdown of these steps please see the Final Report and workbooks provided. 

### Wrangling 
This section contains our acquisition and preparation of the data.

The wrangle.py module contains the code needed to properly acquire and prepare the data. In it nulls are addressed, some datatype modification is performed, and the total_value column is feature engineered. 

The dataframe consists of 130957 transactions that span from 1990-05-03 to 2021-09-30.

### Exploration
For exploration we used the entire dataframe. No splitting of the data was performed as there was no (current) intention for modeling. The explore.py file contains a number of functions that were used to help gain insights into our data, using both visual and statistical methods. The main functions explore the transactions across the time period through use of the *Ship_Date* index and the main target variable *total_value*. 

### RFM Analysis
In leau of modeling RFM (Recency, Frequency, Monetary) analysis was performed to create a dataframe that segments the Agencies into *Top User, High Use, Medium Use, Low Use, and Lowest Use* categories based on a 5 point scale and ranking. The weights used for ranking were .15 * Recency, .28 * Frequency, and .57 * Monetary (total_value) value rankings to provide an overall RFM_Score. While scaling is not used the rankings do factor in a relative ranking to dictate how Agencies compare to eachother, and the final outcome is the following split: *Top User 8%, High Use 10%, Medium Use 20%, Lowest Use 32%, Low Use 30%*.

This outputs a dataframe that can be used to analyze based on State and Agency, and can be re-created by following the notebooks and modules provided.

### Deliverables 
The main deliverable from this project is the Report_1033_Program notebook. Additionally there are modules that contain the functions used and workbooks where a deeper exploration of the process can be seen.

#### Final Report
The Report_1033_Program notebook can be ran to reproduce the same results from start to finish. 

#### Modules
The modules included in this project are:
- wrangle.py
- explore.py
- rfm.py

### Summary and Recommendations
This project provides a baseline that can give an introduction to the 1033_Program and an overview of which States or Agencies are utilizing it. It also provides a quick glimpse at some metrics that can be useful, such as equipment or total_value. Some major takeaways are which States are utilizing the program the most (TX, CA, TN for example), some questionable acquisition locations (such as PR), and some timelines when acquisitions have trended. (2010-2017) Additionally, I think it paints a very clear picture that the militarization of Police has been an ongoing endeavor from both a Federal and State level for quite some time, and has no intention of slowing. One could use this project to look up local States or Agencies and see how they fare based on a comparison of their peers, but I would recommend using this site (no-affiliation to myself) if one is curious: https://project1033.org. 

Moving forward this project provides a foundation that additional information can be coupled with to hopefully provide ongoing insights into the situation. Such prospects may be crime statistics, legislation, political activity, or local activity. There does seem to be an indication that the program has fluctuations (preemptively at that) based on Executive and Congressional legislation. While this work does not provide a conclusive answer for motivations or if this activity is being Federally pushed (as in equipment being intentionally, systematically given to a more decentralized military aka Police) it does hopefully provide a better understanding of the problem and a baseline for interacting with some of those larger questions in the future.