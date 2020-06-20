var endpoint = 'estadisticas'
function animacion_numero(idh, valor){
    document.getElementById(idh).innerHTML = valor;
    
    $({
        Counter: 0
    }).animate({
        Counter: $('.'+idh).text()
    }, {
        duration: 1000,
        easing: 'swing',
        step: function () {
            $('.'+idh).text(Math.ceil(this.Counter));
        }
    });
};
$.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {

        if (data.tipousuario == 3) {
            animacion_numero('huespedes_stat',data.huespedes)
            animacion_numero('servicios_stat',data.servicios)
            animacion_numero('fact_stat',data.total_factura)
            var ctx = document.getElementById('reservas');
            animacion_numero('total_reserva',data.total_reserva)
            var estadisticasReserva = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.labels_reserva,
                    datasets: [{
                        label: 'Reservas',
                        data: data.data_reserva

                            ,
                        backgroundColor: [
                            'rgb(120, 210, 55)',
                            'rgb(255, 210, 70)'
                        ],
                        borderColor: [
                            'rgb(120, 210, 55)',
                            'rgb(255, 210, 70)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
            animacion_numero('total_facturas',data.total_factura)
            ctx = document.getElementById('facturas');
            var estadisticasFactura = new Chart(ctx,{
                type : 'pie',
                data: {
                    labels: data.labels_factura,
                    datasets: [{
                        label: 'Facturas',
                        data: data.data_factura,
                        backgroundColor: [
                            'rgb(120, 210, 55)',
                            'rgb(255, 210, 70)',
                            'rgb(255, 99, 88)'
                        ],
                        borderColor: [
                            'rgb(120, 210, 55)',
                            'rgb(255, 210, 70)',
                            'rgb(255, 99, 88)'
                        ],
                        borderWidth: 1
                    }]
                }
            });
            ctx = document.getElementById('grafico_facturas');
            //var MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            var grafico_facturas_line = new Chart(ctx,{
                type : 'line',
                data: {
                    labels: data.ftm_labels,
                    datasets: [{
                        label: 'Facturas',
                        data: data.ftm_data,
                        backgroundColor: [
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)',
                            'rgb(120, 210, 55)'
                            
                        ],
                        borderColor: [
                            'rgb(120, 210, 55)'
                            
                        ],
                        borderWidth: 1,
                        fill: false
                    }]
                },
                options: {
                    responsive: true,
                    
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Mes'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Total $'
						}
					}]
				}
                }
            });
        }

        if(data.tipousuario == 2){
            
        }

    },
    error: function (error_data) {
        console.log(error_data)
        return null
    }

})