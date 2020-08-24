Here are the basic endpoints for this app:

    POST
    /auth/users/ - for user's sign up.
    
    GET
    /auth/users/me - to show user data, the token is required.
    
    POST
    /auth/token/login - to generate token for user. This request
     needs a password and a username.
     
    POST
    /api/main/posts -  create a new post, the token is required.
     
    GET
    /api/main/posts -  list of all posts, the token is required.
    
    GET
    /api/main/profile/<int:pk> -  showing user activity, the token is required.
    
    POST
    /api/main/postpreference - add preference about someone's post, the token is required.
    
    PUT
    /api/main/postpreference-change/<int:pk> - change preference about someone's post, the token is required.
    
    GET
    /api/main/posts/likes-analysis analysis of posts for likes, the token is required.