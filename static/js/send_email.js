let form = document.getElementById('contact-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    let data = {};
    for (let element of form.elements) {
        data[element.name] = element.value
    }
    console.log(data);
    $.post(form.getAttribute('action'), data, (response) => {
        console.log(response)
        if (response.detail == 'Ok') {
            Swal.fire({
                title: 'Success!',
                text: 'Email sent successfully',
                icon: 'success',
                confirmButtonText: 'Cool'
              })
        }
    });
})