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
    
    public partial class FACTURA
    {
        public FACTURA()
        {
            this.DETALLEFACTURA = new HashSet<DETALLEFACTURA>();
        }
    
        public long IDFACTURA { get; set; }
        public string GIRO { get; set; }
        public System.DateTime FECHAFACTURA { get; set; }
        public Nullable<System.DateTime> FECHAPAGO { get; set; }
        public long CLIENTE { get; set; }
        public long ESTADOFACTURA { get; set; }
    
        public virtual CLIENTE CLIENTE1 { get; set; }
        public virtual ICollection<DETALLEFACTURA> DETALLEFACTURA { get; set; }
        public virtual ESTADOFACTURA ESTADOFACTURA1 { get; set; }
    }
}
