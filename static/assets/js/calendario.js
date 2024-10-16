document.addEventListener("DOMContentLoaded", function() {
    let tituloMes = document.getElementById('getMes');
    const mesSelecionado = document.getElementById("mesSelecionado");
    const dias = document.querySelectorAll(".btn-day");
    const listDatasElement = document.getElementById("list-datas");
    const listDatasString = listDatasElement.innerHTML;

    // 2. Formatar a string para um formato JSON válido
    // Substituindo chaves simples por chaves duplas e formatando o objeto
    const jsonString = listDatasString
        .replace(/'/g, '"') // Troca ' por "
        .replace(/(\w+):/g, '"$1":'); // Coloca aspas em torno das chaves

    // 3. Converter a string formatada para um objeto JSON
    const listDatasObject = JSON.parse(jsonString);


    mesSelecionado.addEventListener("change", function() {
        // Remover as classes de todos os dias
        dias.forEach(dia => dia.classList.remove("bg-primary", "text-light"));
        

        let numeroMes = mesSelecionado.value;
        console.log(tituloMes)
        console.log(mesSelecionado)
        console.log(numeroMes)
        switch(numeroMes){
            case '1':
                tituloMes.innerText = "Janeiro"
                break
            case '2':
                tituloMes.innerText = "Fevereiro"
                break
            case '3':
                tituloMes.innerText = "Março";
                break;
            case '4':
                tituloMes.innerText = "Abril";
                break;
            case '5':
                tituloMes.innerText = "Maio";
                break;
            case '6':
                tituloMes.innerText = "Junho";
                break;
            case '7':
                tituloMes.innerText = "Julho";
                break;
            case '8':
                tituloMes.innerText = "Agosto";
                break;
            case '9':
                tituloMes.innerText = "Setembro";
                break;
            case '10':
                tituloMes.innerText = "Outubro";
                break;
            case '11':
                tituloMes.innerText = "Novembro";
                break;
            case '12':
                tituloMes.innerText = "Dezembro";
                break;
            default:
                tituloMes.innerText = "Mês Desconhecido";
                break;
        };

        // Definir o número de dias para o mês selecionado
        const mes = parseInt(mesSelecionado.value);
        let diasNoMes = 31; // Padrão para meses de 31 dias
        let getDia31 = document.getElementById("31")
        getDia31.style.display = "block"
        let getDia30 = document.getElementById("30")
        getDia30.style.display = "block"

        // Definir o número de dias para cada mês
        if (mes === 4 || mes === 6 || mes === 9 || mes === 11) {
            diasNoMes = 30; // Meses de 30 dias
            getDia30.style.display = "block"
            
            let getExluirDia = document.getElementById("31")
            if (getExluirDia) {
                getExluirDia.style.display = "none"; // Oculta o elemento
            }

        } else if (mes === 2) {
            diasNoMes = 29; // Fevereiro (não considera ano bissexto)
            
            let getExluirDia31 = document.getElementById("31")
            if (getExluirDia31) {
                getExluirDia31.style.display = "none"; // Oculta o elemento
            }

            let getExluirDia30 = document.getElementById("30")
            if (getExluirDia30) {
                getExluirDia30.style.display = "none"; // Oculta o elemento
            }

        }

        
        let valorListDatasObject = tituloMes.innerText
        console.log(listDatasObject)
        let teste = listDatasObject[valorListDatasObject]

        // Adicionar as classes para os dias correspondentes ao mês
        for (let i = 0; i <= teste.length; i++) {
            const diaBtn = document.getElementById(teste[i].toString());
            if (diaBtn) {
                diaBtn.classList.add("bg-primary", "text-light");
            }
        }
    });

    // Disparar o evento de mudança para inicializar com o mês padrão
    mesSelecionado.dispatchEvent(new Event("change"));
});