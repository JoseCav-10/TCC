function marcarVisualizacao(notificacaoId) {
    fetch('/marcar-visualizacao/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': getCookie('csrftoken')  // Envia o token CSRF
        },
        body: `notificacao_id=${notificacaoId}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            console.log('Notificação marcada como visualizada!');
        } else {
            console.error('Erro:', data.message);
        }
    })
    .catch(error => console.error('Erro no fetch:', error));
}

// Função para pegar o CSRF token (necessário para Django)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function markAllAsRead(userId) {
    // Obtém o CSRF Token do campo oculto
    const csrfToken = document.getElementById('csrf_token').value;

    fetch(`/notificacoes/marcar-todas-como-lidas/${userId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken // CSRF Token é obrigatório para Django
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao marcar as notificações como lidas.');
        }
        return response.json();
    })
    .then(data => {
        alert('Todas as notificações foram marcadas como lidas!');
        
        // Atualizar visualmente a página
        document.querySelectorAll('.notificacao').forEach(notif => {
            notif.classList.add('lida'); // Adiciona a classe .lida às notificações
        });
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}
