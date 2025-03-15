// Функция для подтверждения удаления задачи
function confirmDelete(event) {
    event.preventDefault(); // Отменяем стандартное поведение формы
    const form = event.target; // Форма, которая вызвала событие

    Swal.fire({
        title: 'Вы уверены?',
        text: "Вы не сможете отменить это действие!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#007bff', // Синий цвет кнопки подтверждения
        cancelButtonColor: '#dc3545', // Красный цвет кнопки отмены
        confirmButtonText: 'Да, удалить!',
        cancelButtonText: 'Отмена',
        background: '#fff', // Белый фон модального окна
        customClass: {
            popup: 'custom-swal-popup', // Класс для кастомного стиля
        }
    }).then((result) => {
        if (result.isConfirmed) {
            form.submit(); // Отправляем форму, если пользователь подтвердил
        }
    });
}