//------------------------------------------------------------------------------
// <auto-generated>
//    Este código se generó a partir de una plantilla.
//
//    Los cambios manuales en este archivo pueden causar un comportamiento inesperado de la aplicación.
//    Los cambios manuales en este archivo se sobrescribirán si se regenera el código.
// </auto-generated>
//------------------------------------------------------------------------------

namespace CapaDatos
{
    using System;
    using System.Collections.Generic;
    
    public partial class SERVICIOCOMEDOR
    {
        public SERVICIOCOMEDOR()
        {
            this.DETALLEFACTURA = new HashSet<DETALLEFACTURA>();
        }
    
        public long IDSERVICIO { get; set; }
        public string PLATO { get; set; }
        public long PRECIO { get; set; }
        public long ADMINISTRADOR { get; set; }
        public long TIPOSERVICIO { get; set; }
    
        public virtual ADMINISTRADOR ADMINISTRADOR1 { get; set; }
        public virtual ICollection<DETALLEFACTURA> DETALLEFACTURA { get; set; }
        public virtual TIPOSERVICIO TIPOSERVICIO1 { get; set; }
    }
}
