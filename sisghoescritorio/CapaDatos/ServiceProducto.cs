using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CapaDatos
{
    public class ServiceProducto : AbstractService<PRODUCTO>
    {
        public override void addEntity(PRODUCTO entity)
        {
            em.PRODUCTO.Add(entity);
            em.SaveChanges();
        }

        public override void delEntity(object pk)
        {
            PRODUCTO pro = this.getEntity(pk);
            if (pro == null)
            {
                throw new ArgumentException("Producto no encontrado");

            }
            else
            {
                em.PRODUCTO.Remove(pro);
                em.SaveChanges();
            }
        }

        public override List<PRODUCTO> getEntities()
        {
            return em.PRODUCTO.ToList<PRODUCTO>();
        }

        public override PRODUCTO getEntity(object pk)
        {
            int id = int.Parse(pk.ToString());
            PRODUCTO pro = em.PRODUCTO.Where(q => q.IDPRODUCTO == id).FirstOrDefault<PRODUCTO>();

            return pro;
        }

        public override void updEntity(PRODUCTO entity)
        {
            PRODUCTO pro = this.getEntity(entity.IDPRODUCTO);
            if (pro == null)
            {
                throw new ArgumentException("Producto no encontrado");
            }
            else
            {
                pro.DESCRIPCION = entity.DESCRIPCION;
                pro.STOCK = entity.STOCK;
                pro.PRECIO = entity.PRECIO;
                pro.TIPOPRODUCTO = entity.TIPOPRODUCTO;
                pro.PROVEEDOR = entity.PROVEEDOR;
                em.SaveChanges();
            }
        }


        public int id()
        {
            PRODUCTO prod = em.PRODUCTO.OrderByDescending(x => x.IDPRODUCTO).FirstOrDefault<PRODUCTO>();
            int id = 1;
            if (prod == null)
            {
                return id;
            }
            else
            {
                return (int)prod.IDPRODUCTO + 1;
            }

        }




    }
}
