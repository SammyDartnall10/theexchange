# The Exchange

Want to swap some stuff? Look no further 👉 >> (link for deployed app)

The inspiration for this project came from my own conversations with freelancers, and small business owners trying to get their dream off the proverbial ground. 

One common theme would emerge from these conversations - as solo entrepreneurs, freelancers and side hustlers, money for setup and launch is fairly small. However, the range of things you can spend this small amount of money on is seemingly endless. No longer do you need a website, you also need SEO, an Instagram and Facebook presence, and constant 'real' interaction with your hard-earned followers. It’s not enough to take basic photos of your product - you need a photoshoot, professionally staged, and then someone to edit these photos before they go online. Caterers to feed the attendees at launch parties, staff to help you man the tent when selling at markets or festivals. 
Suddenly - the cost of launching your passion with the impact it deserves is looking more and more unattainable. 
If only we had the budget of large corporates - right? 

Wrong.

What we, small business owners, contractors and entrepreneurs have, is range of products and services we "can offer". 

Our businesses may be in photography, catering, flower arrangement, recruitment, web development. And the multiskilled people we are - our skill sets will often branch out beyond that of our core business. The photographer who can retouch photos in a second in lightroom, the chef who is also a sound business management coach. 

What if we could swap our products and services, in return for those we need? If you've been to a networking evening, you'll be familiar with the format - What are you looking for, what is your "ask"? And what can you "offer" in return?

That is the basis for this app- a place where people can post for the things they need, and what they can swap for it in return. 

 

# UX

The following Use Cases summarise the four main groups of users that would use this app (names changed and stock photos used for anonymity purposes)

<img src="readme_static/Use_Stories_Cropped.jpg">

The functional specifications driven by these use cases are as follows:



### Wireframes and Functional flows:

#### Desktop:
<img src="readme_static/Layout.png">

#### Mobile:
<img src="readme_static/Layout_Mobile.png">

# Technologies Used

As a Django application app logic has be written primarily in Python 3 within the Django framework. 
HTML, CSS, and JavaScript have be used to enhance the look and feel in the following ways.

Rendering of pages was achieved using a combination of HTML5 and CSS. The Bootstrap 4 framework has been employed to achieve a consistent look and feel across the app and device sizes. 

Javascript, and the JQuery  and ajax frameworks have been used to capture on-click events and modal popups, to enhance user experience and guide usage (prevent accidental deletion of records)

TheExchange app is data-driven and relies on a mix of structured and unstructured data. CRUD operations are carried out using a postgres database, provisioned through Heroku. 

Stripe payments are collected upon registering, setup up and managed using the Stripe API. Using the Stripe API in this way ensure the app is compliant with financial and data collection regulations. 

# Features

Features deployed, and to be deployed are summarised in the following table
<img src="readme_static/Deployment.png">

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
- company : company specific information, which is separte to the user registered. For example, registered business address, business contact email.
- landing : index.html - provides options for redirection to registering, login or to find out more about the app(about page)
- listing : models views and forms etc for creating, editing and viewing listings, both individually and as a group. 

#### Design:

*TODO  - database design pdf - data flows*

#### Authentication:
Authentication has been used for two main reasons. One - to make sure that only paid users can acccess the database/exchange, and find benefit in it. Secondly, so that users can maintain the information that is held on themselves personally, their company, and the listings they create and display on behalf of their company

#### User Interaction:
Listings are created using a form - this is (if validated) used to create Listings based on the Listing model in the backend.
When a new user registers, an entry in a Company table is generated.
    Editing company detail via a form has been left until the user has logged in, to reduce the overhead in the sign up form.

#### Stripe Payments :
One off payments are taken at registration - successful payment will grant the user acccess to the site. Stripes test functionality, as detailed below, is used to date - not real live payments.

- Card : 4242 4242 4242 4242
- CVC : 123 (or other 3 digit number)
- Expiry : any date later than the current date. 

#### Structure and Navigation:
A responsive navigation menu is at the top of each page, and makes use of bootstrap functionality. Structured layout uses bootstrap extensively to maintain look and feel - see "Wireframes and Functional flows" under "UX" above 

#### Use of JavaScript:
Javascript has been used in the form of modals - not requiring the user to leave the page to leave a reveiw.
Ajax has been used in the exchange page so that the page does not need to be refreshed upon a user upvoting a listing

#### Documentation:
This README.md file is the means by which the project is explained - how it works and what its value is.

#### Version Control:
GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub.

#### Attribution:
Reuse of code is highlighted in comments, There are two large general instances of reuse of code - this is in the accounts app and the stripe payments. Code for each of these elements was based on a previous Code Institue module - my forked version of which can be found [HERE](https://github.com/SammyDartnall10/PuttingItAllTogether-Ecommerce/tree/master/02-FindingAndPurchasingProducts/08-stripe_javascript)

The above code is in turn based on Djangos [inbuilt authentication mechanisim](https://docs.djangoproject.com/en/2.2/topics/auth/), and [stripes API](https://stripe.com/docs).

#### Deployment:
The app is deployed through Heroku. Within Heroku the app is linked to the GitHub branch, in this case the master. See the "Deployment" section for more detail on how this was carried out 

### Project-specific features (in additon to mandatory features)
- Use of Googles Geocoder and Places API to show location of businesses. As some businesses may be based out of peoples homes, location is based on city, rather than street address to protect privacy. 

- Ranking of listings based on upvotes: 
By ranking the listings, users can see what others are looking for the most, and tailor their own offerings to match

- Search for listings feature :
Based on tags, users can search for listings where others are searching for specific things

- Search for businesses : 
Users can search for other companies based on company name, location or main business type. 

- Users can leave reviews/testimonials on other companies, and a rating out of 5. This rating is dispalyed in the users business profile. Users with a higer overall rating will be displayed higher in searches 

 
## Features Left to Implement (Big grand ideas)

- In-app messaging - at the moment contact is done through providing an email for people to contact. A potential development could be to create a means for users to send messages, live or not within the app, increasing engagement with the app. 

- Standard means for sending propoals - similar to other freelancer sites. Send this to a table, whereit is stored in our database. With this information comparisons on proposals can be made by the user. Once a larger set of data is collected data analysis can also show what products are being swapped for what, which are the most popular products and services are being asked for and offered, among other insights. 

- Sending 'karma' to other user as either a thanks, or in a much later version of the app, to make up the difference in a swap. Users can also be given karma in return for products and services - this karma can be used at a later date to make up the difference in exchanges. 


# Testing

### UX testing (look and feel)
For this project, testing was carried out manually, both in the browser and with Google developer tools to test different screen sizes.


### Code Validity
HTML was validated using the Markup Validation Service provided by The World Wide Web Consortium (W3C): https://validator.w3.org/

CSS was validated using the CSS Validation Service provided by The World Wide Web Consortium (W3C): https://jigsaw.w3.org/css-validator/

Throught development, the 'print()' command was used along with code breaks to understand what my code was doing and help bug fix. 

### Maunal Testing with Users

To make sure each of the CRUD operations could be carried out on different devices and in different combinations, manual testing of adding, editing and deleting records was carried out by myself, and two to others (all the thanks to my boyfriend and sister - credits to be found in more detail below).

The following testing structure was used: 

*TODO: make testing flows*
*TODO: python testing*

### Bugs and Problems
One issue not resolved in the submission for this project is the management of image files. MongoDB is not intended to store image files, so I initially searched for other means to store and access images.
Packages in Node.js, or perhaps online hosting were options, but out of the scope of this particular project. 


# Deployment

GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub.

The site has been deployed using Heroku. The process for deploying to Heroku is as follows: 
- In your Heroku account, create a new app
- Under the setting tab in the app, reveal and change the 'config vars' to IP 0.0.0.0 and PORT 5000. 
- Ensure in your app you have in your app files in GitHub a Procfile with the following: 'web: python app.py', and you project requirements in a requirements.txt file. 
- In Heroku, in your app and under the 'deploy' tab, choose the GitHub deployment method. In the app connected to GitHub section find and select the app you wish to deploy. 
- Choose either automatic or manual deploys. In whichever you choose, select the branch in the GitHub repository you wish to deploy. 


Final deployed site is here: *heroku site*

To run locally, create a new workspace in your local computer. Use $ git clone https://github.com/SammyDartnall10/alt_work.git to create a local copy of the code. 
Install requirements with $ pip3 install -r requirements.txt
Run the app with $ python3 app.py


# Credits

A huge thanks to my sister and boyfriend for helping me in many ways, but especially in helping me extensively test this site, to make sure all operations and key tasks can be carried out easy and correctly.

Thanks also to my mentor Aaron Sinnot for helping me build my understanding of how python, the Django framework and how relational databases work, providing direction and helping to squish those final niggly bugs that evaded me until the end! 

Also, once again, I really cannot emphasise my thanks enough to the code institue tutors for their patience and help over countless hours. Without their direction I would still be half way through this course! 

# Content

Companies, listings and users information in the database are entirely fictional, and made up by either myself or those assisting in testing.

Images were from unsplash.com