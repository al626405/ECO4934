## ECO4934 - Topics In Econometrics 
#### Dr. Paarsch
#### 07/03/2024
#### Final Project 

#### <u>**Group B:**</u>
- Polina Baikova
- Jonathon Lewis
- Payton Irvin
- Alexis Leclerc

## Usage

**The Makefile is comprised of 3 mini makefiles. The First mini-Makefile converts a MariaDB database schema that contains 3 tables for Train, Test, & Validation data into an SQLite3 DB. The data was worked/cleaned/revised/filtered earlier in the project and uploaded to multiple MariaDB databases, eventually consolidating into the DB with the 3 Tables for Train, Test, & Validation. As a Business Analyst performing Busienss Intelligence, we will later hand off our completed project over to the production team. Our goal is to package our final results in a computationally efficient and concise way. The Makefile allows anyone to replicate the same project that our team completed.**

**The second mini-Makefile first runs the R scripts composed of multiple models. The scripts save Figures to the Figures Folder, it also saves the plot data so that it can later be plotted alongside our python models later on. After this portion completes it moves on to the python scripts that contain the rest of the models. Python is more computationally efficient than R and we ran models like Boosting, Bagging, Random Forest and had a relatively large dataset. The script then creates a final plot with all our models using the data of the plots for the each model.**

**The third mini-Makefile compiles the Latex slides into a pdf document using the Figures from the Figures folder. We also have an HTML webpage and CSS script which gets updated with the Figures generated from our scripts.**
