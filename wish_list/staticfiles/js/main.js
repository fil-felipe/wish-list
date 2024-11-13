

const modalReservation = document.getElementById('reserveModalBody');

const reserveButton = [...document.getElementsByClassName('reserve-btn')];

const modalDelete = document.getElementById('deleteModalBody');

const deleteButton = [...document.getElementsByClassName('delete-btn')];

reserveButton.forEach(item=>item.addEventListener('click', e=>{
    const gift = e.target.getAttribute('data-gift-name');
    const giftId = e.target.getAttribute('data-gift-id');
    modalReservation.innerHTML = "Czy napewno chcesz zarezerwować " + gift + "?"
    const confirmButton = document.getElementById("confirmButton");
    const currentHref = confirmButton.getAttribute("href");
    const finalHref = currentHref + "/"+ giftId;
    confirmButton.setAttribute("href", finalHref);
}));



deleteButton.forEach(item=>item.addEventListener('click', e=>{
    const button = e.target.closest('.delete-btn');
    console.log(e.target);
    const gift = button.target.getAttribute('data-gift-name');
    const giftId = button.target.getAttribute('data-gift-id');
    const dataListName = button.target.getAttribute('data-list-name');
    const dataRecipientName = button.target.getAttribute('data-recipient-name');
    // modalDelete.innerHTML = `Czy napewno chcesz usunać prezent ${gift} dla ${dataRecipientName} z listy ${dataListName}?`
    // modalDelete.innerHTML = `Czy napewno chcesz usunać prezent ?`
    modalDelete.innerHTML = "Czy napewno chcesz usunać prezent " + gift + " dla " + dataRecipientName + " z listy " + dataListName + "?";
    const confirmButton = document.getElementById("confirmButton");
    const currentHref = confirmButton.getAttribute("href");
    const finalHref = currentHref + "/"+ giftId;
    console.log(finalHref);
    confirmButton.setAttribute("href", finalHref);
}));

