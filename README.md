--------------------------------------------------------------------------------
Clones the Repository

Each team member runs this on their own machine:

git clone https://github.com/Madmanstn/GeoAlert.git
cd GeoAlert

Then set up the backend:

cd backend
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements/development.txt
copy .env.example .env

Then open .env and fill in their own database credentials.

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=your-supabase-password
DB_HOST=db.dxncngkzfgoxlocaomnv.supabase.co
DB_PORT=5432

Then run migrations:

python manage.py migrate
python manage.py seed_data
python manage.py runserver



Then set up the frontend in a new terminal:

cd frontend
npm install
copy .env.example .env
npm start

--------------------------------------------------------------------------------


Install GDAL for Python 3.11 on Windows  ---- for POSTGIS
Step 1 — Open this link in your browser and download the file:
https://github.com/cgohlke/geospatial-wheels/releases/tag/v2025.10.25

Look for the latest release and find this exact file:
gdal-3.11.4-cp311-cp311-win_amd64.whl




install PostGIS via Stack Builder

Create the Database Using pgAdmin
Step 1 — Open pgAdmin from your Start Menu. Search for "pgAdmin 4".
Step 2 — When pgAdmin opens it will ask for a Master Password. This is the password you set when you first installed pgAdmin. Enter it.
Step 3 — Connect to PostgreSQL:

On the left panel click Servers
Click PostgreSQL 15 (or whatever version shows)
It may ask for your postgres password here

Step 4 — Create the database:

Right click on Databases
Click Create → Database
In the Database field type: geoalert_db
In the Owner field select: postgres
Click Save

Step 5 — Enable PostGIS on the database:

Expand Databases → click on geoalert_db
Click on Tools in the top menu → Query Tool
In the query editor paste this and click the Play button (▶):

sqlCREATE EXTENSION IF NOT EXISTS postgis;

You should see CREATE EXTENSION in the output below

Step 6 — Create the app user:

In the same Query Tool paste and run:

sqlCREATE USER geoalert_user WITH PASSWORD 'geoalert2026';
GRANT ALL PRIVILEGES ON DATABASE geoalert_db TO geoalert_user;
GRANT ALL ON TABLE spatial_ref_sys TO geoalert_user;

Step 7 — Verify PostGIS:

Run this in the Query Tool:

sqlSELECT PostGIS_version();
You should see a version number in the output.

Then update your .env file with the password you used:
DB_NAME=geoalert_db
DB_USER=geoalert_user
DB_PASSWORD=geoalert2026
DB_HOST=localhost
DB_PORT=5432


user = User.objects.create_superuser(email='admin@geoalert.gov.ph', password='Admin2026!', full_name='GeoAlert Administrator')




install POSTMAN Thunder Client in vscode
to test the login endpoint 

or on browser