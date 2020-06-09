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
    public partial class FormularioProducto : Form
    {
        public FormularioProducto()
        {
            InitializeComponent();
        }

        private void FormularioProducto_Load(object sender, EventArgs e)
        {
            ProductoController pc = new ProductoController();
            pc.LlenarGrid(dataProd);
        }

        private void btnAgregarPro_Click(object sender, EventArgs e)
        {
            AgregarProducto agp = new AgregarProducto();
            agp.Show();
        }

        private void btnModificarPro_Click(object sender, EventArgs e)
        {
            try
            {
                ProductoController pc = new ProductoController();
                int id = int.Parse(dataProd.CurrentRow.Cells[0].Value.ToString());
                ModificarProducto mp = new ModificarProducto();
                pc.LlenarComboTipo(mp.comboTipo);
                pc.LlenarCampos(id,mp.txtDescripcion,mp.txtStock,mp.txtPrecio,mp.comboTipo,mp.labelID,mp.comboProveedor);
                mp.Show();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Debe seleccionar un producto.", "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void btnEliminarPro_Click(object sender, EventArgs e)
        {
            try
            {
                ProductoController pc = new ProductoController();
                int id = int.Parse(dataProd.CurrentRow.Cells[0].Value.ToString());
                pc.EliminarProducto(id);
                pc.LlenarGrid(App.fpp.dataProd);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Debe seleccionar un producto.", "Eliminar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
    }
}
