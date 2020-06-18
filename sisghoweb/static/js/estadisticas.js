var endpoint = 'estadisticas'
$.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        if (data.tipousuario == 3) {
            document.getElementById('total_reserva').innerHTML = data.total_reserva;
            $({
                Counter: 0
            }).animate({
                Counter: $('.reservas').text()
            }, {
                duration: 1000,
                easing: 'swing',
                step: function () {
                    $('.reservas').text(Math.ceil(this.Counter));
                }
            });
            var ctx = document.getElementById('reservas');
            var estadisticasReserva = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.labels_reserva,
                    datasets: [{
                        label: 'Reservas',
                        data: data.data_reserva

                            ,
                        backgroundColor: [
                            'rgb(54,162,235)',
                            'rgb(54,235,127)'
                        ],
                        borderColor: [
                            'rgb(54,162,235)',
                            'rgb(54,235,127)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
            document.getElementById('total_facturas').innerHTML = data.total_factura;
            $({
                Counter: 0
            }).animate({
                Counter: $('.facturas').text()
            }, {
                duration: 1000,
                easing: 'swing',
                step: function () {
                    $('.facturas').text(Math.ceil(this.Counter));
                }
            });
            ctx = document.getElementById('facturas');
            var estadisticasFactura = new Chart(ctx,{
                type : 'pie',
                data: {
                    labels: data.labels_factura,
                    datasets: [{
                        label: 'Facturas',
                        data: data.data_factura,
                        backgroundColor: [
                            'rgb(54,162,235)',
                            'yellow',
                            'red'
                        ],
                        borderColor: [
                            'rgb(54,162,235)',
                            'yellow',
                            'red'
                        ],
                        borderWidth: 1
                    }]
                }
            });
        }


    },
    error: function (error_data) {
        console.log(error_data)
        return null
    }

})