// Mengerjakan fungsi button di bagian clothing & accessories
let btns = document.getElementsByClassName('addtocart')

// Loop tiap buttons, tambahkan fungsi untuk get id tiap product
for(let i = 0; i < btns.length; i++) {
    btns[i].addEventListener('click', function(e){
        // Akses data attribute
        let product_id = e.target.dataset.product // Merujuk ke item yang di klik (dapat product id)
        let action = e.target.dataset.action
        console.log(product_id)

        // Handle apakah user loged in atau tidak
        if(user=='AnonymousUser'){
            console.log('You are not signed in')
            
            // Arahin user untuk login

            $('#exampleModal').modal('show');

        }
        else{
            // Masukin product ke cart
            addToCart(product_id,action)
        }
    
    })
}

function addToCart(p_id, act){
    const data = {product_id: p_id, action: act};
  
    // fetch api diambil dari dokumentasi developer.mozilla.org
  
  let url = 'updatecart'
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
    },
    body: JSON.stringify(data),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    // Update nomor cart tanpa reload
    document.getElementById('cart').innerHTML = `<h4>${data.quantity}</h4>`
  })
  .catch((error) => {
    console.error('Error:', error);
  });
  
}


// Untuk handle quantity produk di cart

let inputfields = document.getElementsByTagName('input')
// Masukkan actionlistener
for (let i =0; i<inputfields.length; i++) {
    inputfields[i].addEventListener('change', updateQuantity)

}

// Buat func updateQuantity untuk send data dari input type number ke backend
function updateQuantity(e) {
    let inputvalue = e.target.value 
    let product_id = e.target.dataset.product

    const data = {p_id: product_id, in_val: inputvalue};
    let url = 'updatequantity'

    // fetch api diambil dari dokumentasi developer.mozilla.org
    fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);

        // Merujuk ke yang user click
        e.target.parentElement.parentElement.children[4].innerHTML = `<h3>Rp ${data.subtotal.toFixed(2)}</h3>`
        // Update content element dari total dan cart (update data tanpa harus reload)
        document.getElementById('total').innerHTML = `<h3><strong>Rp ${data.grandtotal.toFixed(2)}</strong></h3> `
        document.getElementById('cart').innerHTML = `<h4>${data.quantity}</h4>`


      })
      .catch((error) => {
        console.error('Error:', error);
      });
}