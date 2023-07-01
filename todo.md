 * MVC (Under Flask + MySQL)
 - getListingByID 'title' to 'ListingData'
 * error page for when user attempts to access userid URL that doesn't exist
 - style things
 * page for viewing listing (no need anymore)
 * delete button if listing is by user
 * logout button
 * background image
 * login errors ex: email or password invalid
 * logged in cookie
 * encrypt/decrypt password
 - ability to click on user to get contact info
 - move usermaps add to JSON functions to dbtalk and call dbtalk in usermaps
 - implement check for if userID exists and assign new userID when creating new account
 * assign images to listings in DB
 * group link to users in DB
 * upload listing images
 - delete groups
 * join groups
 * create groups
 * group pin
 * change group pin
 * show group pin
 * delete photos
 - delete photos assosiated with deleted listing
 * photos need PhotoID in DB
 - userColor, generate based on letters in name
 - dropdown menu for which group to add listing on New Listing page
 - encrypt cookies for security?
 - convert description input to HTML via markdown
 - newListing: append listing ID to selected group in DB
 - all pin inputs set from textbox to password type
 - listing tags
 - sort by tags
 - calendar view or date range

 - create base application package and start testing for errors (db.json starts empty but with Users, Listings, Groups, etc)
 - publish official release on Github
 - db clean function (primarily for images after listing has been deleted)
 - 'New Listing' needs validation for being part of a group

errors:
  [x] listings will not display until group select is changed
    - user can not see listings unless part of two groups
    - fix: run 'updateGroupSelect' if 'session['GroupIDSel']' is -1
  [] when user is already part of a group, they may add multiple of the same userIDs to a group by joining the group again. Deleting the user from that group will then not work
  [] webpage breaks when listing has no images (all new listings)
  



 notes:
  - add images to database by getting file name from html then prefacing with "../static/images/"
    - use existing database insert functionality


 Environment Commands:
 - python -v
 - pip install pipenv
 - pipenv install flask
 - pip list
 - pipenv shell
 - python server.py
 - pip install flask-bcrypt


 https://www.w3schools.com/howto/howto_js_lightbox.asp