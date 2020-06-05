namespace CapaPresentacion.Modulos.Producto
{
    partial class FormularioProducto
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.linkProv = new System.Windows.Forms.LinkLabel();
            this.labelPoducto = new System.Windows.Forms.Label();
            this.btnEliminarPro = new System.Windows.Forms.Button();
            this.btnModificarPro = new System.Windows.Forms.Button();
            this.btnAgregarPro = new System.Windows.Forms.Button();
            this.dataProd = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.dataProd)).BeginInit();
            this.SuspendLayout();
            // 
            // linkProv
            // 
            this.linkProv.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.linkProv.AutoSize = true;
            this.linkProv.LinkColor = System.Drawing.Color.White;
            this.linkProv.Location = new System.Drawing.Point(751, 476);
            this.linkProv.Name = "linkProv";
            this.linkProv.Size = new System.Drawing.Size(93, 13);
            this.linkProv.TabIndex = 23;
            this.linkProv.TabStop = true;
            this.linkProv.Text = "¿Necesita ayuda?";
            // 
            // labelPoducto
            // 
            this.labelPoducto.AutoSize = true;
            this.labelPoducto.Font = new System.Drawing.Font("Century Gothic", 15F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.labelPoducto.ForeColor = System.Drawing.Color.White;
            this.labelPoducto.Location = new System.Drawing.Point(12, 17);
            this.labelPoducto.Name = "labelPoducto";
            this.labelPoducto.Size = new System.Drawing.Size(108, 23);
            this.labelPoducto.TabIndex = 22;
            this.labelPoducto.Text = "Productos";
            // 
            // btnEliminarPro
            // 
            this.btnEliminarPro.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnEliminarPro.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnEliminarPro.Font = new System.Drawing.Font("Century Gothic", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnEliminarPro.ForeColor = System.Drawing.Color.White;
            this.btnEliminarPro.Location = new System.Drawing.Point(208, 403);
            this.btnEliminarPro.Name = "btnEliminarPro";
            this.btnEliminarPro.Size = new System.Drawing.Size(92, 48);
            this.btnEliminarPro.TabIndex = 21;
            this.btnEliminarPro.Text = "Eliminar Producto";
            this.btnEliminarPro.UseVisualStyleBackColor = true;
            this.btnEliminarPro.Click += new System.EventHandler(this.btnEliminarPro_Click);
            // 
            // btnModificarPro
            // 
            this.btnModificarPro.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnModificarPro.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnModificarPro.Font = new System.Drawing.Font("Century Gothic", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnModificarPro.ForeColor = System.Drawing.Color.White;
            this.btnModificarPro.Location = new System.Drawing.Point(110, 403);
            this.btnModificarPro.Name = "btnModificarPro";
            this.btnModificarPro.Size = new System.Drawing.Size(92, 48);
            this.btnModificarPro.TabIndex = 20;
            this.btnModificarPro.Text = "Modificar Producto";
            this.btnModificarPro.UseVisualStyleBackColor = true;
            this.btnModificarPro.Click += new System.EventHandler(this.btnModificarPro_Click);
            // 
            // btnAgregarPro
            // 
            this.btnAgregarPro.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.btnAgregarPro.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnAgregarPro.Font = new System.Drawing.Font("Century Gothic", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnAgregarPro.ForeColor = System.Drawing.Color.White;
            this.btnAgregarPro.Location = new System.Drawing.Point(12, 403);
            this.btnAgregarPro.Name = "btnAgregarPro";
            this.btnAgregarPro.Size = new System.Drawing.Size(92, 48);
            this.btnAgregarPro.TabIndex = 19;
            this.btnAgregarPro.Text = "Agregar Producto";
            this.btnAgregarPro.UseVisualStyleBackColor = true;
            this.btnAgregarPro.Click += new System.EventHandler(this.btnAgregarPro_Click);
            // 
            // dataProd
            // 
            this.dataProd.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.dataProd.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataProd.Location = new System.Drawing.Point(12, 66);
            this.dataProd.Name = "dataProd";
            this.dataProd.Size = new System.Drawing.Size(832, 304);
            this.dataProd.TabIndex = 18;
            // 
            // FormularioProducto
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(31)))), ((int)(((byte)(30)))), ((int)(((byte)(68)))));
            this.ClientSize = new System.Drawing.Size(856, 506);
            this.Controls.Add(this.linkProv);
            this.Controls.Add(this.labelPoducto);
            this.Controls.Add(this.btnEliminarPro);
            this.Controls.Add(this.btnModificarPro);
            this.Controls.Add(this.btnAgregarPro);
            this.Controls.Add(this.dataProd);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "FormularioProducto";
            this.Text = "FormularioProducto";
            this.Load += new System.EventHandler(this.FormularioProducto_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataProd)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.LinkLabel linkProv;
        private System.Windows.Forms.Label labelPoducto;
        private System.Windows.Forms.Button btnEliminarPro;
        private System.Windows.Forms.Button btnModificarPro;
        private System.Windows.Forms.Button btnAgregarPro;
        public System.Windows.Forms.DataGridView dataProd;
    }
}