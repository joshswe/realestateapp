# Real Estate App with Django
In this project, we are going to build a real estate application for a fictional company called **JH Real Estate** (yes, JH means Joshua Hui!) using **Django**. A **HTML/CSS Bootstrap 4** theme will be used. This is a real working application where the user can register an account, search for a real estate listing base on his/her preference(s) and make an inquiry of the listing; and the admin can manage resources including property listings, realtors and contact inquiries in the admin area.

- [Real Estate App with Django](#real-estate-app-with-django)
- [Languages/ Technologies used](#languages--technologies-used)
- [Demo](#demo)
- [What is Django](#what-is-django)
- [Joshua Hui (JH) Real Estate App Requirements](#joshua-hui--jh--real-estate-app-requirements)
  * [Front-End Pages](#front-end-pages)
  * [Functionality Specifications](#functionality-specifications)
  * [Listing Page Fields](#listing-page-fields)
- [Instructions](#instructions)
  * [Create a new app](#create-a-new-app)
  * [Create Model(s) in the app](#create-model-s--in-the-app)
  * [Add the newly created model into Django Admin](#add-the-newly-created-model-into-django-admin)
- [Useful Links](#useful-links)
  * [Setting Up](#setting-up)
  * [Django Related](#django-related)
  * [pgadmin](#pgadmin)


# Languages/ Technologies used
- Backend
 - Django
 - PostgreSQL
 - Gunicorn
 - Nginx
- Frontend
 - HTML/CSS Bootstrap 4
 - JavaScript
- Deployment Server
 - DigitalOcean


<p align="center">
 <img src="/demo-pics/jhre_home.PNG" width="514" height="545" title="Home Page Picture">
</p>

Feel free to:
- Browse through the web app
- Register and login with your account (or you can test with this account: *joshtest* with password: *20191003*)
- Click into the listing(s) to see more detail(s)
- Make an inquiry in the listing(s)
- Go to the dashboard to see a list of inquiries that you made
- Do property searching
- And more!


# What is Django
- [Django](https://www.djangoproject.com/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- What does high-level mean here? It means you have a really specific way to structure your files and to write the code.
- Django has the idea of a *project* (which is your web site as a whole), and inside that project you have what are called *apps*. Let's say you have a blog in your website, then the blog would be an individual app that has its own model, view, URL and files, etc. So each piece of functionality on the website will be called an app. 




# Joshua Hui (JH) Real Estate App Requirements

## Front-End Pages
- Home
- About
- Listings
- Single Listing
- Search
- Register
- Login
- Dashboard (Inquiries)


## Functionality Specifications
- Manage listings, realtors, contact inquiries and website users via admin
- Role based users (staff and non-staff)
- Display listings in app with pagination
- Ability to set listings to unpublished
- Search listings by keyword (in description), city, state, bedrooms and price (Homepage & search page)
- List realtors on about page with “seller of the month” (Control via admin)
- Listing page should have fields listed below
- Listing page should have 5 images with lightbox
- Lightbox should scroll through images
- Listing page should have a form to submit inquiry for that property listing
- Form info should go to database (and notify realtor(s) with an email, which is a future functionality)
- Frontend register/login to track inquiries
- Both unregistered and registered users can submit form. If registered, can only submit one per listing


## Listing Page Fields
- Title
- Address, city, state, zip
- Price
- Bedrooms
- Bathrooms
- Square Feet
- Lot Size
- Garage
- Listing Date
- Realtor – Name & Image
- Main image and 5 other images


# Instructions
## Create a new app
For example you want to create an app called *contacts*:
1. Start the *contacts* app using the command: `python manage.py startapp contacts`
2. Add `contacts.apps.ContactsConfig` into the `INSTALLED_APPS` section inside **settings.py** within the project folder

## Create Model(s) in the app
For example you want to create a model in the *contacts* app:
1. Go to **models.py** inside the *contacts* folder
2. Create a class that define the model, visit [here](https://docs.djangoproject.com/en/2.2/topics/db/models/) for more
3. Run `python manage.py makemigrations contacts` to create a migration file see [here](https://docs.djangoproject.com/en/2.2/topics/migrations/)
4. Run `python manage.py migrate` to propagate changes you make to your model(s) into your database after the creation of the migration file

## Add the newly created model into Django Admin
- https://docs.djangoproject.com/en/2.2/ref/contrib/admin/


# Useful Links
## Setting Up
- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)
- [How To Set Up a Virtual Environment in Python](https://docs.python.org/3/library/venv.html)
- [How To Install and Use PostgreSQL on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
- [Step by Step Branch and Merge using VS Code](https://github.com/159356-1702-Extramural/capstone/wiki/Step-by-Step-Branch-and-Merge-using-VS-Code)
## Django Related
- [Django - Models](https://docs.djangoproject.com/en/2.2/topics/db/models/)
- [Django Structure](https://www.youtube.com/watch?v=u49eOt8XJA4)
- [Django Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/)
- [Django Cross Site Request Forgery protection](https://docs.djangoproject.com/en/2.2/ref/csrf/)
- [Django Messages Framework](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/)
- [Django Email](https://docs.djangoproject.com/en/2.2/topics/email/)

## pgadmin
pgadmin is very useful for validating the data and understanding the dataset, for more, please visit: https://www.pgadmin.org/

<p align="center">
 <img src="/demo-pics/pgadmin.PNG" width="392" height="685" title="pgadmin">
</p>
