
let templete = ``;

for (let i = 1; i < 5; i++) {
    document.getElementById('formdata').insertAdjacentHTML('beforebegin', `<div class="form-row mt-3">
        <div class="col-5">
            <input type="number" id="obj${i}1" class="form-control" placeholder="Value 1">
        </div>
        <div class="col-2">
            <select class="form-control" id="obj${i}2">
                <option value="+">+</option>
                <option value="-">-</option>
            </select>
        </div>
        <div class="col-5">
            <input type="number" class="form-control" id="obj${i}3" placeholder="Value 2">
        </div>
    </div>`);
}


document.getElementById('formdata').addEventListener('submit', async (e) => {

    e.preventDefault();
    let dataForm = new FormData();
    dataForm.append('op1', `${document.getElementById('obj11').value} ${document.getElementById('obj12').value} ${document.getElementById(`obj13`).value}`)
    dataForm.append('op2', `${document.getElementById('obj21').value} ${document.getElementById('obj22').value} ${document.getElementById(`obj23`).value}`)
    dataForm.append('op3', `${document.getElementById('obj31').value} ${document.getElementById('obj32').value} ${document.getElementById(`obj33`).value}`)
    dataForm.append('op4', `${document.getElementById('obj41').value} ${document.getElementById('obj42').value} ${document.getElementById(`obj43`).value}`)
    let consult = await fetch('arimetic', {
        method: 'POST', body: dataForm
    })

    let response = await consult.json();
    // swal("Here's the title!", response[0]);
    alert(response[0])


});