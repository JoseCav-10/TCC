let dia_1 = document.getElementById("getDias")
let dias = dia_1.innerText
let dia_2 = document.getElementById("dia_2")
let listDias = dias.split(",")

console.log(listDias)

dia_1.innerText = listDias[0]
dia_2.innerText = listDias[1]
