<h1>The Exchange</h1>

<p>Want to swap some stuff? Look no further 👉 >> (link for deployed app)

<p>The inspiration for this project came from my own conversations with freelancers, and small business owners trying to get their dream off the proverbial ground. 
</p>
<p>
One common theme would emerge from these conversations - as solo entrepreneurs, freelancers and side hustlers, money for setup and launch is fairly small. However, the range of things you can spend this small amount of money on is seemingly endless. No longer do you need a website, you also need SEO, an Instagram and Facebook presence, and constant 'real' interaction with your hard-earned followers. It’s not enough to take basic photos of your product - you need a photoshoot, professionally staged, and then someone to edit these photos before they go online. Caterers to feed the attendees at launch parties, staff to help you man the tent when selling at markets or festivals. 
Suddenly - the cost of launching your passion with the impact it deserves is looking more and more unattainable. 
If only we had the budget of large corporates - right? 
</p>
<p>
Wrong.
</p>
<p>
What we, small business owners, contractors and entrepreneurs have, is range of products and services we "can offer". 
</p>
<p>
Our businesses may be in photography, catering, flower arrangement, recruitment, web development. And the multiskilled people we are - our skill sets will often branch out beyond that of our core business. The photographer who can retouch photos in a second in lightroom, the chef who is also a sound business management coach. 
</p>
<p>
What if we could swap our products and services, in return for those we need? If you've been to a networking evening, you'll be familiar with the format - What are you looking for, what is your "ask"? And what can you "offer" in return?
</p>
<p>
That is the basis for this app- a place where people can post for the things they need, and what they can swap for it in return. 
</p>
 

<h1>UX</h1>

<p>The following Use Cases summarise the four main groups of users that would use this app (names changed and stock photos used for anonymity purposes)</p> 

<img src="readme_static/Use_Stories_Cropped.jpg">

<p>The functional specifications driven by these use cases are as follows:<p>



-  


<h3>Wireframes and Functional flows:</h3>

<h4>Desktop:</h4>
<img src="readme_static/Layout.png">

<h4>Mobile:</h4>
<img src="readme_static/Layout_Mobile.png">

<h1>Technologies Used</h1>

<p>As a Django application app logic has be written primarily in Python 3 within the Django framework. 
</p>
<p>
HTML, CSS, and JavaScript have be used to enhance the look and feel in the following ways.
</p>
<p>
Rendering of pages was achieved using a combination of HTML5 and CSS. The Bootstrap 4 framework has been employed to achieve a consistent look and feel across the app and device sizes. 
</p>
<p>
Javascript, and the JQuery  and ajax frameworks have been used to capture on-click events and modal popups, to enhance user experience and guide usage (prevent accidental deletion of records)
</p>
<p>
TheExchange app is data-driven and relies on a mix of structured and unstructured data. CRUD operations are carried out using a postgres database, provisioned through Heroku. 
</p>
<p>
Stripe payments are collected upon registering, setup up and managed using the Stripe API. Using the Stripe API in this way ensure the app is compliant with financial and data collection regulations. 
</p>

<h1>Features</h1>

<p>Features deployed, and to be deployed are summarised in the following table</p>
<img src="readme_static/Deployment.png">

<h3>High level project purpose</h3>

<p>This project is a full-stack site based around business logic used to control a centrally-owned dataset - namely - products and services that people are looking for, and able to offer. Authentication mechanisms and paid access to the site's data and other activities are based on this dataset, allowing only registered users to post listings, and find what others are looking for in return.</p> 

<h3>Key Value Add</h3>

<p>By authenticating on the site and paying for some of its services, users can use the site to find other businesses with whom they may swap goods and services, to the benefit and growth of both parties. Before authenticating, the user can find out how this works in the 'about' page.</p>

<p>As access to the exchange, contact users and create listings is dependent on authentication, there is no way for a regular user to bypass the site's mechanisms and derive all of the value available to paid users without paying.</p>
<p>In this way, the site owner is able to make money by providing this access as a set of services to the users. </p>

<h2>Existing Features</h2>

<h3>Mandatory requirements</h3>

<h4>Relational Database:</h4>
<p> A postgres database provisioned through Heroku has been used. Users are able to login in and create, edit and delete data records pertaining to their own accounts - ie they can create and manipulate listings made for their company. </p>

<h4>Multiple Apps:</h4>
<p> Each distinct feature has been split into its own app as follows. This way each element of the website becomes reusable</p>

- about : information about the site itself
- accounts : registration and payments have been combined here, as registration and payment(subscription) occurs at the same time. Contains models for personal information, username, email etc.
- busex : top level settings.py and urls.py
- company : company specific information, which is separte to the user registered. For example, registered business address, business contact email.
- landing : index.html - provides options for redirection to registering, login or to find out more about the app(about page)
- listing : models views and forms etc for creating, editing and viewing listings, both individually and as a group. 

<h4>Design:</h4><p></p>

<h4>Authentication:</h4>
<p>Authentication has been used for two main reasons. One - to make sure that only paid users can acccess the database/exchange, and find benefit in it. Secondly, so that users can maintain the information that is held on themselves personally, their company, and the listings they create and display on behalf of their company</p>

<h4>User Interaction:</h4>
<p>Listings are created using a form - this is (if validated) used to create Listings based on the Listing model in the backend.</p>
<p>When a new user registers, an entry in a Company table is generated.
    Editing company detail via a form has been left until the user has logged in, to reduce the overhead in the sign up form.</p>

<h4>Stripe Payments :</h4>
<p>One off payments are taken at registration - successful payment will grant the user acccess to the site. Stripes test functionality, as detailed below, is used to date - not real live payments.</p>

- Card : 4242 4242 4242 4242
- CVC : 123 (or other 3 digit number)
- Expiry : any date later than the current date. 

<h4>Structure and Navigation:</h4>
<p>A responsive navigation menu is at the top of each page, and makes use of bootstrap functionality. Structured layout uses bootstrap extensively to maintain look and feel - see "Wireframes and Functional flows" under "UX" above </p>

<h4>Use of JavaScript:</h4>
<p>Javascript has been used in the form of modals - not requiring the user to leave the page to leave a reveiw.</p>
<p>Ajax has been used in the exchange page so that the page does not need to be refreshed upon a user upvoting a listing</p>

<h4>Documentation:</h4>
<p>This README.md file is the means by which the project is explained - how it works and what its value is.</p>

<h4>Version Control:</h4>
<p>GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub.</p>

<h4>Attribution:</h4>
<p>Reuse of code is highlighted in comments, There are two large general instances of reuse of code - this is in the accounts app and the stripe payments. Code for each of these elements was based on a previous Code Institue module - my forked version of which can be found  [HERE](https://github.com/SammyDartnall10/PuttingItAllTogether-Ecommerce/tree/master/02-FindingAndPurchasingProducts/08-stripe_javascrip)</p>
<p>The above code is in turn based on Djangos [inbuilt authentication mechanisim](https://docs.djangoproject.com/en/2.2/topics/auth/), and [stripes API](https://stripe.com/docs).</p>

<h4>Deployment:</h4>
<p>The app is deployed through Heroku. Within Heroku the app is linked to the GitHub branch, in this case the master. See the "Deployment" section for more detail on how this was carried out </p>


<h2>Features Left to Implement (optional)</h2>

- Sending 'karma' to other user as either a thanks, or top make up the difference in a swap. Users can also be given karma in return for products and services - this karma can be used at a later date to make up the difference in exchanges. 

- In-app messaging - at the moment contact is done through providing an email for people to contact. 
- Means for sending propoals - similar to other freelancer sites 
- 




<h1>Testing</h1>

<h3>UX testing (look and feel)</h3>
For this project, testing was carried out manually, both in the browser and with Google developer tools to test different screen sizes.


<h3>Code Validity</h3>
HTML was validated using the Markup Validation Service provided by The World Wide Web Consortium (W3C): https://validator.w3.org/

CSS was validated using the CSS Validation Service provided by The World Wide Web Consortium (W3C): https://jigsaw.w3.org/css-validator/

Throught development, the 'print()' command was used along with code breaks to understand what my code was doing and help bug fix. 

<h3>Maunal Testing with Users</h3>

To make sure each of the CRUD operations could be carried out on different devices and in different combinations, manual testing of adding, editing and deleting records was carried out by myself, and two to others (all the thanks to my boyfriend and sister - credits to be found in more detail below).

The following testing structure was used: 

<img src="readme_static/CRops.png">
<img src="readme_static/UDops.png">


<h3>Bugs and Problems</h3>
One issue not resolved in the submission for this project is the management of image files. MongoDB is not intended to store image files, so I initially searched for other means to store and access images.
Packages in Node.js, or perhaps online hosting were options, but out of the scope of this particular project. 


<h1>Deployment</h1>

GitHub has been used throughout this project to maintain version control as feature are added. After adding a new feature, the code is pushed to GitHub.

The site has been deployed using Heroku. The process for deploying to Heroku is as follows: 
- In your Heroku account, create a new app
- Under the setting tab in the app, reveal and change the 'config vars' to IP 0.0.0.0 and PORT 5000. 
- Ensure in your app you have in your app files in GitHub a Procfile with the following: 'web: python app.py', and you project requirements in a requirements.txt file. 
- In Heroku, in your app and under the 'deploy' tab, choose the GitHub deployment method. In the app connected to GitHub section find and select the app you wish to deploy. 
- Choose either automatic or manual deploys. In whichever you choose, select the branch in the GitHub repository you wish to deploy. 


Final deployed site is here: https://alt-working.herokuapp.com/

<p>To run locally, create a new workspace in your local computer. Use $ git clone https://github.com/SammyDartnall10/alt_work.git to create a local copy of the code.</p> 
<p>Install requirements with $ pip3 install -r requirements.txt</p>
<p>Run the app with $ python3 app.py</p>


<h1>Credits</h1>

<p>A huge thanks to my sister and boyfriend for helping me in many ways, but especially in helping me extensively test this site, to make sure all operations and key tasks can be carried out easy and correctly.</p>

<p>Thanks also to my mentors- previous and current - for helping me build my understanding of how python, the Flask framework and NoSQL databases work, providing direction and helping to squish those pesky bugs that keep popping up! </p>

<p>Also, I really cannot emphasise my thanks enough to the code institue tutors for their patience and help over countless hours - the real MVPs!!  </p>

<h1>Content</h1>

<p>Descriptions for each of the locations was found through google searches of locations in the area. </p>

<p>Reviews and information on wifi, plugs, food and bringing pets are entirely fictional, and made up by either myself or those assisting in testing.</p>

<p>An excel spreadsheet was created and then converted to CSV. This CSV file was then converted to JSON, so that location data could be uploaded in one go to MongoDB.</p>

<p>Images were from unsplash.com</p>