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
    public partial class ModificarProducto : Form
    {
        public ModificarProducto()
        {
            InitializeComponent();
        }

        private void btnModificar_Click(object sender, EventArgs e)
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

                                if (pc.ModificarProducto(txtDescripcion.Text,int.Parse(labelID.Text), int.Parse(txtStock.Text), int.Parse(txtPrecio.Text), comboTipo.Text,comboProveedor.Text))
                                {
                                    pc.LlenarGrid(App.fpp.dataProd);
                                    this.Dispose();
                                }


                            }
                            catch (Exception ex)
                            {
                                MessageBox.Show("Ingrese un numero valido.", "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                            }
                        }
                        else
                        {
                            MessageBox.Show("Ingrese stock del producto.", "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        }
                    }
                    else
                    {
                        MessageBox.Show("Ingrese precio del producto.", "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    }
                }
                else
                {
                    MessageBox.Show("Ingrese tipo del producto.", "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            else
            {
                MessageBox.Show("Ingrese descripcion del producto.", "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            this.Dispose();
        }

        private void comboTipo_Enter(object sender, EventArgs e)
        {
            ProductoController pc = new ProductoController();
            pc.LlenarComboTipo(comboTipo);
            comboTipo.SelectedIndex = 0;
        }

        private void btnAgregarTipo_Click(object sender, EventArgs e)
        {
            AgregarTipo at = new AgregarTipo();
            at.Show();
        }

        private void ModificarProducto_Load(object sender, EventArgs e)
        {

        }
    }
}
