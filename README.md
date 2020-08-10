# Flask Microservice
  A flask microservice Cookie Cutter that I made to ease the initial setup whenever I start a project.


## System Installation
  1. Make sure that your operating system can execute [make commands](https://www.gnu.org/software/make/manual/make.html)
  2. Download any python virtual environment manager e.i. [virtualenv](https://virtualenv.pypa.io/en/latest/), [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), [conda](https://docs.conda.io/en/latest/)


## Project Installation
  1. Read and understand the content of the makefile
  2. Create an `.env` file
  
      ```
      # Sample .env file
      FLASK_ENV={project_env}
       
      DB_NAME={db_name}
      DEV_DB_HOST={db_host}
      DEV_DB_AUTH={db_username}:{db_password} 

      STAG_DB_HOST={db_host} 
      STAG_DB_AUTH={db_username}:{db_password} 
      
      PROD_DB_HOST={db_host}
      PROD_DB_AUTH={db_username}:{db_password} 
     ```
  3. Execute install dependencies by executing `make install`
  4. Export the app name using `export FLASK_APP=${APP_NAME}.py`
  6. Optional. `flask db init` (execute if the `migrations` folder does not exist)


## Database Operations
  [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
  Read about the [Alembic library](https://alembic.sqlalchemy.org/en/latest/) for fancier solution to your db migration problems 

#### Creating a migration file
  `make migrate`

#### Upgrading the Database
  `make upgrade`

#### Downgrading the Databas
  `make downgrade`
 

## Running the Project
#### Locally
  1. `export FLASK_APP={app_name}`
  2. `flask run [--port=8000]`

## Running Test
  `make test`

## Library Used
  - mypy
  - autopep8
  - Flask
  - Flask-Restful
  - Flask-SQLAlchemy
  - Flask-Migrate
  - Flask-GraphQL
