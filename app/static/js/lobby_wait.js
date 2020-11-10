setInterval(check_for_users, 7000);

function check_for_users() {
    let ul = document.getElementById('lobby_user_list');
    const url = ul.getAttribute('data-ajax-url');
    $.ajax({
        url: url,
        dataType: 'json',
        success: function (data) {
            console.log(data.users);

            let li_childs = ul.querySelectorAll('li');
            console.log(li_childs);
            if (li_childs.length > 0){
                for (let child of li_childs){
                    child.remove()
                }
            }

            let all_user = data.users;
            console.log(all_user);
            for (let index = 0; index < data.users.length; index++) {
                console.log(data.users[index]);

                let x = document.createElement("LI");
                x.innerText = data.users[index];
                ul.insertAdjacentElement('afterbegin', x)
            }
        }

    })
}