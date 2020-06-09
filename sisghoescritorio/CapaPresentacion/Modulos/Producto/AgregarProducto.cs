using CapaNegocio;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CapaPresentacion.Modulos.Producto
{
    public partial class AgregarProducto : Form
    {
        public AgregarProducto()
        {
            InitializeComponent();
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            this.Dispose();
        }

        private void btnAgregar_Click(object sender, EventArgs e)
        {
            if (!String.IsNullOrEmpty(txtDescripcion.Text))
            {
                if (!String.IsNullOrEmpty(comboTipo.Text))
                {
                    if (!String.IsNullOrEmpty(txtPrecio.Text))
                    {
                        if (!String.IsNullOrEmpty(txtStock.Text))
                        {
                            try
                            {
                                ProductoController pc = new ProductoController();
                                
                                if (pc.AgregarProducto(txtDescripcion.Text,int.Parse(txtStock.Text),int.Parse(txtPrecio.Text),comboTipo.Text,(int)App.user.IDADMINISTRADOR,comboProveedor.Text))
                                {
                                    pc.LlenarGrid(App.fpp.dataProd);
                                    this.Dispose();
                                }


                            }
                            catch (Exception ex)
                            {
                                MessageBox.Show("Ingrese un numero valido.", "Crear Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                            }
                        }
                        else
                        {
                            MessageBox.Show("Ingrese stock del producto.", "Crear Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        }
                    }
                    else
                    {
                        MessageBox.Show("Ingrese precio del producto.", "Crear Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                }
                else
                {
                    MessageBox.Show("Ingrese tipo del producto.", "Crear Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            else
            {
                MessageBox.Show("Ingrese descripcion del producto.", "Crear Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void AgregarProducto_Load(object sender, EventArgs e)
        {
            ProductoController pc = new ProductoController();
            pc.LlenarComboTipo(comboTipo);
            comboTipo.SelectedIndex = 0;
            pc.LlenarComboProveedor(comboProveedor);
            comboProveedor.SelectedIndex = 0;
        }

        private void btnAgregarTipo_Click(object sender, EventArgs e)
        {
            AgregarTipo at = new AgregarTipo();
            at.Show();
        }
        
        private void comboTipo_Enter(object sender, EventArgs e)
        {
            ProductoController pc = new ProductoController();
            pc.LlenarComboTipo(comboTipo);
            comboTipo.SelectedIndex = 0;
        }
    }
}
