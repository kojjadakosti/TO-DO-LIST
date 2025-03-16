// Функция для подтверждения удаления задачи
function confirmDelete(event) {
    event.preventDefault();
    const form = event.target;

    Swal.fire({
        title: 'Вы уверены?',
        text: "Вы не сможете отменить это действие!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#007bff',
        cancelButtonColor: '#dc3545',
        confirmButtonText: 'Да, удалить!',
        cancelButtonText: 'Отмена',
        background: '#fff',
        customClass: {
            popup: 'custom-swal-popup',
        }
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit();
        }
    });
}