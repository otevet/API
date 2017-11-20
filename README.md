# RESTful API with flask

#### 1. Create Project folder named 'API' in home directory
#### 2. Download repo, unzip
#### 3. Extract 'app.py' 'take_home.csv' and into the new folder "API", or just clone the repo and skip steps 1 and 2.
#### 4. Open Linux Terminal and set working directory using "$  cd ~/API " -- sets as present working directory
#### 5. Run the code below ("$" for Linux Terminal User and ">" for sqlite3:


	#$ 
	mkdir rest-app
	cp app.py rest-app
	cp take_home.csv rest-app
	cd rest-app   #Sets to 'app root directory'
	sqlite3 takehome.db
		
	 # Load csv data into salaries table
	 # sqlite> 

		  .mode csv takehome

		  .import take_home.csv takehome
		
		# sqlite> 
		   
		  SELECT * FROM takehome limit 3;


	   # Next: 'Ctrl-D' quit out of sqlite3 from terminal
	

	# Make virtual environment with name "rest-api"
	# $ 
	  virtualenv rest-api
	  source rest-api/bin/activate     # Source into virtual environment for pip inst.


	# (rest-api)$ 
		sudo pip install flask  
		sudo pip install flask-restful
	  sudo pip install sqlalchemy

	#(rest-api) ~/API/rest-app$  
		sudo python app.py


#### 6. Navigate to browser:
        
	#http://localhost:3000/ID/column  # replace empty spaces with "%20" or "_" (for example, 'Web Browser' --> 'Web_browser')
  #if querying multiple ID's, separate them with a comma (,)
	#http://localhost:3000/ID/Exposure_stamps replace Exposure_stamps with the stamp number
  
   #make sure to replace ID with the desired user ID and column with the desired column name to query

  #Example: http://localhost:3000/b4b7e743-516d-4055-abb9-2b973fede411/Gender will produce the gender of  user_id 'b4b7e743..."
	

  ### Note: To get out of virtualenv
	control + D
	# (rest-api)
	deactivate 
