var endpoint = 'estadisticas'

function animacion_numero(idh, valor) {
    $({
        someValue: 0
    }).animate({
        someValue: valor
    }, {
        duration: 1000,
        easing: 'swing',
        step: function () {
            $('#' + idh).text(commaSeparateNumber(Math.round(this.someValue)));
        },
        complete: function () {
            $('#' + idh).text(commaSeparateNumber(Math.round(this.someValue)));
        }
    });

    function commaSeparateNumber(val) {
        while (/(\d+)(\d{3})/.test(val.toString())) {
            val = val.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1.");
        }
        return val;
    }
};
$.ajax({
    method: "GET",
    url: endpoint,
    success: function (data) {
        var verde = '#00b26f';
        var naranjo = '#ff8300';
        var azul = '#00b5e9';
        var rojo = '#fa4251';
        if (data.tipousuario == 3) {
            animacion_numero('huespedes_stat', data.huespedes)
            animacion_numero('servicios_stat', data.servicios)
            animacion_numero('fact_stat', data.total_factura)
            animacion_numero('habitaciones_disponibles', data.habitaciones_disponible)
            var ctx = document.getElementById('reservas');
            animacion_numero('total_reserva', data.total_reserva)
            var estadisticasReserva = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.labels_reserva,
                    datasets: [{
                        label: 'Reservas',
                        data: data.data_reserva

                            ,
                        backgroundColor: [
                            verde,
                            azul
                        ],
                        borderColor: [
                            verde,
                            azul
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
            animacion_numero('total_facturas', data.total_factura)
            ctx = document.getElementById('facturas');
            var estadisticasFactura = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.labels_factura,
                    datasets: [{
                        label: 'Facturas',
                        data: data.data_factura,
                        backgroundColor: [
                            verde,
                            naranjo,
                            rojo
                        ],
                        borderColor: [
                            verde,
                            naranjo,
                            rojo
                        ],
                        borderWidth: 1
                    }]
                }
            });
            ctx = document.getElementById('grafico_facturas');
            var grafico_facturas_line = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.ftm_labels,
                    datasets: [{
                        label: 'Facturas',
                        data: data.ftm_data,
                        backgroundColor: [
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul

                        ],
                        borderColor: [
                            azul

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

        if (data.tipousuario == 2) {
            animacion_numero('habit_stat', data.habitaciones_asignadas)
            animacion_numero('servicios_stat', data.servicios_solicitados)
            animacion_numero('fact_stat', data.facturas_emitidas)
            animacion_numero('ganancias_stat', data.ganacias_totales)
            var ctx = document.getElementById('grafico_facturas');
            var grafico_ganacias = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.ganancias_labels,
                    datasets: [{
                        label: 'Ganancias',
                        data: data.ganancias_data,
                        backgroundColor: [
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul

                        ],
                        borderColor: [
                            azul

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

            ctx = document.getElementById('solicitudesproductos');
            var estadisticasSolicitudes= new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.sdp_labels,
                    datasets: [{
                        label: 'Reservas',
                        data: data.sdp_data

                            ,
                        backgroundColor: [
                            verde,
                            naranjo,
                            azul,
                            rojo
                        ],
                        borderColor: [
                            verde,
                            naranjo,
                            azul,
                            rojo
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
            animacion_numero('total_solicitudes',data.sdp_total)
            ctx = document.getElementById('facturas');
            var estadisticasSolicitudes= new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.f_labels,
                    datasets: [{
                        label: 'Facturas',
                        data: data.f_data

                            ,
                        backgroundColor: [
                            verde,
                            naranjo,
                            rojo
                        ],
                        borderColor: [
                            verde,
                            naranjo,
                            rojo
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
            animacion_numero('total_facturas',data.f_total)
        }

        if(data.tipousuario == 4){
            animacion_numero('p_solicitados',data.pedidos_solicitados)
            animacion_numero('p_transito',data.pedidos_transito)
            animacion_numero('p_entregados',data.pedidos_entregados)
            animacion_numero('p_rechazados',data.pedidos_rechazados)
            var ctx = document.getElementById('grafico_ganancias');
            var grafico_ganacias = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.ganancias_labels,
                    datasets: [{
                        label: 'Ganancias',
                        data: data.ganancias_data,
                        backgroundColor: [
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul

                        ],
                        borderColor: [
                            azul

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

        if(data.tipousuario == 1){
            animacion_numero('user_stat',data.usuarios)
            animacion_numero('product_stat',data.productos)
            animacion_numero('service_stat',data.servicios)
            animacion_numero('room_stat',data.habitaciones)
            
            var ctx = document.getElementById('grafico_facturas');
            var grafico_ganacias = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.ganancias_labels,
                    datasets: [{
                        label: 'Ganancias',
                        data: data.ganancias_data,
                        backgroundColor: [
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul,
                            azul

                        ],
                        borderColor: [
                            azul

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

            ctx = document.getElementById('solicitudesproductos');
            var estadisticasSolicitudes= new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.sdp_labels,
                    datasets: [{
                        label: 'Reservas',
                        data: data.sdp_data

                            ,
                        backgroundColor: [
                            verde,
                            naranjo,
                            azul,
                            rojo
                        ],
                        borderColor: [
                            verde,
                            naranjo,
                            azul,
                            rojo
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
            animacion_numero('total_solicitudes',data.sdp_total)
            ctx = document.getElementById('facturas');
            var estadisticasSolicitudes= new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.f_labels,
                    datasets: [{
                        label: 'Facturas',
                        data: data.f_data

                            ,
                        backgroundColor: [
                            verde,
                            naranjo,
                            rojo
                        ],
                        borderColor: [
                            verde,
                            naranjo,
                            rojo
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true
                }
            });
            animacion_numero('total_facturas',data.f_total)
        
            
        }

    },
    error: function (error_data) {
        console.log(error_data)
        return null
    }

})