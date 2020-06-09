using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CapaDatos
{
    public class ServiceAdministrador : AbstractService<ADMINISTRADOR>
    {
        public override void addEntity(ADMINISTRADOR entity)
        {
            throw new NotImplementedException();
        }

        public override void delEntity(object pk)
        {
            
        }

        public override List<ADMINISTRADOR> getEntities()
        {
            throw new NotImplementedException();
        }

        public override ADMINISTRADOR getEntity(object pk)
        {
            int user = int.Parse(pk.ToString());
            ADMINISTRADOR adm = em.ADMINISTRADOR.Where(q => q.IDADMINISTRADOR == user).FirstOrDefault<ADMINISTRADOR>();

            return adm;
        }

        public override void updEntity(ADMINISTRADOR entity)
        {
            throw new NotImplementedException();
        }
    }
}
