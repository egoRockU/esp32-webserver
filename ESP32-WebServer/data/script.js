document.addEventListener('DOMContentLoaded', function(){
    const txtElement = document.getElementById('inputText');
    const btnElement = document.getElementById('sendButton')

    btnElement.addEventListener('click', function(e){
        e.preventDefault();
    
        let message = txtElement.value;
    
        fetch('http://localhost:5000/message', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({message})
        }).then( res => {
            if (!res.ok) throw new Error("Network response was not ok");
            alert("Message Sent");
            txtElement.value = "";
        }).catch(err => {
            console.error(err);
        });
        return false;
    })

})