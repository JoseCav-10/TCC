function setSigla(elemento){
    let mes = document.getElementById(`mes_agendado${elemento}`).innerText;

    switch(mes){
        case "01":
            document.getElementById(`mes_agendado${elemento}`).innerText = "JAN";
            break
    
        case "02":
            document.getElementById(`mes_agendado${elemento}`).innerText = "FEV";
            break
        
        case "03":
            document.getElementById(`mes_agendado${elemento}`).innerText = "MAR";
            break
    
        case "04":
            document.getElementById(`mes_agendado${elemento}`).innerText = "ABR";
            break
    
        case "05":
            document.getElementById(`mes_agendado${elemento}`).innerText = "MAI";
            break
    
        case "06":
            document.getElementById(`mes_agendado${elemento}`).innerText = "JUN";
            break
    
        case "07":
            document.getElementById(`mes_agendado${elemento}`).innerText = "JUL";
            break
        
        case "08":
            document.getElementById(`mes_agendado${elemento}`).innerText = "AGO";
            break
    
        case "09":
            document.getElementById(`mes_agendado${elemento}`).innerText = "SET";
            break
    
        case "10":
            document.getElementById(`mes_agendado${elemento}`).innerText = "OUT";
            break
    
        case "11":
            document.getElementById(`mes_agendado${elemento}`).innerText = "NOV";
            break
    
        case "12":
            document.getElementById(`mes_agendado${elemento}`).innerText = "DEZ";
            break
    
        default:
            document.getElementById(`mes_agendado${elemento}`).innerText = "INVÁLIDO";
    };
    
};

console.log("OII")


const listAprov = document.getElementById("lista_aprovados").innerText;
const arrayAprov = JSON.parse(listAprov);




for (let e of arrayAprov){
    setSigla(e)
    console.log(`Tá indo ${e}`)
};


