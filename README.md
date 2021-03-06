# The Exchange

Want to swap some stuff? Look no further 👉 >> <https://businessexchange.herokuapp.com/>

The inspiration for this project came from my own conversations with freelancers, and small business owners planning on, or in the midst of launching their own businesses. 

One common theme emerged from these conversations - the amount of money small businesses have for initial launch is typically very small. However, the range of things you can spend this small amount of money on is seemingly endless. No longer do you need a website, you also need SEO, an Instagram and Facebook presence, and constant 'real' interaction with your hard-earned followers. It’s not enough to take basic photos of your product - you need a photoshoot, professionally staged, and then someone to edit these photos before they go online. Caterers to feed the attendees at launch parties, staff to help you man the tent when selling at markets or festivals. 
Suddenly - the cost of launching your passion with the impact it deserves is looking more and more unattainable. 
If only we had the budget of large corporates - right? 

Wrong.

What we, small business owners, contractors and freelancers have, is range of products and services we "can offer". 

Our businesses may be in one core area -photography, catering, flower arrangement, recruitment, web development. However, the multiskilled people we are - our skill sets will often branch out beyond that of our core business. The photographer who can retouch photos in a second in lightroom, the chef who is also a sound business management coach. 

What if we could swap our broad range of products and services in return for those we need? If you've been to a networking evening, you'll be familiar with the format - What are you looking for, what is your "ask"? And what can you "offer" in return?

That is the basis for this app- a place where people can post for the things they need, and what they can swap for it in return. 

 

# UX

The following Use Cases summarise the four main groups of users that would use this app (names changed and stock photos used for anonymity purposes)

![UserStories](/media/readme_static/UserStoriesCropped.png)

The functional specifications driven by these use cases are as follows:
- Make listings to detail what you are looking for, and what you can offer in return 
- Search functionality to look for listings you respond to 
- Ability to leave reviews on companies
- Search functionality to look for other companies 
- Ranking of "what’s popular" of all listings


## Wireframes and Functional flows:

## Functional Flows:
![Flow](/media/readme_static/LAYOUT.png)

## Desktop Wireframes:
![WebLayout](/media/readme_static/TheExChange.png)

## Mobile Wireframes:
![Mobile](/media/readme_static/TheExChange_Mobile.png)

# Technologies Used

As a Django application app logic has be written primarily in Python 3 within the Django framework. 
HTML, CSS, and JavaScript have be used to enhance the look and feel in the following ways.

Rendering of pages was achieved using a combination of HTML5 and CSS. The Bootstrap 4 framework has been employed to achieve a consistent look and feel across the app and device sizes. 

JavaScript, and the JQuery  and ajax frameworks have been used to capture on-click events and modal popups, to enhance user experience and guide usage (prevent accidental deletion of records)

TheExchange app is data-driven and relies on a mix of structured and unstructured data. CRUD operations are carried out using a postgres database, provisioned through Heroku. 

Stripe payments are collected upon registering, setup up and managed using the Stripe API. Using the Stripe API in this way ensure the app is compliant with financial and data collection regulations. 

# Features

Features deployed, and to be deployed are summarised in the following table and sections

![Features](/media/readme_static/Features.png)

### High level project purpose

This project is a full-stack site based around business logic used to control a centrally-owned dataset - namely - products and services that people are looking for, and able to offer. Authentication mechanisms and paid access to the site's data and other activities are based on this dataset, allowing only registered users to post listings, and find what others are looking for in return. 

### Key Value Add

By authenticating on the site and paying for some of its services, users can use the site to find other businesses with whom they may swap goods and services, to the benefit and growth of both parties. Before authenticating, the user can find out how this works in the 'about' page.

As access to the exchange, contact users and create listings is dependent on authentication, there is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.
In this way, the site owner is able to make money by providing this access as a set of services to the users. 

## Existing Features

### Mandatory requirements

#### Relational Database:
A postgres database provisioned through Heroku has been used. Users are able to login in and create, edit and delete data records pertaining to their own accounts - ie they can create and manipulate listings made for their company. 

#### Multiple Apps:
Each distinct feature has been split into its own app as follows. This way each element of the website becomes reusable

- about : information about the site itself
- accounts : registration and payments have been combined here, as registration and payment(subscription) occurs at the same time. Contains models for personal information, username, email etc.
- busex : top level settings.py and urls.py
- company : company specific information, which is separate to the user registered. For example, registered business address, business contact email.
- landing : index.html - provides options for redirection to registering, login or to find out more about the app(about page)
- listing : models views and forms etc for creating, editing and viewing listings, both individually and as a group. 

#### Design:

Design of the database is made up of five main tables. 
- Users: Personal details on the user who signed up for the business account. 
- Company: This has been separated out for a number of reasons:
    - To reflect business setup - owners will normally register their business as a separate entity to themselves
    - There are many elements that both people and companies can have, that may differ. For example, address, contact details
    - To allow for scaling of the project, where many unique users may belong to one company.
- Listings: Users can make many listings for goods and services, on behalf of the Company
- Reviews: Many Users can make Many reviews about companies. To ensure a Many to One Relationship, the Review table bridges between Users and Companies. 
- Upvotes: Many Users can make Many upvotes. The Upvotes table collects the upvotes a user has made. The Listing and User models can then pull from this table as needed, eg to count number of listings.

A diagrammatic representation of this schema is below:   
*(Please note, the var/int are not representations of the final model property types - diagram was made to help me visualise and represent relationships between tables)*

![Database](/media/readme_static/DB.png)

#### Authentication:
Authentication has been used for two main reasons. One - to make sure that only paid users can access the database/exchange, and find benefit in it. Secondly, so that users can maintain the information that is held on themselves personally, their company, and the listings they create and display on behalf of their company

#### User Interaction:
Listings are created using a form - this is (if validated) used to create Listings based on the Listing model in the backend.
When a new user registers, an entry in a Company table is generated.
    Editing company detail via a form has been left until the user has logged in, to reduce the overhead in the sign up form.

#### Stripe Payments :
One off payments are taken at registration - successful payment will grant the user access to the site. Stripes test functionality, as detailed below, is used to date - not real live payments.

- Card : 4242 4242 4242 4242
- CVC : 123 (or other 3 digit number)
- Expiry : any date later than the current date. 

#### Structure and Navigation:
A responsive navigation menu is at the top of each page, and makes use of bootstrap functionality. Structured layout uses bootstrap extensively to maintain look and feel - see "Wireframes and Functional flows" under "UX" above 

#### Use of JavaScript:
JavaScript has been used in the form of modals - not requiring the user to leave the page to leave a review.
Ajax has been used in the exchange page so that the page will refresh and update the upvotes count to the correct amount. 
Mouseover events on the index.html page, create interest and engagement

#### Documentation:
This README.md file is the means by which the project is explained - how it works and what its value is.

#### Version Control:
GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub.

#### Attribution:
Reuse of code is highlighted in comments, There are two large general instances of reuse of code - this is in the accounts app and the stripe payments. Code for each of these elements was based on a previous Code Institute module - my forked version of which can be found [HERE](https://github.com/SammyDartnall10/PuttingItAllTogether-Ecommerce/tree/master/02-FindingAndPurchasingProducts/08-stripe_javascript)

The above code is in turn based on Django’s [inbuilt authentication mechanism](https://docs.djangoproject.com/en/2.2/topics/auth/), and [stripes API](https://stripe.com/docs).

#### Deployment:
The app is deployed through Heroku. Within Heroku the app is linked to the GitHub branch, in this case the master. See the "Deployment" section for more detail on how this was carried out 

### Project-specific features (in addition to mandatory features)
- Use of Googles Geocoder and Places API to show location of businesses. As some businesses may be based out of peoples homes, location is based on city, rather than street address to protect privacy. 

- Ranking of listings based on upvotes: 
By ranking the listings, users can see what others are looking for the most, and tailor their own offerings to match

- Search for listings feature :
Based on tags, users can search for listings where others are searching for specific things

- Search for businesses : 
Users can search for other companies based on company name, location or main business type. 

- Users can leave reviews/testimonials on other companies, and a rating out of 5. This rating is displayed in the users business profile. Users with a higher overall rating will be displayed higher in searches 

 
## Features Left to Implement (Big grand ideas)

- In-app messaging - at the moment contact is done through providing an email for people to contact. A potential development could be to create a means for users to send messages, live or not within the app, increasing engagement with the app. 

- Standard means for sending proposals - similar to other freelancer sites. All proposals could be sent to a table, and stored in our database. With this information comparisons on proposals can be made by the user. It could also provide an audit trail, and useful tool for mediating issues between users. Once a larger set of data is collected, data analysis can also show what products are being swapped for what, which are the most popular products and services are being asked for and offered, among other insights. 



# Testing

### UX testing (look and feel)
For this project, testing was carried out manually, both in the browser and with Google developer tools to test different screen sizes.


### Code Validity
HTML was validated using the Mark-up Validation Service provided by The World Wide Web Consortium (W3C): https://validator.w3.org/

CSS was validated using the CSS Validation Service provided by The World Wide Web Consortium (W3C): https://jigsaw.w3.org/css-validator/

Throughout development, the 'print()' and ’console.log()’ commands was used along with code breaks to understand what my code was doing and help bug fix. 

### Manual Testing with Users

To make sure each of the CRUD operations could be carried out on different devices and in different combinations, manual testing of adding, editing and deleting records was carried out by myself, and two to others (all the thanks to my boyfriend and sister - credits to be found in more detail below).

The following testing structure was used: 

![TestingOne](/media/readme_static/ManualTestingOne.png)
![TestingTwo](/media/readme_static/ManualTestingTwo.png)
![TestingThree](/media/readme_static/ManualTestingThree.png)

### Bugs and Problems
One final issue I couldn't work out was how to handle the last step of upvoting. On the initial click the vote will increase or decrease as expected, however, if clicked again nothing happens until you refresh the page.  

Another issue was how to display and rank the listings, based on upvotes (highest to lowest). Initially, I was ranking them based on the upvotes @property (see Listings/models.py), but this would result in duplication of results. As it turns out this is to do with how the database is queried - because the upvotes property is a function, SQL doesn’t quite know what to do with it, and so (as I understand it) kind of loops through it (my huge thanks to my mentor Aaron Sinnott for helping me understand this - I was at a loss as to why that behaviour was occurring till we had our call!). So, even though I now know the cause of the problem, I am still struggling to find a solution to it. I have created a work around for now by creating an integer field (the count field) that increases or decreases when the button clicked/ajax call made. Not as robust as basing ranking on the upvotes property, but works for the purposes of displaying functionality.  


# Deployment

GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub with an appropriate commit message.

To run locally, create a new workspace in your local computer. 

- Use $ git clone https://github.com/SammyDartnall10/alt_work.git to create a local copy of the code. 
- Install requirements with $ pip3 install -r requirements.txt
- This project relies on S3 for image and static file storage, and a postgres database as provisioned for by Heroku. However the Django SQLite will work just as well for local serving.
- This project also uses the Stripe API. To collect payments in a local installation the user must signup for their own Stripe account.
- The env.py file is not pushed to GitHub, therefore for local running you will need to use your own unique variables for the following:
    - Stripe publishable
    - Stripe secret
    - Database URL (if linking to postgres database - otherwise the SQLite will work fine)
    - AWS Access Key Id
    - AWS Secret Access Key
    
- Run the app with $ python3 manage.py $IP:$PORT

The site has been deployed using Heroku. The process for deploying to Heroku is as follows: 
- In your Heroku account, create a new app
- Under the setting tab in the app, reveal and change the 'config vars' to: 
    - IP 0.0.0.0
    - PORT 5000
    - Stripe Publishable (as per your unique settings)
    - Stripe Secret (as per your unique settings)
    - Database URL (as per your unique settings)
    - AWS Access Key Id (as per your unique settings)
    - AWS Secret Access Key (as per your unique settings)
- Ensure you have in your app files in GitHub dependencies in the form of a requirements.txt file, and a Procfile with the following: 
    - release: python manage.py migrate 
    - web: gunicorn busex.wsgi:application
- In Heroku, in your app and under the 'deploy' tab, choose the GitHub deployment method. In the app connected to GitHub section find and select the app you wish to deploy. 
- Choose either automatic or manual deploys. In whichever you choose, select the branch in the GitHub repository you wish to deploy. 


Final deployed site is here: <https://businessexchange.herokuapp.com/>




# Credits

A huge thanks to my sister and boyfriend for helping me in many ways, but especially in helping me extensively test this site, to make sure all operations and key tasks can be carried out easy and correctly.

Thanks also to my mentor Aaron Sinnott for helping me build my understanding of how python, the Django framework and how relational databases work, providing direction and helping to squish those final niggly bugs that evaded me until the end! 

Also, once again, I really cannot emphasise my thanks enough to the Code Institute tutors for their patience and help over countless hours. Without their direction I would still be half way through this course! 

# Content

Companies, listings and users information in the database are entirely fictional, and made up by either myself or those assisting in testing.

Images were from unsplash.com

