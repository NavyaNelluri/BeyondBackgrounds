# BeyondBackgrounds
Our application aims to revolutionize the way resume filtering is conducted,  particularly by ensuring that job skills are assessed independently of a candidate's  criminal record. This approach sets us apart from traditional software solutions by  providing a fair and unbiased hiring process.

# Use Cases
## Skill-Based Matching: 
Our software identifies and matches a candidate’s skills 
with job requirements, eliminating the influence of criminal records on initial 
screening.
##Diversity and Inclusion: 
Promoting diversity by preventing discrimination based 
on criminal history, thus ensuring a broader pool of candidates.
##Efficient Hiring:
Reducing the time and effort needed for manual screening, leading 
to faster and more efficient hiring processes.
# Users
## HR Professionals: These users will interact with the system to create job postings, 
define skill requirements, and review matched candidates' profiles without access to 
criminal record information.
## Recruiters: 
Responsible for conducting initial screenings, recruiters will use the 
software to shortlist candidates based on skills and qualifications, removing personal 
biases.
## Candidates:
Applicants can view job listings, submit resumes, and track their 
application status, confident that their criminal records won't be a determining factor 
in the initial screening process.

![image](https://github.com/NavyaNelluri/BeyondBackgrounds/assets/123142678/0bb01c7b-35a2-488f-9bfe-a30fbbf64932)

1. Applicants and recruiters data which they have submitted through application 
will be stored in the database as shown in the diagram.
2. Then the data will be segmented via Python framework to match the 
appropriate job postings.
3. Web application will allow recruiters to sort according to the category.
## Front end:
1. Separate authentication process for applicants and job seekers.
2. Applicants/job seekers will fill in their details along with criminal records 
through the application process.
3. Recruiters will also have the feature of uploading job postings from a web
application.
4. Front-end will also give the ability for recruiters to do sorting based on 
categories like criminal record or skill set. 
## Back-end: 
1. Maintaining the data in the database.
2. Framework for mapping process
3. Connection to Database.

## Instructions for setting up a development environment:
1. To run our application, python development environment is required.
2. The required libraries to run our application are mentioned in the requirements.txt file.


## Steps to build and run your application:
1. Run application in python environment.
   After setting up the python environment and installing all the necessary packages and libraries,Run the app.py file in terminal by using the command : python app.py
   You can access the application in the localhost port 80.
2.Running application using docker file.
  Docker file is provided to built & run the image for the application.
  Build Command:  docker build -t <imagename>:<tag>
  Run command : docker run -p 80:80 --name <container_name> <imagename>:<tag>
  After successful execution of above commands,the application is available at localhost port 80


## Information for future development:
1.Possible Enhancements:
  Addition of more filters to filter the applicants.
  Can implement machine learning algorithm to predict the selection of resume.
