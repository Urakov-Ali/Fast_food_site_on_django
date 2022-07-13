# Fast_food_site_on_django

Website works on sqlite3 database structure.

The website has 2 models
1: For accounts
2: For products

The Feane fast food site has 6 pages:
1. About page - Here the user can take an information about the company

2. Add food page - Here the user can add the food through the site (without entering to the admin page)
! Important: in order to add the product to the site you must insert the url "http://127.0.0.1:8000/addfood/"

3. Base.html page is made in order to seperate header and footer section from the page, if any edition is needed to make in the header or footer section, then the it is not needed to repeat same work at every pages, it can be done easily  at one "base.html" page

4.Book page - Here the user can book any product he/she needs. The client can use it page as claim sending page. The client fills [name/number/email/and message fields, after all [send] button will be pressed, so the message is sent through telegram bot to the admin of the website. 
!Important: to activate this option inter to the my_app/test.py and enter the bot's token and the admin's private chat_id. 
+additional:(@myidbot - private chat id can be known by this bot)

5.Menu page - Here can be found the next page and the previous page buttons. Suggested products from the menu can be seen comfortly.

6.sign_up page - The registration system page is done in order to create a private profile for the clients. After the registration here on the right top corner, user's nick-name will appear on the place of sign_up and sign_in button. In order to leave his/her profile the client can log_out easily.
