$(document).ready(function () {

    let currentPage;
    let page = 1;
    // Bắt sự kiện submit form
    $('#search-form').on('submit', function (event) {
        event.preventDefault(); // Ngăn chặn form submit mặc định
        let keyword = $('input[name="name"]').val();
        $.ajax({
            url: '/api/items2?page=' + 1 + '&keyword=' + keyword,
            dataType: 'json',
            success: function (data) {
                // render table với items nhận được
                renderTable(data.items);

                createPagination(data.total_pages, data.current_page);

                // attach click event to pagination buttons
                $('#pagination').on('click', '.page-link', function () {
                    console.log('click');
                    console.log($(this).data('page'));
                    loadPage($(this).data('page'));
                });
            }
        });
    });

    function createPagination(totalPages, currentPage) {
        let pagination = $('#pagination ul');

        pagination.empty();

        if (totalPages <= 1) {
            return;
        }

        if (currentPage == null) {
            currentPage = 1;
        }

        if (currentPage > totalPages) {
            currentPage = totalPages;
        }

        if (currentPage > 1) {
            pagination.append('<li class="page-item"><a class="page-link" href="#" data-page="' + (currentPage - 1) + '">Prev</a></li>');
        }

        for (var i = 1; i <= totalPages; i++) {
            if (i == currentPage) {
                pagination.append('<li class="page-item active"><a class="page-link" href="#" data-page="' + i + '">' + i + '</a></li>');
            } else {
                pagination.append('<li class="page-item"><a class="page-link" href="#" data-page="' + i + '">' + i + '</a></li>');
            }
        }

        if (currentPage < totalPages) {
            pagination.append('<li class="page-item"><a class="page-link" href="#" data-page="' + (currentPage + 1) + '">Next</a></li>');
        }
    }

    function renderTable(items) {
        // Xóa tất cả dữ liệu trong table
        $('#item-table').empty();
        // tạo HTML code để render table với items được truyền vào
        // ví dụ:
        let html = '<table class=' + 'table' + '>';
        html += '<tr><th>ID</th><th>Name</th><th>Price</th></tr>';

        for (let i = 0; i < items.length; i++) {
            html += '<tr><td>' + items[i].id + '</td><td>' + items[i].name + '</td><td>' + items[i].price + '</td></tr>';
        }

        html += '</table>';

        // gắn HTML code vào thẻ có id="item-table"
        $('#item-table').html(html);
    }


    function loadPage(page) {
        if (page === currentPage) {
            return;
        }
        currentPage = page;
        let keyword = $('input[name="name"]').val();

        $.ajax({
            url: '/api/items2?page=' + page + '&keyword=' + keyword,
            dataType: 'json',
            success: function (data) {
                // render table với items nhận được
                renderTable(data.items);

                createPagination(data.total_pages, data.current_page);

                // attach click event to pagination buttons
                $('#pagination').on('click', '.page-link', function () {
                    console.log('click');
                    console.log($(this).data('page'));
                    loadPage($(this).data('page'));
                });
            }
        });
    }

});