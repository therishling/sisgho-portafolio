using CapaDatos;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CapaNegocio
{
    public class ProductoController
    {

        public List<PRODUCTO> ListadoProducto()
        {

            ServiceProducto sp = new ServiceProducto();
            return sp.getEntities();
        }

        public void LlenarGrid(DataGridView dt)
        {
            ServiceProducto sp = new ServiceProducto();
            dt.Rows.Clear();
            dt.Columns.Clear();

            
            DataGridViewTextBoxColumn columna1 = new DataGridViewTextBoxColumn();
            columna1.HeaderText = "id";
            DataGridViewTextBoxColumn columna2 = new DataGridViewTextBoxColumn();
            columna2.HeaderText = "DESCRIPCION";
            DataGridViewTextBoxColumn columna3 = new DataGridViewTextBoxColumn();
            columna3.HeaderText = "TIPO PRODUCTO";
            DataGridViewTextBoxColumn columna4 = new DataGridViewTextBoxColumn();
            columna4.HeaderText = "PRECIO";
            DataGridViewTextBoxColumn columna5 = new DataGridViewTextBoxColumn();
            columna5.HeaderText = "STOCK";
            

            // Agregamos Columnas al DataGridView
            dt.Columns.Add(columna1);
            dt.Columns.Add(columna2);
            dt.Columns.Add(columna3);
            dt.Columns.Add(columna4);
            dt.Columns.Add(columna5);

            foreach (PRODUCTO producto in ListadoProducto())
            {
                dt.Rows.Add(producto.IDPRODUCTO, producto.DESCRIPCION, producto.TIPOPRODUCTO1.DESCRIPCION, producto.PRECIO, producto.STOCK);
            }



            dt.ReadOnly = true;


        }

        public bool AgregarProducto(string descripcion, int stock, int precio, string tipoproducto)
        {
            ServiceProducto sp = new ServiceProducto();
            ServiceTipoProducto stp = new ServiceTipoProducto();

            TIPOPRODUCTO tp = stp.getEntity(tipoproducto);
            try
            {
                // Crear producto
                PRODUCTO entity = new PRODUCTO();
                entity.IDPRODUCTO = sp.id();
                entity.DESCRIPCION = descripcion;
                entity.STOCK = stock;
                entity.PRECIO = precio;
                entity.TIPOPRODUCTO = tp.IDTIPO;
                entity.ADMINISTRADOR = 1;
                sp.addEntity(entity);

               
                MessageBox.Show("Producto Creado.", "Crear Producto", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
                return true;

            }catch(Exception ex)
            {

             MessageBox.Show("El producto ya existe.", "Crear Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return false;
                throw new ArgumentException(ex.Message);
            }
               

        }

       
        public bool ModificarProducto(string descripcion, int id, int stock, int precio, string tipoproducto)
        {
            try
            {
                ServiceProducto sp = new ServiceProducto();
                ServiceTipoProducto stp = new ServiceTipoProducto();

                TIPOPRODUCTO tp = stp.getEntity(tipoproducto);

                PRODUCTO entity = new PRODUCTO();
                entity.IDPRODUCTO = id;
                entity.DESCRIPCION = descripcion;
                entity.STOCK = stock;
                entity.PRECIO = precio;
                entity.TIPOPRODUCTO = tp.IDTIPO;

                sp.updEntity(entity);

                
                MessageBox.Show("Producto Modificado.", "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
                return true;
            }
            catch (Exception ex)
            {
                MessageBox.Show("No se pudo modificar el producto."+ex.Message, "Modificar Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return false;
            }





        }

       


        public void LlenarCampos(int id, TextBox descripcion, TextBox stock, TextBox precio, ComboBox tipoproducto, Label idlabel)
        {
            ServiceProducto sp = new ServiceProducto();
            ServiceTipoProducto stp = new ServiceTipoProducto();


            PRODUCTO p = sp.getEntity(id);

            this.LlenarComboTipo(tipoproducto);

            descripcion.Text = p.DESCRIPCION;
            stock.Text = p.STOCK.ToString();
            tipoproducto.SelectedIndex = (int)p.TIPOPRODUCTO - 1;
            idlabel.Text = p.IDPRODUCTO.ToString();
            precio.Text = p.PRECIO.ToString();


        }

        public void LlenarComboTipo(ComboBox tipo)
        {
            ServiceTipoProducto stp = new ServiceTipoProducto();
            List<TIPOPRODUCTO> lista = stp.getEntities();

            tipo.Items.Clear();
            tipo.DropDownStyle = ComboBoxStyle.DropDownList;

            foreach (TIPOPRODUCTO ts in lista)
            {
                tipo.Items.Add(ts.DESCRIPCION);
            }

        }

        public void EliminarProducto(int id)
        {
            ServiceProducto sp = new ServiceProducto();

            PRODUCTO p = sp.getEntity(id);

            if (MessageBox.Show("Esta seguro de que desea eliminar el producto: " + p.DESCRIPCION + "?", "Eliminar Producto", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Warning) == DialogResult.Yes)
            {
                sp.delEntity(p.IDPRODUCTO);
                MessageBox.Show("Producto Eliminado", "Eliminar Producto", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
            }

        }

        public bool AgregarTipoProducto(string descripcion)
        {
            ServiceTipoProducto stp = new ServiceTipoProducto();
            TIPOPRODUCTO tp = new TIPOPRODUCTO();

            try
            {
                tp.IDTIPO = stp.id();
                tp.DESCRIPCION = descripcion;
                stp.addEntity(tp);

                MessageBox.Show("Tipo Producto Agregado.", "Crear Tipo Producto", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
                return true;
            } catch (Exception ex)
            {
                MessageBox.Show("No se pudo agregar el tipo de producto", "Crear Tipo Producto", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return false;
            }
  
           
        }














    }
}
