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
    
    public partial class AUTH_PERMISSION
    {
        public AUTH_PERMISSION()
        {
            this.AUTH_GROUP_PERMISSIONS = new HashSet<AUTH_GROUP_PERMISSIONS>();
            this.AUTH_USER_USER_PERMISSIONS = new HashSet<AUTH_USER_USER_PERMISSIONS>();
        }
    
        public long ID { get; set; }
        public string NAME { get; set; }
        public long CONTENT_TYPE_ID { get; set; }
        public string CODENAME { get; set; }
    
        public virtual ICollection<AUTH_GROUP_PERMISSIONS> AUTH_GROUP_PERMISSIONS { get; set; }
        public virtual DJANGO_CONTENT_TYPE DJANGO_CONTENT_TYPE { get; set; }
        public virtual ICollection<AUTH_USER_USER_PERMISSIONS> AUTH_USER_USER_PERMISSIONS { get; set; }
    }
}
