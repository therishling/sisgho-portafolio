using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CapaDatos
{
    public class ServiceTipoProducto : AbstractService<TIPOPRODUCTO>
    {
        public override void addEntity(TIPOPRODUCTO entity)
        {
            em.TIPOPRODUCTO.Add(entity);
            em.SaveChanges();
        }

        public override void delEntity(object pk)
        {
            throw new NotImplementedException();
        }

        public override List<TIPOPRODUCTO> getEntities()
        {
            return em.TIPOPRODUCTO.ToList<TIPOPRODUCTO>();
        }

        public override TIPOPRODUCTO getEntity(object pk)
        {
            string tipo = pk.ToString();
            TIPOPRODUCTO tp = em.TIPOPRODUCTO.Where(q => q.DESCRIPCION.Equals(tipo)).FirstOrDefault<TIPOPRODUCTO>();
            return tp;
        }

        public override void updEntity(TIPOPRODUCTO entity)
        {
            throw new NotImplementedException();
        }

        public int id()
        {
            TIPOPRODUCTO tp = em.TIPOPRODUCTO.OrderByDescending(x => x.IDTIPO).FirstOrDefault<TIPOPRODUCTO>();
            int id = 1;
            if (tp == null)
            {
                return id;
            }
            else
            {
                return (int)tp.IDTIPO + 1;
            }

        }
    }
}
