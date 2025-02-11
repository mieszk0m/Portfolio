document.getElementById('commandForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Zapobiega standardowemu wysłaniu formularza

    const command = document.getElementById('commandInput').value;

    // Przetwarzanie komendy
    switch (command) {
        case 'log':
            console.log('To jest wiadomość log.');
            break;
        case 'group':
            console.group('Grupa Wiadomości');
            console.log('Wiadomość 1 w grupie');
            console.log('Wiadomość 2 w grupie');
            console.groupEnd();
            break;
        case 'warn':
            console.warn('To jest ostrzeżenie!');
            break;
        case 'error':
            console.error('To jest błąd!');
            break;
        default:
            console.log('Nieznana komenda');
    }
});