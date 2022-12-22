## Homework 23
This application emulates command line functions to get data from file. 

There're some parameters you can use in the app:

 - filter - works like search string in file
 - map - splits all file strings by space and returns a single column
 - sort - sorts all strings by ascending or descending order
 - unique - returns only unique strings
 - limit - returns certain amount of file strings
 
To get correct result you need to adhere to following rules:
1. Use this query format cmd1={method}&value1={value}&cmd2={method}&value2={value}&file={filename}
(for instance cmd1=filter&value1=google&cmd2=limit&value2=30&file=log.txt
2. Use all necessary parameters and provide correct values 
 ---
The project's structure: 
 - file_dao.py - DAO to work with files
 - file_service.py - a service with business logic
 - args_checker.py - ArgumentsChecker class to check if arguments is valid
 - constants.py - there're file paths, mapping dict, etc
 - container.py - there're DAO, Service classes' and another instances
 - requirements.txt - file with the project's dependencies
 - app.py - a main file to start the application
 - README.md - this file with app info
 ---
 The project was created in 22 December 2022 by Aleksey Mavrin