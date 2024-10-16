let dia_1 = document.getElementById("getDatas")
let dias = dia_1.innerText
let listDias = dias.split(",")



dia_1.innerText = `${listDias[0]} e ${listDias[1]}`

