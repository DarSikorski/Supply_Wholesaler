let updatebtn = document.getElementsByClassName('update-order');

for (let index = 0; index < updatebtn.length; index++) {
    updatebtn[index].addEventListener('click',function(){
        let productId = this.dataset.product;
        let action = this.dataset.action;
        console.log('productId',productId,action)
    
        console.log('user:', user)
        if (user === 'AnonymousUser'){

        }else{
            updateOrder(productId, action);
        }
    });
    
}

function updateOrder(productId, action){

    let url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId,'action': action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        location.reload()
    })
}
