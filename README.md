# zicare

## Documentation for running code 

#### Install requirements, by typing this code in your terminal
```
python -m pip install -r requirements.txt 
```

#### Migration
* Create database
* Go to `db.py` inside the config folder, and edit the database name `mysql+pymysql://root@localhost:3306/db_name`
* You can view the database structure by referring to the following link: [Database Structure](https://dbdiagram.io/d/64db583302bd1c4a5ecc954d).
* If you happen to need the data, you can download it from the following link: [Download Data](https://drive.google.com/file/d/1heFJAQxn4n2Psm3pgjJOqJHyYu524ACY/view?usp=sharing).


Finally for running application type `uvicorn index:app --reload` in terminal
