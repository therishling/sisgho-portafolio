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
    
    public partial class PROVEEDOR
    {
        public PROVEEDOR()
        {
            this.DETALLEPEDIDO = new HashSet<DETALLEPEDIDO>();
            this.PRODUCTO = new HashSet<PRODUCTO>();
        }
    
        public long IDPROVEEDOR { get; set; }
        public string RUBRO { get; set; }
        public long TELEFONO { get; set; }
        public string DESCRIPCION { get; set; }
        public string SITIOWEB { get; set; }
        public long USUARIO { get; set; }
    
        public virtual ICollection<DETALLEPEDIDO> DETALLEPEDIDO { get; set; }
        public virtual ICollection<PRODUCTO> PRODUCTO { get; set; }
        public virtual USUARIO USUARIO1 { get; set; }
    }
}
