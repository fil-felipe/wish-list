//console.log("Hello world!");

const modalReservation = document.getElementById('reserveModalBody');

const reserveButton = [...document.getElementsByClassName('reserve-btn')];
//console.log(reserveButton);
reserveButton.forEach(item=>item.addEventListener('click', e=>{
    const gift = e.target.getAttribute('data-gift-name');
    const gift_id = e.target.getAttribute('data-gift-id');
    modalReservation.innerHTML = "Czy napewno chcesz zarezerwować " + gift + "?"
    const confirmButton = document.getElementById("confirmButton");
    const confirmInput = document.getElementById("confirmId").value = gift_id;
    const currentHref = confirmButton.getAttribute("href");
    const finalHref = currentHref + "/"+gift_id;
    console.log(finalHref);
    confirmButton.setAttribute("href", finalHref);
}));


//console.log(testElement);

//const reserveButton = [...document.getElementByClassName('reserve-btn')];
//console.log(reserveButton);