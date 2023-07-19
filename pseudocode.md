# Where do I begin? What am I doing?

No idea, so ask lots of questions.

Create an interactive shell script with the help of python that helps superheroes stay in touch with their friends and keep track of supervillains through the terminal.
For this project, we will be using Python 3 and PostgreSQL and the PyPi package psycopg3.

I don't have docker and cannot install it due to hardware and software constraints

# Procedural
### user stories
 - As a superhero, I want to add new friends to my network so that I can keep in touch with them and strengthen our alliance against supervillains.

- As a superhero, I want to view a list of all my friends (superheroes) and foes (villains) in the database so that I can keep track of them and their current status.
- As a superhero, I want to update the type (hero/villain) of my friends in the database, so I can ensure accurate information about their alignment and activities.
- As a superhero, I want the interactive shell script to maintain data consistency in the database, ensuring that no duplicate entries or invalid data is allowed.
- As a superhero, I want the interactive shell script to provide a smooth and efficient user experience, minimizing delays in data retrieval and processing, so I can focus on protecting the world.


## Begin

Connect to the PostgreSQL Database: At the beginning, the program establishes a connection to the PostgreSQL database. This step ensures that the script can communicate with the database for data storage and retrieval.

## Init
Create a Table for Superheroes and Villains: Once connected to the database, the script initializes the project by creating a table named "heroes_villains." This table will store information about superheroes and villains, such as their names and types.

Questions:
Who are the superheroes? where will the data be drawn from?

## Render
- Provide an Interactive Shell Interface for Users: After setting up the database, the script presents an interactive shell interface to the users. This interface allows users to interact with the database through the terminal using various commands.
  *Note* there will only be interactivity in the terminal and no where else. queries will be made using sql

## Compute

## END

# Flowchart 
```
                      +-------------------------------+
                      |       Begin: Connect DB       |
                      +-------------------------------+
                                  |
                                  v
                      +-------------------------------+
                      | Initialize: Create Table     |
                      +-------------------------------+
                                  |
                                  v
                      +-------------------------------+
                      |         Render: Shell         |
                      |                               |
                      |  +-------------------------+  |
                      |  | Display Options         |  |
                      |  +-------------------------+  |
                      |             |                 |
                      |             v                 |
                      |  +-------------------------+  |
                      |  | User Input and Action   |  |
                      |  +-------------------------+  |
                      |             |                 |
                      v             v                 |
          +------------------+   +------------------+  |
          | Update Database |   | Show Data         |  |
          +------------------+   +------------------+
```

# Functional 

```
function create table
{
if table name doesn't exist, make the table with the name
}
function make a hero
{
add a hero and values with it

}
function add relationships
{
if a friend of a hero, build a link on grounds of being an ally

if an enemy of a hero, build a link on grounds of being an enemy
}

function add abilities
{
if a hero exists claiming of having an ability, connect it otherwise ignore
}


```

# Object Oriented

# Chat GPT Advice Procedural
Begin:

Connect to the PostgreSQL Database: At the beginning, the program establishes a connection to the PostgreSQL database. This step ensures that the script can communicate with the database for data storage and retrieval.

Initialize:

Create a Table for Superheroes and Villains: Once connected to the database, the script initializes the project by creating a table named "heroes_villains." This table will store information about superheroes and villains, such as their names and types.

Render:

- Provide an Interactive Shell Interface for Users: After setting up the database, the script presents an interactive shell interface to the users. This interface allows users to interact with the database through the terminal using various commands.

X Options Display: In the interactive shell, the available options are displayed to the users. These options represent the CRUD operations (Create, Read, Update, Delete) that they can perform on the superhero and villain data.

User Input and Action: Users are prompted to enter their choice (1/2/3/4/5) based on the displayed options. The script takes the user's input and proceeds accordingly:

Option 1: Add Hero/Villain - Users can input the name and type (hero/villain) of a new superhero or villain, which will be added to the database.
Option 2: View All Heroes/Villains - The script retrieves all the superheroes and villains from the database and displays them in a formatted manner.
Option 3: Update Hero/Villain Type - Users can input the ID of a hero/villain and update its type (hero/villain) in the database.
Option 4: Delete Hero/Villain - Users can input the ID of a hero/villain to be deleted from the database.
Option 5: Exit - If users choose to exit, the script ends the interactive shell loop and the program terminates.

## superhero stories

- As a superhero, I want to add new friends to my network so that I can keep in touch with them and strengthen our alliance against supervillains.

 - As a superhero, I want to view a list of all my friends (superheroes) and foes (villains) in the database so that I can keep track of them and their current status.

- As a superhero, I want to update the type (hero/villain) of my friends in the database, so I can ensure accurate information about their alignment and activities.

X As a superhero, I want to delete supervillains from the database, so I can maintain an up-to-date list of threats and potential dangers to our world.

X As a superhero, I want to easily navigate through the interactive shell interface, so I can quickly perform various CRUD operations without any technical complexities.

X As a superhero, I want the interactive shell script to provide clear instructions and prompts, so I can easily understand the available options and make informed decisions.

X As a superhero, I want the interactive shell script to handle errors gracefully, so I can receive meaningful error messages and troubleshoot any issues encountered during database operations.

- As a superhero, I want the interactive shell script to maintain data consistency in the database, ensuring that no duplicate entries or invalid data is allowed.

X As a superhero, I want the interactive shell script to be secure and protect my superhero friends' data from unauthorized access or modifications.

- As a superhero, I want the interactive shell script to provide a smooth and efficient user experience, minimizing delays in data retrieval and processing, so I can focus on protecting the world.



