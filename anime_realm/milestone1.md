<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Jay Rajesh Munjapara (jm2527)</td></tr>
<tr><td> <em>Generated: </em> 11/14/2023 12:44:12 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/jm2527" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T00.39.20image.png.webp?alt=media&token=34a237c8-1edc-426a-a944-966cff86f171"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T00.40.19image.png.webp?alt=media&token=8aa25561-66bf-4537-b102-05c7205e809f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password Validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T00.48.06image.png.webp?alt=media&token=5b809292-5efe-4d54-998e-75ac0e617702"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email ID already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T00.46.53image.png.webp?alt=media&token=a5e90d45-6b56-442d-9f90-fe69117b2013"/></td></tr>
<tr><td> <em>Caption:</em> <p>Username already taken<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T00.52.49image.png.webp?alt=media&token=3a9c08eb-3b5c-4a2c-9d73-396cc8e9a4ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid form data before submission<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T00.58.50image.png.webp?alt=media&token=42b5110b-4579-41ef-ab36-71a557042972"/></td></tr>
<tr><td> <em>Caption:</em> <p>from task 1, it shows valid user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/27">https://github.com/jay-munjapara/jm2527-is601-007/pull/27</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><b>Form Handling and Behavior:</b></div><div>- The provided Flask code defines routes for user registration,<br>login, profile management, and logout. It utilizes WTForms for form handling and includes<br>client-side and server-side validation.</div><div><br></div><div><b>Validation Logic:</b></div><div>- Frontend: The validation logic is implemented using WTForms<br>in the HTML templates, ensuring proper input on the client side.</div><div>- Backend: Server-side<br>validation is performed in the Flask routes, checking for duplicate entries and validating<br>passwords during registration and login.</div><div><br></div><div><b>Password Handling:</b></div><div>- During registration, the password is hashed using<br>Flask-Bcrypt's `generate_password_hash` before being stored in the database.</div><div>- During login, the hashed password<br>in the database is compared with the entered password using `check_password_hash` to authenticate<br>the user.</div><div><br></div><div><b>Database Utilization:</b></div><div>- The code interacts with the database using the `DB` class,<br>performing operations such as inserting new user data, querying user information during login,<br>and updating user information during profile changes. The database is utilized for user<br>registration, authentication, and profile management.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T01.09.17image.png.webp?alt=media&token=799aadf7-acd7-4978-95df-5e6aeed51d35"/></td></tr>
<tr><td> <em>Caption:</em> <p>It shows invalid password validation but with correct email ID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T01.11.11image.png.webp?alt=media&token=a3caccbc-44c3-43de-8f11-a00c52c70b54"/></td></tr>
<tr><td> <em>Caption:</em> <p>It Shows invalid user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T01.13.12image.png.webp?alt=media&token=5fd456d2-87db-49fe-a1bc-097d97c2f537"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows valid user login<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/26">https://github.com/jay-munjapara/jm2527-is601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><b>Form Handling and Behavior:</b></div><div>- The provided Flask code defines routes for user registration,<br>login, profile management, and logout. It utilizes WTForms for form handling and includes<br>client-side and server-side validation.</div><div><br></div><div><b>Validation Logic:</b></div><div>- Frontend: The validation logic is implemented using WTForms<br>in the HTML templates, ensuring proper input on the client side.</div><div>- Backend: Server-side<br>validation is performed in the Flask routes, checking for duplicate entries and validating<br>passwords during registration and login.</div><div><br></div><div><b>Password Handling:</b></div><div>- During registration on the login page, the<br>entered password is hashed using Flask-Bcrypt's `generate_password_hash` before being compared with the stored<br>hashed password in the database using `check_password_hash` for user authentication.</div><div><br></div><div><b>Database Utilization:</b></div><div>- The code<br>interacts with the database using the `DB` class, querying user information during login.<br>The database is utilized for user authentication.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T01.17.28image.png.webp?alt=media&token=b7f5b01c-22b1-4e34-bb5b-f48b3947faa1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows valid message when user is logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.00.17image.png.webp?alt=media&token=7fdbee23-e6aa-4186-931c-f7df7845b0a2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows unauthorized access when accessing a login-protected page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/28">https://github.com/jay-munjapara/jm2527-is601-007/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <div><b>Session Logic and Login:</b></div><div><br></div><div>- The Flask session is utilized to store user information,<br>such as the user object serialized as JSON, upon successful login. <br>- This<br>session data is checked to determine user identity and access permissions for login-protected<br>pages. The session is cleared during logout to secure access.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T03.58.28image.png.webp?alt=media&token=b8d4deb9-c626-4293-b610-035ff5bf4238"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows permission denied when accessing a roles/add page<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.05.44image.png.webp?alt=media&token=5e378df1-2dd8-4c2f-8df9-baaa5cf6f658"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows permission denied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.07.32image.png.webp?alt=media&token=39439509-4feb-458e-8d9d-f5bda7cecb00"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows roles/list<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.09.45image.png.webp?alt=media&token=36a3bdee-3be3-494a-ac84-9ecabbbeb763"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin -&gt; jm2527<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.13.00image.png.webp?alt=media&token=c06af11d-6966-4da4-806c-78a0577d0bd3"/></td></tr>
<tr><td> <em>Caption:</em> <p>User&#39;s table<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/28">https://github.com/jay-munjapara/jm2527-is601-007/pull/28</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <div><b>Login-Protected Pages:</b></div><div>- Upon successful login, the user object is stored in the Flask<br>session as JSON. Flask-Login's `login_user` is used to log in the user, and<br>Flask-Principal is informed of the identity change. Access to login-protected pages is then<br>controlled by checking the session for the user's identity.</div><div><br></div><div><b>Session Usage and Helpers:</b></div><div>- The<br>session stores the user object as JSON, and Flask-Principal's `identity_changed` is employed to<br>manage user identity changes. Flask-Login's `login_user` facilitates user login, and access to protected<br>pages is controlled by checking the session for the user's identity.</div><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <div><b>Role-Protected Pages:</b></div><div>- Role-protected pages utilize Flask-Principal to manage user roles. After successful login,<br>roles are queried from the database and assigned to the user object. Flask-Principal's<br>`identity_changed` is used to notify changes in user identity, and access to role-protected<br>pages is controlled by checking the user's roles.</div><div><br></div><div><b>Session Usage and Helpers:</b></div><div>- The session<br>stores the user object as JSON, including role information. Flask-Principal's `identity_changed` is employed<br>to manage identity changes, and access to role-protected pages is controlled by checking<br>the user's roles stored in the session.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.44.24image.png.webp?alt=media&token=81140959-9587-455b-bba4-ed7063665ab1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Shows basic bootstrap css on elements<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/25">https://github.com/jay-munjapara/jm2527-is601-007/pull/25</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p><b>CSS:</b><br>- The code utilizes basic Bootstrap CSS for styling elements such as navigation<br>(<code>nav</code>) and forms. The styling is not explicitly detailed in the provided code<br>snippet, but the use of Flask and the presence of form templates suggests<br>a common choice for Bootstrap styling conventions.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.50.57image.png.webp?alt=media&token=ea8618b2-f1c0-4aaa-ab9f-df407d981d2c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid Password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.52.05image.png.webp?alt=media&token=dce3bba8-af04-4cf6-81a6-eb7807e55a7e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid User<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.53.10image.png.webp?alt=media&token=4104eeda-8e4c-45a1-b648-44bea8b8aa2b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission Denied<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/31">https://github.com/jay-munjapara/jm2527-is601-007/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div>- The code incorporates Flash messages to handle technical notifications and converts them<br>into user-friendly messages. These messages are displayed using the flash function, providing a<br>more user-friendly presentation of potential technical issues or success notifications, making the system<br>more accessible to users.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T04.55.18image.png.webp?alt=media&token=1a647744-1729-4be4-a958-4e962d65fdea"/></td></tr>
<tr><td> <em>Caption:</em> <p>User/profile<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/31">https://github.com/jay-munjapara/jm2527-is601-007/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <ul><br><li>The user data is retrieved from the database during the profile rendering<br>process. The code utilizes the <code>DB</code> class to query the database for the<br>user&#39;s information, and upon a successful retrieval, it populates the form fields with<br>the user&#39;s email and username. The data is then displayed in the form,<br>allowing users to see and potentially update their profile information.<br></li><br></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T05.20.00image.png.webp?alt=media&token=1f56aba1-ad0f-46a7-9e2d-50b2f0a240be"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid user format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T05.20.58image.png.webp?alt=media&token=024d06b0-73a4-4a5c-ad2c-8696af67c754"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email address<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T05.22.31image.png.webp?alt=media&token=7f08fbd6-a6c2-45e3-993d-e5182ce95701"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T05.23.34image.png.webp?alt=media&token=3ebd1315-4130-4f6d-9eb3-0f58473d00e3"/></td></tr>
<tr><td> <em>Caption:</em> <p>password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T05.24.41image.png.webp?alt=media&token=41863ebd-0e1e-43c4-bc7a-1b303453389c"/></td></tr>
<tr><td> <em>Caption:</em> <p>username not available<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T05.34.20image.png.webp?alt=media&token=30f8abdc-94c0-4f73-a8ca-4ede1939bb71"/></td></tr>
<tr><td> <em>Caption:</em> <p>before update<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fjm2527%2F2023-11-14T05.35.17image.png.webp?alt=media&token=c4c3c2e8-7c7b-4f91-a265-ca602a8575ad"/></td></tr>
<tr><td> <em>Caption:</em> <p>after update<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/jay-munjapara/jm2527-is601-007/pull/31">https://github.com/jay-munjapara/jm2527-is601-007/pull/31</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <div><b>Edit Logic for Updating Email, Username, and Password:</b></div><div>- The code employs database queries<br>through the `DB` class to update user information, handling edits for email and<br>username through SQL updates. Password updates involve bcrypt hashing. Server-side validation is implemented<br>to ensure the current password is valid before proceeding with changes.</div><div><br></div><div><b>Validation:</b></div><div>- Server-side validation<br>checks the correctness of the current password before allowing updates to the email,<br>username, and password fields.</div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <p><b>Learnings:</b><br>- My knowledge of Flask has expanded, covering aspects such as SQL queries,<br>authentication procedures for login and registration, role assignments, and insights into deployment practices.<br>This experience has provided a comprehensive understanding of web development using Flask.<br><br><div><div><b>Challenges Faced:</b></div><div>-<br>Initially, I misplaced the venv folder but rectified it. I forgot to create<br>a milestone branch initially, leading to direct merges into the dev branch. Recognizing<br>the error, I later created the milestone1 branch and integrated the necessary branches.<br>Another oversight was including each step-wise branch in every dev.yml file, which was<br>more of a precautionary check during the code review process.</div></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-jm2527-prod-e91d1b5fc033.herokuapp.com/login">https://is601-jm2527-prod-e91d1b5fc033.herokuapp.com/login</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/jm2527" target="_blank">Grading</a></td></tr></table>