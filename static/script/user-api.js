const code = $('form').attr('id');

$.ajax({
    'url': `/api/v1/users/user/${code}`,
    'method' : 'GET'
}).done(user => {
    $('#username').val(user.username);
    $('#name').val(user.name);
    $('#email').val(user.email);
})

function update_user() {
    name = $('#name').val();
    email = $('#email').val();
    password = $('#password').val();

    data = {}

    if(name !== '') {
        data['name'] = name;
    }
    if(email !== '') {
        data['email'] = email;
    }
    if(password !== '') {
        data['password'] = password;
    }

    $.ajax({
        "url": `/api/v1/users/user/${code}`,
        "method": "PUT",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        },
        "data": JSON.stringify(data),
    }).done(function (response) {
        console.log(response);
    }).fail(function(error) {
        console.log(error);
    })
}