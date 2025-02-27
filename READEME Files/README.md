# The On Call Musician

### Milestone Project Four
Over the past few years, it has become necessary for businesses to become more digital when it comes to not only marketing, but 
in content too.  Companies are having to re-brand at least once a year to keep up with the ever changing lanscape, and find more creative ways to be seen by the public,
including, video content and podcasting.

Music is a massive part of this.  Why trawl around trying to find someone every year to write a new jingle or backing music?  This is time consuming and very
expensive.

I have developed The On Call Musician for just this purpose!

It is a simple lifetime subscription service, which allows anyone, from hobbyist to film and TV studios, to have access to their own personal musician and original music,
when they need it, without the hassle.

## Demo
The live site can be viewed here - [The On Call Musician](https://on-call-musician.herokuapp.com/).

GitHub repository can be viewed here - [Hunnser86/On-call-musician](https://github.com/Hunnser86/On-call-musician).

![Site Mockup](/media/site-mockup.png)

## UX
### Strategy
The aim is to create a user-friendly subscription service based around controlling a centrally owned dataset, which I will be building. As an subscription service, the site will be based around the business logic of being able to browse and select items to buy then finally completing the transaction and taking a payment.

Users should be able to view the services both individually and collectively. They should be shown in an appropriate and clear way. Items will be able to be added and removed from a shopping cart and then finally paid for. Any user should be able to complete a transaction easily on The On Call Musician, but users will be encouraged to register in order to have access to their own profile where order history is stored and default billing information can be saved. The ability to use a music library will also only be given to registered users as well as the ability to email us a request for original music. In addition to all this the site owner (admin) should be able to add, edit and remove services conveniently from the frontend.

### User Stories
As a customer I'd like to:
* View a selection of services and select the one I wish to purchase.
* Look at individual service details in order to consolidate my decision on whether to purchase the item or not.
* Add items to the cart to purchase at a later point.
* Easily view the carts contents.
* Be given the ability to remove items completely.
* Checkout, pay and complete my order easily.
* Have order confirmation once my order has been completed.
* Navigate around the site easily and the site to be user friendly.
* Receive feedback whilst interacting with the site.
* Do all of the above regardless of what device I’m using.

As a returning user I'd like:
* To sign up and register for an account easily. 
* To login and logout easily.
* To receive email confirmation of registration and have the ability to recover forgotten passwords.
* To login and logout easily.
* A personalised user profile where I can see my order history and set my default billing information if desired.
* The ability to browse and download songs from a music library.

As the site owner / admin I want:
* The ability to add new products to the store.
* To be able to edit and remove products from the store.

### Scope
* The site must have a section where all products are displayed, for all users to see.
    * All products shown will have to be done so in a visually appealing manner.
    * Each card should act as a link to its own page.
* Individual service pages will follow a template, which will be populated from the database.
    * All information on this page should be clear and presented in a visually appealing manner.
* Items must be able to be added to a cart. The items in the cart can be removable.
* A user must be able to complete the checkout process easily from cart through to order completion.
    * Methods of data input must be clear and inputted data must get validated.
    * The site will need to relay information back to the user when required or when suitable and do so in an appropriate manner.
    * A payment and the order must be taken.
* Allow users to login, logout and register.
    * Restrictions will need to be placed on what unregistered users can see and use.
* Access to a personalised profile page that shows order history (registered user only).
* A music library will also be made available to registered customers.
* CRUD functionality for services (admin only).
* We want the user to remain engaged throughout use so the site must be user-friendly and easy to navigate around.
* Function as expected:
    * Fully responsive on all devices.
    * Links or buttons take you to the expected place or complete the expected task.
    * External links must open in new windows.

### Structure
Based on the information gathered so far the structure of The On Call Musician will be:
* Fixed navigation bar at the top of every page. This will show the business name and links to other pages on the site. 
* A home page with a hero image and a call-to-action button directing the user to the services page.  Unregistered customers will see a register now button instead.
* Django allauth will handle the log in/ log out and registration processes.
* Services page where product cards are displayed.
    * Each card will link to the service detail page, where further information is shown.
    * Users will be able to add an item to their carts.
    * Registered users can download a song from the music library.
* Individual service pages will show an image along with further information about the product.
    * Users will be able to add the item to their carts.
    * Admin will be able edit and delete the product from this page.
* The cart page will show what item the user has added to their cart, the details of the product in the cart, the quantity and the subtotal of each item. This page will be the start of the checkout process so a link to checkout will be available here also.
* Checkout page where the users personal information, delivery address along with their payment details are taken to be processed.
* Checkout success page confirms the order and payment has been taken and authorised.
* The user profile page will be created for all registered users and tailored to them. It will show their order history along with the ability to edit / add their default delivery information via a form.
* A music library, where users can download songs from a privately shared soundcloud account.
    * Only available to registered users.
* Add service form will be accessible by admin only. This form will input the supplied data into the database and the service.
* Edit service form will be accessible by admin only. The form will be pre-populated with the existing data and any changes made will then overwrite / remove existing data. 


### Surface
The On Call Musician is built using Bootstraps grid system. I’ve used a combination of containers, rows and columns along with the built in flexbox capabilities to position content as well as making each page responsive at all breakpoints. Another positive to using this grid system is that it’s allowed me to keep the layout of pages consistent throughout.

Pages have a similar layout of page title followed by its content. The Service page contains a lot of information so in order not to overpower the user with a lot of information at once, products are displayed via cards. These cards show all the information about the service and link to the individual product page. Where the use of cards wasn’t applicable (such as the individual product pages and pages that feature forms) I broke information up by using block colour and columns. Doing so ties in with the overall aesthetic of the site, adds some space between information and forms where appropriate whilst remaining visually appealing and responsive.

I found a suitable colour palette using [Adobe Color Wheel](https://color.adobe.com/create/color-wheel). The scheme is a combination of a dark blue (rgb(1, 9, 82)) and Light Blue (#17a2b8) that work well together, work well with white text and gives the site the professional, modern aesthetic I was after. I decided that buttons for adding, updating and checking out were to use The dedault black and white, as I felt they stood out in contrast against the blue overlay. For delete functions I used Bootstraps danger class for the same reasoning. Howerver, on other pages like loggin in and registering, I chose to use the warning class for functions, as it really stood out against the blue compared to the original blue colour. The Google font Poppins is used throughout.


## Features
### Page layout
* Responsive at all breakpoints. By using a combination of media queries, Bootstrap’s responsive grid and built in flexbox capabilities means the sites layout remains consistent while the content adapts to the device it’s being viewed on.

### Navigational
* A fixed navigation bar means that links to any other section of the website are accessible at any point making for easier navigation.
* The logo has a secondary feature as a link back to the home page. All other links are where a user would expect to find them making for good UX.
* The menu button on smaller screen widths features Font Awesome’s icon “fa-bars”, which is associated with this dropdown menu function.
* The Grand total (if any) in a customer’s cart is displayed as a counter on the cart icon. 

### Buttons and links
* Call-to-action buttons are used throughout the site to engage with the user and point them to relevant pages of the site or to perform certain tasks.
* Buttons will invert colour when hovered showing the user it is clickable in order to get them to engage with them.
* All buttons are clear and obvious in what they do and function as expected.
* The buttons used in the Boutique Ado tutorial to add a quantity to the cart are removed, but the functionality remains to allow the user to add just one service to their account at a time, allowing them to add another at a later date.

### Toasts, modals and error pages
* Toasts are used throughout to relay information back to the user. These could be anything from welcoming a user when logging in, telling them their cart has been amended or confirming their purchase.
* The toasts also enhance UI by providing a customer a preview of their cart, telling them how much they have spent and which service they have selected.
* Deletion of anything on the site is a 2 step process with admin having to confirm they wish to delete an object via a modal so accidental deletions can't happen.

### Home
* A hero image fills the majority of the page when it first loads. I’ve used a hero image as I believe it sets the tone by giving a professional and modern feel.
* A call-to-action button aimed at directing traffic towards the Services page is layered over this image.

### Services, service pages and music library.
* Services are shown as cards. I felt this was the best way to display this amount of information without overwhelming a user. 
* Individual service pages show all the information the cards do, except it is laid out in a side by side fashion.

### The checkout process
* Items can be removed from the cart by using the remove button.
* All information in the cart, checkout and checkout confirmation pages is shown in intuitive way prioritising information that is most important.
* Totals are shown in a clear and obvious manner; these are updated as the cart gets amended.
* On the checkout page we get a summary of all the items we’re about to purchase. A call-to-action button is placed underneath this in case of any last minute revisions.
* The checkout form gets pre-populated if default information has been saved to the user’s profile. This will speed up the checkout process for returning users.
* The option to change this information is given when checking out a new order. The customer has the option to override existing information by ticking the checkbox on the form.
* When the order is placed an overlay appears on the screen to indicate that the order is being processed. Not only does this show that something is happening but stops the user from altering the form whilst it’s being processed. It also makes the transaction and site look professional. 
* An email confirmation of an order is sent to the email address given at the time of order, so the user has receipt of the purchase and a record of the information given.

### Music Library
* All songs are set out using the grid system and taking advantage of the soundcloud embed iframes.
* Each frame contains the title, a download button and some artwork.

### Profile
* Every user is assigned a profile page on registration.
* Order history will appear on this page. From here a user will be able to access any old order confirmation that was generated at the time of order by clicking the order number as it acts a link.
* To speed up the checkout process for returning customers a default billing address can be added via a form here. This will pre-populate the checkout form with the default address when buying goods.

### Adding, editing and removing
* Only admin can add, edit and delete services.
* Inputs on forms are labelled and have placeholders so it’s clear what goes into each field.
* Some fields are required in order to submit a form, validation messages will appear to help with input if needed.
* Inputted data is validated so forms will only accept data how we’d like it. The better the data inputted into the database the better the end result will be when it’s displayed throughout the site.

### Features left to implement
* I would like to implement an overlay on the service page, on the card image of the service a customer has already bought, just to stop them accidentally making a double purchase ( they can always but more than one on purpose of course ). I would also like to implement a music player for the library, instead of embedding code from another site, as this would then mean everything is taken care of and owned by the site owner. This would also include using Filefields in a "Song" model, musch like the services.

## Database

![Database schema](/media/database_schema.png)

## Technologies
### Languages:
* HTML.
* CSS.
* JavaScript.
* Python.

### Databases:
* SQLite – Development database provided by Django.
* PostgreSQL – Production database provided via Heroku.

### Frameworks, libraries and tools:
* Django. Python web framework with external libraries.
    * External libraries are visible in the requirements.txt file.
* [jQuery.](https://jquery.com/) JavaScript library.
* Gitpod (IDE).
* Git and GitHub. Used for version control and hosting my repository.
* [Heroku.](https://heroku.com/) Used to host my site.
* [AWS S3 Bucket.](https://aws.amazon.com/) Cloud storage for media and static files used by Heroku.
* [Stripe.](https://stripe.com/gb) Online payment processing for internet businesses used to receive payments.
* [Gmail.](https://en.wikipedia.org/wiki/Gmail) I've hooked my deployed site up to Gmail's smtp server in order to send emails. 
* [Font Awesome.](https://fontawesome.com/) Adds icons throughout the site to increase UX.
* [Bootstrap.](https://getbootstrap.com/) Grid layout, responsive design and basic styling.
* [Google fonts.](https://fonts.google.com/specimen/Poppins) Poppins was imported and used throughout.
* [RandomKeygen.](https://randomkeygen.com/) Secure password and keygen generator used for secret key.
* W3C [HTML](https://validator.w3.org/) & [CSS](https://jigsaw.w3.org/css-validator/) validators.
* [JSHint.](https://jshint.com/) JavaScript validator.
* [PEP8 online.](http://pep8online.com/) Checks python code meets PEP8 requirements.

## Testing
Separate testing document can be found here - [testing documentation.](/READEME%20Files/TESTING.md)

## Deployment
### Heroku deployment
This project is hosted by Heroku but is still deployed from the master branch of a GitHub repository. The following steps were taken to deploy this project to Heroku:
1. Went to [Heroku](https://heroku.com/) and logged in.
2. Created a new app by clicking **create new app** from the drop down menu labelled "new".
3. Gave my app a name and selected the region from the dropdown menu that was closest geographically. 
4. Clicked the **create app** button where I was directed to the dashboard for the new app.
5. Clicked on the **resources** tab on the dashboard. Added Heroku Postgres to the app by searching and then selecting it. I then selected the Hobby Dev – Free plan.
6. I populated my database with a fixtures file containing one json file containing the services.
7. Installed dj_database_url and psycopg2-binary using `pip3 install`.
8. In `settings.py` I imported dj_database_url at the top of the file.
9. Then replaced the default `DATABASE` setting with:
```
DATABASES = {
        'default': dj_database_url.parse(<DATABASE_URL>)
    }
```
The `<DATABASE_URL>` is found in the Heroku apps **Config Vars**. It's important that you don't commit this url into version control!

10. I ran migrations using `python3 manage.py migrate` to create the models in the new database.
11. I now used the json file in step 6 to populate the new database.
    * `python3 manage.py loaddata services.json`
12. Then I created a new superuser, this was done by using `python3 manage.py createsuperuser` and then following the instructions shown in the terminal.
13. Installed gunicorn using `pip3 install`.
14. Used `pip3 freeze > requirements.txt`, this stores all our apps requirements.
15. Created a Procfile and populated it with:
```
web: gunicorn <app_name>.wsgi:application
```
16. I logged into Heroku but this time via the terminal using `heroku login -i`.
17. Then I used `heroku config:set COLLECTSTATIC=1 --app <app_name>` to disable static files from being collected. This is only a temporary measure.
18. Added the hostname of the Heroku app to `ALLOWED_HOSTS` in `settings.py`
```
ALLOWED_HOSTS = ['<hostname>', 'localhost']
```
19. Returned to the Heroku dashboard, clicked on the **deploy** tab, scrolled down to the “Deployment method” section and clicked the **connect to GitHub** button. 
20. I searched for my repository in the “Connect to GitHub” section, found it and clicked **connect**.
21. I then enabled **Automatic Deploys**.
22. At the top of the dashboard I selected the **settings** tab. Scrolled down to the **Config Vars** section and populated the section with the key value pairs of the following:
    * AWS_ACCESS_KEY_ID - I get this when I set up AWS.
    * AWS_SECRET_ACCESS_KEY - I get this when I set up AWS.
    * DATABASE_URL - Prepopulated.
    * DISABLE_COLLECTSTATIC - Created this during step 17.
    * SECRET_KEY
    * STRIPE_PUBLIC_KEY
    * STRIPE_SECRET_KEY
    * STRIPE_WH_SECRET
    * USE_AWS - True
23. I changed the default `DATABASE` setting we created in step 9 in `settings.py` so that it now retrieves the value from Heroku:
```
DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
```
24. Added, committed and pushed all files via the terminal.
25. Heroku is now set up and the app visible. It will automatically update whenever commits are pushed to Github via the IDE.

<details>
<summary>Setting up S3</summary>

1. Create an [AWS](https://aws.amazon.com/) account.
2. Navigate to the management console, search for "S3" to be taken to the S3 dashboard.
3. Click **create bucket** button.
    * Give it a name and select the region closest to you.
    * Allow public access.
4. In the bucket's properties select **static website hosting**.
    * Select "use this bucket to host a website".
    * Give it the default values of `index.html` and `error.html` then save.
5. For the buckets permissions CORS configuration use:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
6. For the buckets permissions policy:
    * Copy the Amazon resource name (ARN) from the top of the page.
    * Click "policy generator".
    * Select type of policy as "S3 Bucket Policy".
    * Allow all principals by using `*`.
    * Set action to "GetObject".
    * Paste in the ARN.
    * Click **Add statement**. Then **Generate policy** and copy the json file shown.
    * Paste this json file to bucket policy.
        * Add `/*` at the end of the 'Resource' key.
    * Save.
7. For the access control list:
    * Set list objects to everyone.
</details>

<details>
<summary>Setting up IAM (Identity and Access Management)</summary>

1. From the AWS management console, search for "IAM" to be taken to the IAM dashboard.
2. Creating a group:
    * Select "Groups" from the menu.
    * Click the **Create new group** button.
    * Name the group.
3. Creating a policy:
    * Select "Policies" from the menu.
    * Click the **Create policy** button.
    * Select the **JSON** tab and click the "import managed policy" link.
        * Find and import **Amazon S3 Full Access**.
    * In the 'Resource' key of the json code shown paste in the ARN from the bucket policy twice forming a list.
        * Add `/*` to the end of one.
    * Review the policy and give it a name and a description.
    * **Create policy**.
4. Attaching the policy to the group:
    * Select "Groups" from the menu and select the group created in step 2.
    * Click the **Attach policy** button.
    * Select the policy created in step 3.
    * **Attach policy**.
5. Creating a user:
    * Select "Users" from the menu.
    * Click the **Add user** button.
    * Create a user by giving them a name.
    * Grant the programatic access and click **Next**.
    * Select the group shown that has the policy attached.
    * **Create user**.
6. Download the .csv file.
</details>

<details>
<summary>Connect Django to S3</summary>

1. Install boto3 by using `pip3 install boto3`.
2. Install django-storages by using `pip3 install django-storages`.
3. Run `pip3 freeze > requirements.txt`.
4. Add 'storages' to the apps list in `settings.py`.
5. Add the values of AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY to **Config Vars** in Heroku.
    * These values are in the downloaded .csv file.
6. Delete the DISABLE_COLLECTSTATIC variable.
7. Create a file called `custom_storages.py` and populate it like so:
```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
8. Add the following to `settings.py`.
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = '<aws_bucket_name>'
    AWS_S3_REGION_NAME = '<aws_region>'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
9. Add, commit and push all via the terminal.
</details>

<details>
<summary>Adding and committing files</summary>

I’ve been using Gitpod to write my code and using the terminal to add, commit and push code from my workspace to GitHub where it is stored remotely as shown in the course content.
1. Typing `git add` into the terminal will move files to the staging area. You should normally do this once a couple of minor additions or changes have been made or one large change or addition has been made. `git add .` will add all files that have been modified, the full stop here means all. If I want to be more selective I can type in the file name e.g. index.html or the files pathway e.g. assets/css/style.css instead of the full stop e.g. `git add index.html`.
2. To send these changes to the local repository we use `git commit`. Normally you'll want to include a brief description of these changes so instead use `git commit –m “ ”`. Between the “ ” write a clear, concise message detailing what this commit has done.
3. To view the changes on Heroku or when you want to send your work to the remote repository (GitHub in this instance) then use the `git push` command. This pushes all the previous commits made to the remote repository. While deploying to Heroku we set it so it'll automatically pick up any changes pushed to our GitHub repository and once Heroku has finished building (this takes a couple of mins) it'll display the most up to date version of the site.
</details>

### Cloning
You can clone a repository so that it can be worked on locally in an IDE such as VSCode by following these steps:
1. Log in to GitHub and navigate to the repository you wish to clone.
2. Click the button that reads **code**. This button is situated to the left of the green Gitpod button near the top of the page.
3. To clone the repository using HTTPS, copy the link shown whilst HTTPS is selected. The link will look something like this: `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`
4. Open your local IDE and in the terminal navigate to the working directory of where you wish to insert the cloned directory.
5. Type `git clone` followed by the link you copied in step 3 into the terminal, this will look something like this: `git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`
6. Press **enter** and the clone will be created in your selected / current working directory (cwd).
7. A new `env.py` file will have to be created to include all the environment variables used throughout and should look like below.
    * Both STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY can be found on the **Developers** dashboard once logged into Stripe.
    * The STRIPE_WH_SECRET can be found once a new endpoint has been created in **Developers** > **Webooks**.
        1. Click on the 'Add endpoint' button.
        2. Enter the URL of your localhost followed by `/checkout/wh/` as your endpoint URL.
        3. Select all events to listen to and click on the 'Add endpoint' button.
        4. The value for STRIPE_WH_SECRET can now be found by clicking the 'reveal' link under the signing secret tab on the webhook's dashboard.
    * Add `env.py` to the .gitignore file so it doesn’t get published in version control.
```
import os

os.environ.setdefault(“SECRET_KEY”,  “<secret key>”)
os.environ.setdefault(“DEVELOPMENT”, “True”)
os.environ.setdefault(“STRIPE_PUBLIC_KEY”, “<key from stripe developers dashboard>”)
os.environ.setdefault(“STRIPE_SECRET_KEY”, “<key from stripe developers dashboard>”)
os.environ.setdefault(“STRIPE_WH_SECRET”, “<key from individual webhook>”)
```
8. You will need to reinstall all the dependencies used, you can do this by running the following `pip3 install -r requirements.txt` in the terminal.
9. You will then need to migrate the database by typing `python3 manage.py migrate` in the terminal.
10.	A new superuser will now need to be created, this can be done by typing `python3 manage.py createsuperuser` in the terminal and following the instructions shown.
11. The site is now cloned… Use the command `python3 manage.py runserver` to run it.

## Credits
### Code
* I used the Boutique Ado e-commerce store project that is part of the course content as a guide as I built my site. Many of the apps, models and functionality’s have been taken from this walkthrough and adapted to suit my needs.
* I used the following documentation throughout:
    * [Django docs.](https://docs.djangoproject.com/en/3.2/)
    * [Allauth docs.](https://django-allauth.readthedocs.io/en/latest/index.html)
    * [Stripe - accepting a payment docs.](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=elements#web-collect-payment-details)
    * [jQuery docs.](https://api.jquery.com/)
    * [Crispy forms docs.](https://django-crispy-forms.readthedocs.io/en/latest/index.html)
* [W3schools,](https://www.w3schools.com/) [Stack Overflow](https://stackoverflow.com/) & [MDN.](https://developer.mozilla.org/en-US/) For general coding problem solving.


### Acknowledgements
* My mentor Brian Macharia for all the feedback and aiding in the planning and execution of this site.
* Tutor support at Code Institute for their help and support when needed most.
* README examples:
    * [Taikatta.](https://github.com/taikatta/Mileston4-EggSellNT)
    * [Samathaluca.](https://github.com/samathaluca/new-lazycamp)

### Disclaimer
This site has been created purely for educational purposes.