import sqlite3

# Task 1: Add a Member
def add_member(id, name, age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        # SQL query to add a new member
        cursor.execute("INSERT INTO Members (id, name, age) VALUES (?, ?, ?)", (id, name, age))
        
        # Commit the transaction
        conn.commit()
        print("Member added successfully.")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. The member ID may already exist.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        # SQL query to add a new workout session
        cursor.execute(
            "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (?, ?, ?, ?)", 
            (member_id, date, duration_minutes, calories_burned)
        )
        
        # Commit the transaction
        conn.commit()
        print("Workout session added successfully.")
    
    except sqlite3.IntegrityError as e:
        print(f"Error: {e}. The member ID may be invalid.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        # Check if member exists
        cursor.execute("SELECT id FROM Members WHERE id = ?", (member_id,))
        if cursor.fetchone() is None:
            print("Member not found.")
            return
        
        # SQL query to update age
        cursor.execute("UPDATE Members SET age = ? WHERE id = ?", (new_age, member_id))
        
        # Commit the transaction
        conn.commit()
        print("Member age updated successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        # SQL query to delete a session
        cursor.execute("DELETE FROM WorkoutSessions WHERE id = ?", (session_id,))
        
        # Check if a row was deleted
        if cursor.rowcount == 0:
            print("No workout session found with the provided session ID.")
            return
        
        # Commit the transaction
        conn.commit()
        print("Workout session deleted successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Function to create the necessary tables
def create_tables():
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        # Create Members table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Members (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')
        
        # Create WorkoutSessions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS WorkoutSessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                duration_minutes INTEGER NOT NULL,
                calories_burned INTEGER NOT NULL,
                FOREIGN KEY (member_id) REFERENCES Members (id)
            )
        ''')
        
        # Commit the transaction
        conn.commit()
        print("Tables created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Function to view all members
def view_members():
    try:
        conn = sqlite3.connect('gym.db')
        cursor = conn.cursor()
        
        # SQL query to fetch all members
        cursor.execute("SELECT * FROM Members")
        members = cursor.fetchall()
        
        if members:
            print("Members:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        else:
            print("No members found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the connection
        conn.close()

# Menu interface
def menu():
    create_tables()  # Ensure tables are created before performing any operations

    while True:
        print("\nGym Management System")
        print("1. Add a Member")
        print("2. View Members")
        print("3. Add a Workout Session")
        print("4. Update Member Age")
        print("5. Delete a Workout Session")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            id = int(input("Enter Member ID: "))
            name = input("Enter Member Name: ")
            age = int(input("Enter Member Age: "))
            add_member(id, name, age)
        
        elif choice == '2':
            view_members()
        
        elif choice == '3':
            member_id = int(input("Enter Member ID: "))
            date = input("Enter Workout Date (YYYY-MM-DD): ")
            duration_minutes = int(input("Enter Duration (in minutes): "))
            calories_burned = int(input("Enter Calories Burned: "))
            add_workout_session(member_id, date, duration_minutes, calories_burned)
        
        elif choice == '4':
            member_id = int(input("Enter Member ID: "))
            new_age = int(input("Enter New Age: "))
            update_member_age(member_id, new_age)
        
        elif choice == '5':
            session_id = int(input("Enter Workout Session ID: "))
            delete_workout_session(session_id)
        
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    menu()
