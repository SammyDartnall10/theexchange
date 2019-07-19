<h1>The Exchange</h1>

<p>Want to swap some stuff? Look no further 👉 >> (link for deployed app)

The inspiration for this project came from my own conversations with freelancers, and small business owners trying to get their dream off the proverbial ground. 

One common theme would emerge from these conversations is that - as solo entrepreneurs, freelancers and side hustlers, money for setup and launch is fairly small. However, the range of things you can spend this small amount of money on is seemingly endless. No longer do you need a website, you also need SEO, an Instagram and Facebook presence, constant interaction with your hard-earned followers. And it’s not enough to take basic photos of your product - you need a photoshoot, professionally staged, and then someone to edit these photos before they go online. Caterers to feed the attendees at launch parties, staff to help you man the tent when selling at markets or festivals. 
Suddenly - the cost of launching your passion with the impact it deserves is looking more and more unattainable. 
If only we had the budget of large corporates - right? 

Wrong.

What we, small business owners, contractors and entrepreneurs have, is range of products and services we "can offer". 

Our businesses may be in photography, catering, flower arrangement, recruitment, web development. And the multiskilled people we are - our skill sets will often branch out beyond that of our core business. The photographer who can retouch photos in a second in lightroom, the chef who is also a sound business management coach. 

What if we could swap our products and services, in return for those we need? If you've been to a networking evening, you'll be familiar with the format - What’s are you after, what is your "ask"? And what can you "offer" in return?

That is the basis for this app- a place where people can post for the things they need, and what they can swap for it in return. 




<h1>UX</h1>

<p>The following Use Cases summarise the four main groups of users that would use this app (names changed and stock photos used for anonymity purposes)</p> 

<img src="readme_static/Use_Stories_Cropped.jpg">

<p>The functional specifications driven by these use cases are as follows:<p>

- Search for locations by category

- Search for locations by location

- Search for locations by best_for

- Display information of each location :
	* Address
	* Category
	* Amenities (wifi etc)
    * Reviews from other users

- Users can upload a new location record

- Location owners can identify themselves as the owner of that location, and maintain business record information:
    * Business Name
    * Address
    * Email/Contact details
    * Profile/Display photo
    * Offers and sales available for users (BYGOF etc)
    

- Users can edit exising location records by way of adding a review

- If information on a location is incorrect users can edit and update

- To make changes or upload new records users must login - this will provide a means of tracking changes. 


<h3>Wireframes and Functional flows:</h3>

<h4>Desktop:</h4>
<img src="readme_static/Layout.png">

<h4>Mobile:</h4>
<img src="readme_static/Layout_Mobile.png">

<h1>Features</h1>

<p>Features deployed, and to be deployed are summarised in the following table</p>
<img src="readme_static/Deployment.png">

<h2>Existing Features</h2>

<p>All the CRUD (Create, Read, Update and Delete) operations have been fully deployed in the app. </p>
- Anyone can search the main exchange page for listings
    Anyone can search the main business exchange - allowing people that arent yet users to see what listings are available, and incentove signups. Contact details wont be shown - only high level detail (the card) will be seen. Pop up saying - want to get in touch? Sign up here - and redirects to signup page
- Authentication - logging in and logging out to maintain profile and add/edit listings
- E-commerce - one off payment to access the site when registering 
- Forgot Password feature
- When a new user registers, an entry in a Company table is generated.
    Editing company detail has been left until the user has logged in, to reduce the overhead in the sign up form. 

- Users can upload info and edit info on thier own business/Company
- Each User can add thier own listings, also edit listings. 
    Achive option for listings that have been fufilled. 
 

- If logged in, users can see the contact details for Listings and respond to them
- If logged in, users can upvote/like a listing to say “I also want this” - gives the listing a higher placed spot

- Logged in users can leave reviews on other users and give a rating. Overall rating for users displayed on each Companies page.
- Having a high overall rating will rank the users listings higher in the exchange

- Javascript used in pop-up forms/modals for adding reviews (also maybe adding new listings?)

- Bootstrap to ensure usability across devices

<h2>Features Left to Implement (optional)</h2>

- Sending 'karma' to other user as either a thanks, or top make up the difference in a swap. Users can also be given karma in return for products and services - this karma can be used at a later date to make up the difference in exchanges. 

- In-app messaging - at the moment contact is done through providing an email for people to contact. 
- Means for sending propoals - similar to other freelancer sites 
- 


<h1>Technologies Used</h1>

As a Flask application app logic has be written in Python 3. 

HTML, CSS, and JavaScript have be used to enhance the look and feel in the following ways.

Rendering of pages was achieved using a combination of HTML5 and CSS. The Bootstrap 4 framework has been employed to achieve a consistent look and feel across the app and device sizes. 

Javascript, and the JQuery  and ajax frameworks have been used to capture on-click events and modal popups, to enhance user experience and guide usage (prevent accidental deletion of records)

The Alt_Work app is data-driven and relies on a mix of structured and unstructured data. CRUD operations are carried out using NoSQL databse - specifically MongoDB.

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