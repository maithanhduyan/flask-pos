$(document).ready(function () {
    // Bắt sự kiện submit form
    $('#search-form').on('submit', function (event) {
        event.preventDefault(); // Ngăn chặn form submit mặc định

        // Lấy giá trị từ input tên item
        var name = $('input[name="name"]').val();

        // Gửi AJAX request đến server để tìm kiếm item theo tên
        $.ajax({
            url: '/api/search',
            type: 'POST',
            data: JSON.stringify({ name: name }),
            dataType: "json",
            contentType: "application/json",
            success: function (response) {
                // Xóa nội dung bảng hiển thị item cũ
                $('#item-table tbody').empty();

                // Thêm item mới vào bảng
                $.each(response, function (index, item) {
                    $('#item-table tbody').append(
                        '<tr>' +
                        '<td>' + item.id + '</td>' +
                        '<td>' + item.name + '</td>' +
                        '<td>' + item.price + '</td>' +
                        '</tr>'
                    );
                });
            },
            error: function () {
                console.log('Error!');
            }
        });
    });
});