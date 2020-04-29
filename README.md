## Quick Tutor App

### How to Use the App

This web application allows students to get help by requesting for tutors. Essentially, this is Uber but for tutors. A user can have both a tutor and student profile. The following is a basic process of how to use the app:

1. Sign in with a Google account
2. Sign up by creating whichever account you would like (student, tutor, or both):
    - If you are a **student**, request tutors using the home page. On the home page, you will see markers indicating active tutors. Check out their profiles and request those you want. Check on the status of your requests on the **Requests** tab. Rate tutors by closing accepted requests. 
    - If you are a **tutor** and ready to start tutoring, set yourself as an active tutor after adjusting the marker to your location and pushing the "I'm ready to tutor!" button. Look at student requests on the **Requests** tab and accept/deny requests. You can stop tutoring by going back to the home page and pushing the "I'm done tutoring!" button or logging out. 
    - You can switch between your student and tutor accounts on the **Profiles** tab.

### Citations and Tools

- Used HTML Geolocation API (https://www.w3schools.com/html/html5_geolocation.asp) to grab the user's current location on the map
- Used Mapbox documentation (https://docs.mapbox.com/help/tutorials/custom-markers-gl-js/) to create the map
- Used Bootstrap components (https://getbootstrap.com/docs/4.4/components/alerts/) to create the UI
- Used django-allauth (https://medium.com/@whizzoe/in-5-mins-set-up-google-login-to-sign-up-users-on-django-e71d5c38f5d5) for Google Login
- Used PostgreSQL database

### Django License

Copyright (c) Django Software Foundation and individual contributors.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of Django nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

### PostgreSQL License

Copyright (c) 2020, The QTs

Permission to use, copy, modify, and distribute this software and its documentation for any purpose, without fee, and without a written agreement is hereby granted, provided that the above copyright notice and this paragraph and the following two paragraphs appear in all copies.

IN NO EVENT SHALL The QTs BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF The QTs HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The QTs SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND The QTs HAS NO OBLIGATIONS TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
