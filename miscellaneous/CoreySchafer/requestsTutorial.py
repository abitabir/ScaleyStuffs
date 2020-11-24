# https://www.youtube.com/watch?v=tb8gHvYlCFs Python Requests Tutorial by Corey Schafer

import requests

def requestingURL(url, params=None):  # technically dunneed a method for a method lol
    response = requests.get(url)
    return response


r = requestingURL("https://en.wikipedia.org/wiki/Turtle")
i = requestingURL("https://upload.wikimedia.org/wikipedia/commons/f/f4/Florida_Box_Turtle_Digon3_re-edited.jpg")

# print(r)
# print(dir(r))  # running an object through a dir() function allows you to see all the attributes and methods availible to you for that object
# print(help(r))  # help on the other hand gives a much more detailed explanation of everyhting from this object
# print(r.text)  # gives us the content of the response in unicode - html for the page we just looked at in the browser. you can use a HTML parser to parse this info


# print(r.status_code)  # prints out HTTP code
# print(r.ok)  # returns True if server response is less than 300

# print(r.headers)  # we get all the headers

# print(i.content)  # .content returns the content of the response in bytes, as opposed to .text which does in bits
# just an image of a turtle, so .content prints out the bytes from that image - we can save this to a file onto our computer
# with open ("turt.png", "wb") as f: # "wb" mode is write byte, hum
#     # this code is going to save this file in the same directory as our python module as we didn't specify a full path
#     # we find an image of a turtleeeee XDDD
#     f.write(i.content)
#     f.close()

# payload is term used for main body, excluding headers of HTTP
#
# payload = {"page": 2, "count": 25}  # using clean dico to set url on a route that has some url parameters
# g = requests.get("https://httpbin.org/get", payload)  # httpbin responds with JSON information of what we sent in the request
# this api is is using a rest model, most do, but not all
# print(g.text)  # says our request had arguemnts of a page equal to 2 and a count of 25
# print(g.url)  # allows you to check if the requests library created the correct url for you
#
# data = {"username": "abitabir", "password": "ami"}  # form data you want to post to a route (this is an example of what would be more likely to be in a form as opposed to the url params in payload
# # can make these data/payload being inputted key value pairs whatever you like - however if you are trying to pass in certain form data, you will have to actually look at the HTML source code of the URL to see what values the form actually expects
# p = requests.post("https://httpbin.org/post", data)  # what you'd use to post data to a route
# print(p.text)  # we'll see our args are empty cuz we didn't pass anything into url parameters, but we find the data that we inputted/posted in form
# # note that we get a JSON response back from the website - very common when working with certain APIs
# # instead if using .text as a method, we can use .json()
# print(p.json())  # this returns a python dictionary! from that JSON -  can store it in a variable if we want to access the data inside
# dico = p.json()
# print(dico["form"])  # returns {'password': 'ami', 'username': 'abitabir'}
# # this is the same as importing the json module in python and using json.loads on the response text, but this is nice little shortcut for that functionality
#
# u = requests.put("https://httpbin.org/put", data)  # does same thing as post here
# # put is for update (hardly used - mostly get and post are used, occasionally delete as well), post is for creating new record
# print(u.text)

#
# # not all logins are done via form based authentication - some done via basic authentication, and both requests and
# # httpbin can help you with that
# # httpbin allows you to test basic auth routes is by specifying the credentials that you want to test against
# # {like HYPOTHESIS stats XO} in the URL, and then you can pass different credentials to that route to see if that works
# a = requests.get("https://httpbin.org/basic-auth/abitabir/ami", auth=("abitabit", "ami"))
# print(a.text)  # no response text returned
# print(a)  # this on other hand returns <Response [401]> when unauthenticated - 401 is the unauthorised response code
# print(a.ok)  # prints False
# a = requests.get("https://httpbin.org/basic-auth/abitabir/ami", auth=("abitabir", "ami"))
# print(a.text)
# print(a)  # this on other hand returns <Response [200]> which means everything working fine and dandy
# print(a.ok)  # prints True
# # lattermost one authenticates! {"authenticated": true, "user": "abitabir"}

# another thing to note with the requests module is that it will wait indefinitely if it's not getting a response form
# a page it is tryin gto access so it is probably a good idea to set a timeout if possibel that the website won't
# respond in a reasonable amount of time ~ otherwise it'll just wait and hang forever X'(
# reccomended to implement, unless you know you are dealing with an API that you know is gonna do a load of computation
# you can just pass timeout into the parameters of the .get as an int for however many seconds
print(requests.get("https://httpbin.org/delay/1", timeout=3).ok)  # prints True
# as this url route delays a response by 1 second and the timeout is 3
print(requests.get("https://httpbin.org/delay/10", timeout=3).ok)  # doesn't even print False, gives ReadTimeoutError
# as this url route delays a response by 10 seconds but the timeout is 3
