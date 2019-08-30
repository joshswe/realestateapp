# Real Estate App with Django
In this project, we are going to build a real estate application for a fictional company called **JH Real Estate** (yes, JH means Joshua Hui!) using **Django**. A **HTML/CSS Bootstrap 4** theme will be used. This is a real working application with an admin area to manage resources including property listings, realtors and contact inquiries.


# Languages/ Technologies used
- Python 
- Django
- HTML/ CSS
- JavaScript
- (PostgreSQL)[https://www.postgresql.org/]
- Gunicorn
- Nginx

# What is Django
- (Django)[[https://www.djangoproject.com/] is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
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
- Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
- List realtors on about page with “seller of the month” (Control via admin)
- Listing page should have fields listed below
- Listing page should have 5 images with lightbox
- Lightbox should scroll through images
- Listing page should have a form to submit inquiry for that property listing
- Form info should go to database and notify realtor(s) with an email
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

# Useful Links
- (How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 18.04)[https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04]
- (How To Set Up a Virtual Environment in Python)[https://docs.python.org/3/library/venv.html]
- (How To Install and Use PostgreSQL on Ubuntu 18.04)[https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04]
- (Django - Models)[https://docs.djangoproject.com/en/2.2/topics/db/models/]
- 	