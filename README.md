# 📜Blog Site using Flask & Jinja of Python

🌟Previously in Part 1 (https://github.com/bellaryyash23/Blog_Flask_Jinja_1) added the basic HTML, CSS & templating using Jinja for website and Flask server
setup to run and test the website.

🌟Upgraded the Blog site with inclusion of Bootstrap & Bootstrap templating to the features like: 1. Multi-page website with an interactive navigation bar. 2. 
Dynamically generated blog post pages with full screen titles. 3. Fully mobile responsive with an adaptive navigation bar.

🌟With this upgradation in frontend, in the backend the implementation of HTML forms in Flask is done. Thus, the form on Contact page is made responsive 
i.e submitting HTML forms and catching the submitted data in our Flask server.

👉Jinja Templates is used to make it easier to create HTML pages by templating. Instead of re-writing the same header/navigation bar/footer just 
created a header and footer template which can then be applied to all web pages in the website. This is done using the '{% include %}' method.

👉Thus, the navigation bar is designed using Bootstrap and is templated to all waebpages of the website using Jinja. Also, two new routes 'contact' & 'about' and 
respective pages are added to the navbar and to the website.

👉Now, the design templates with static images, Full screen titles, and updated fonts are added to each webpage. 

👉On the home page, from previous day we had added the functionality to GET all posts from a API response and render them on the page. This is implemented here and 
the final design template of home page look like this:

![Home Page of Blogsite](https://github.com/bellaryyash23/Blog_Flask_Jinja_2/blob/master/samples/home.jpg?raw=true)

👆Home Page of Blogsite with new template design👆

👉We had also added Dynamic generation of blog post using Jinja '.url_for()' method with blog_id passed as parameter. These dynamically generted post pages also are designed
with bootstrap templates.

![Single Post Page of Blogsite](https://github.com/bellaryyash23/Blog_Flask_Jinja_2/blob/master/samples/post.jpg?raw=true)

👆Single Post Page of Blogsite with template design👆

👉The About Page is also made to render using Jinja templating and other Boootstrap features. 

![About Page of Blogsite](https://github.com/bellaryyash23/Blog_Flask_Jinja_2/blob/master/samples/about.jpg?raw=true)

👆About Page of Blogsite with template design👆

👉The Contact page is also designed with the same templating. In the Contact page, a HTML form is also created which visitors can use to send their feedback to owner of
blog site.

![Contact Page of Blogsite](https://github.com/bellaryyash23/Blog_Flask_Jinja_2/blob/master/samples/contact.jpg?raw=true)

👆Contact Page of Blogsite with template design👆

👉Now, this HTML form present in Contact page is made to work using Flask form methods. Using the Flask decorator functions the GET and POST action and respective method
call are setup in the HTML file using Jinja and the Flask method 'request' which allows us to tap into the parameters of the request that was made to the server.

👉Also using 'request.method' we can come to know wheather GET or POST request was made and subsequently load the form method for those actions.

👉Thus, on POST method call of form, the parameters get passed to Flask server which, get caught using name tag of HTML form input and request method of server.
We can then use the SMTP module to send this message to the blog site's owner with the values of name, email, message of the visitor passed in the body of the mail.

![Sample Mail received from Form](https://github.com/bellaryyash23/Blog_Flask_Jinja_2/blob/master/samples/mail.jpg?raw=true)

👆Sample Mail received from Form👆

👉In this way the form is made to work and data is collected in the Flask server.

👉Thus, a fully working and Mobile responsive website is created successfully.

![Blog Website Responsive Working](https://github.com/bellaryyash23/Blog_Flask_Jinja_2/blob/master/samples/site.gif?raw=true)

👆Blog Website Responsive Working👆
