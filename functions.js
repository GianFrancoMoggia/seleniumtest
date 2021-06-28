
var mail;     
var username;
var password;
var re_password;

function myFunction(){
    mail     = document.getElementById("mail").value;
    password = document.getElementById("password").value;

    if(typeof(document.getElementById("username")) != 'undefined' && document.getElementById("username") != null){
        username    = document.getElementById("username").value;
        re_password = document.getElementById("re-password").value;
    }else{
        username = null;
    }

    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    
    if (mail.toLowerCase().match(re)) {
        if (password.length > 6 && password.match(/^[0-9a-zA-Z]+$/)) {
            if(username != null){
                if(username.length > 6 && username.match(/^[0-9a-zA-Z]+$/) && password == re_password){
                    callApi("register")
                } else {
                    alert(false);
                }
            } else {
                callApi("login")
            }
        } else {
            alert(false); 
        } 
    } else {
        alert(false);  
    }
}

function callApi(action) {
    if(action == "login"){
        if (mail == "nacho@gmail.com" && password == 1234567){
            alert(true);
        } else {
            alert(false);
        }
    } else {
        alert(true);
    }
}