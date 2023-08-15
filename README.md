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

## Application Flow: Managing Patient Reservations
1. Patient Table:
   * The patients table stores personal information.
2. Doctor Table:
   * The doctors table contains the profiles of the doctors, include personal information and expertise.
3. Doctor Slot Table:
   * The doctor_slots table stores information about doctor schedules, allowing reservations to be made for available time slots.
4. Reservation Table:
   * The reservations table handles booking details, recording patient and doctor IDs for each reservation.
   * Before insertion, the system validates if the chosen reservation date aligns with the doctor's availability.
5. Reservation Process:
   * A patient requests a reservation by specifying the desired doctor and preferred date.
   * The system checks if the chosen doctor has an available slot on the requested date.
   * If the slot is available, the system creates a reservation entry in the reservations table.
   * If the slot is not available, the patient get the message to select an alternative date or doctor.
6. Reservation Confirmation:
   * If the reservation data was inputed, the system will give patients about reservation details and doctor's information.
