# PesaTrack


## Project Description

PesaTrack is a complete online finance tracker which allows to eep track of your finances be it cash or mobile money. Forget about the days money is gone and you have no idea how it was spent!
      
<!-- 
## BDD

| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| View photos of interest | Scroll to see a gallery and click on picture | Displays a picture with name description and copy link for sharing |
| Search a picture by category | Enter the category in the search input| Displays Images in the searched category |
| View pictures by location | Click on location of interest from the Navbar | Displays Images of chosen location |
| Copy Link to clipboard | Click on copy link button in the modal class | Copies link to clipboard |
| View Single picture | Click on photo of interest then click on image | Displays a single page with details of the picture and related images | -->

<br>




## Getting Started

To clone the repository, run:

    git clone https://github.com/sirgama/pesatrack

Then navigating to the cloned directory:

    cd pesatrack


### Prerequisite
This pesatrack Clone project requires a prerequisite understanding of the following:
- Django Framework
- Python3.9
- Postgres
- Python virtualenv

## Setup and installation

###  Activate virtual environment
Activate virtual environment using python3.9 as default handler
    `virtualenv -p /usr/bin/python3.9 genv && source genv/bin/activate`
####  Install dependancies
Install dependancies that will create an environment for the app to run `pip3 install -r requirements.txt`
####  Create the Database
    - psql
    - CREATE DATABASE pesatrack;
####  .env file
Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'pesatrack'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
#### Run initial Migration
    python3.9 manage.py makemigrations pesatrack
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000

## Deployment

The application is deployed on Heroku and is live on this link:

[https://pesatrack.herokuapp.com/](https://pesatrack.herokuapp.com/)


## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Authors

- **Gamaliel Sirengo** - *Full Stack Developer* -
- **Sarah Kamunya** - *Full Stack Developer* -
- **Lydia Wachira** - *Full Stack Developer* -
-  **Innocencia Kakan** - *Full Stack Developer* -
## License

MIT License

Copyright (c) 2022 Gamaliel Sirengo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


