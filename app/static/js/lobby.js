function guess(){
    const start = document.querySelector('#start_number');
    const end = document.querySelector('#end_number');
    const client_data = JSON.stringify({'data':{'name': 'guess'}
    });

    $.ajax({
        type: 'POST',
        url: '/lobby/status/change',
        dataType: 'json',
        data: {'name': 'guess'},
        success: function (data) {
            console.log(data);
            document.querySelector('#guess_lobby').style.display = 'block';
            let h2 = document.querySelector('#guess_lobby_h2');
            h2.innerText = data.name;
        }
    })
}

function evaluate_guess() {
    $.ajax({
        url: '/game/evaluate',
        dataType: 'json',
        data: {'name': 'guess'},
        success: function (data) {
            alert('Number: ' + data['result']);
            let list = document.querySelector('#results');
            for (let winner in data['winner']){
                let li = document.createElement('li');
                li.innerText = 'Winner: ' +winner + '; Game: ' + data['game']['name'];
                list.insertAdjacentElement('afterbegin', li);
            }
            document.querySelector('#guess_lobby').style.display = 'none';
        }
    });
}