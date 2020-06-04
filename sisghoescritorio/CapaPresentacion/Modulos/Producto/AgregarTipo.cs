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
    public partial class AgregarTipo : Form
    {
        public AgregarTipo()
        {
            InitializeComponent();
        }

        private void btnCancelar_Click(object sender, EventArgs e)
        {
            this.Dispose();
        }

        private void btnAgregar_Click(object sender, EventArgs e)
        {
            if (!String.IsNullOrEmpty(txtTipo.Text))
            {
                ProductoController pc = new ProductoController();
                if (pc.AgregarTipoProducto(txtTipo.Text))
                {
                    this.Dispose();
                }
                
                
            }
            else
            {
                MessageBox.Show("Ingrese descripcion del tipo producto.", "Crear Tipo Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
    }
}
