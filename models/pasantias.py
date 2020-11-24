# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Solución ERP de código abierto
#
#    Este programa es software libre: se puede redistribuir y / o modificar
#    bajo los términos de la GNU Affero General Public License
#
#    Debería haber recibido una copia de la Licencia Pública General GNU Affero
#    Junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import api, fields, models, api, exceptions;
from datetime import timedelta;

class pasantias(models.Model):
    """Tabla de Registro Maestro de Pasantias"""
    _name = 'pasantias'
    _description = "Pasantias"
    _order = 'convenios_id'
    #_rec_name = ''
    pasante_id = fields.Many2one('res.partner', string='Pasante', required=True, readonly=False, help='Pasante que realiza esta pasantia')
    convenios_id = fields.Many2one('convenios',string= 'Convenio', required=True, readonly=False, help='Convenio dentro del cual se incorporo esta pasantia')
    promotor_id = fields.Many2one('promotores', string='Promotor', required=True, readonly=False, help='Promotor asignado')
    departamento_area = fields.Char(string='Departamento asignado o area', default='Departamento asignado', size=64,required='True', traslate=True, readonly=False, copy=True, help='Departameto asignado o area donde realiza pasantia')
    tipo_pasantias_id = fields.Many2one('tipos.pasantias', string='Tipo de pasantia', required=True, readonly=False, help='Tipo de pasantia realizada')
    condicion_nofirmantes_id = fields.Many2one('condicion.nofirmante',string='Condicion no firmante', requered=True, readonly=False, help='Empresas o Institucines que no firman convenio')
    pasantia_desde = fields.Date(string='Pasantia desde', required=True, readonly=False, copy=False, help='Fecha de inicio de pasantia')
    pasantia_hasta = fields.Date(string='Pasantia hasta', required=True, readonly=False, copy=False, help='Fecha culminacion de pasantia')
    numero_semana = fields.Integer(string='Numero de semana',default=0, size=2,required='True', readonly=False, copy=False, help='Numero de semanas de duracion de la pasantia')
    turnos_id = fields.Many2one('turnos', string='Turno', required=True, readonly=False, copy=False, help='Turno de la pasantia')
    fecha_recepcion = fields.Date(string='Fecha de Recepcion documentos', required=True, readonly=False, copy=False, help='Fecha de recepcion de pasantia')
    prorroga_desde = fields.Date(string='Prorroga desde', required=False, readonly=False, copy=False, help='Fecha de inicio Prorroga de Pasantia')
    prorroga_hasta = fields.Date(string='Prorroga hasta', required=False, readonly=False, copy=False, help='Fecha de culminacion Prorroga')
    semana_prorroga = fields.Integer(string='Semana Prorroga', default=0, required=False, readonly=False, copy=False, help='Numero de semanas de prorroga')
    turno_prorroga_id = fields.Many2one('turnos', string='Turno de la prorroga', required=False, readonly=False, copy=False, help='Turno de la prorroga')
    condiciones_registro_id = fields.Many2one('condiciones.registro', string='Condicion de registro', required=True, readonly=False, copy=False, help='Condicion del registro de pasante')
    observacion = fields.Text('Observaciones', help='Observaciones de pasantia')
    observaciones_prorroga = fields.Text('Observacion de prorroga', help='Observaciones de la prorroga')
    nivel_academico_id = fields.Many2one('nivel_academico', string='Nivel Academico de la Pasantia', required=True, readonly=False, copy=False, help='Indica el nivel academico en la cual realizara su pasantia')
    nombre_instituto_id = fields.Many2one('instituciones', string='Instituto Procedente', required=True, readonly=False, copy=False, help='Instituto que procede el estudiante a realiza la pasantia')
    beneficiario_ids = fields.One2many('beneficiarios', 'beneficiario_id', string='Beneficiario', required=False, readonly=False, copy=False, help='Beneficiario de los aporte del seguro del pasante en caso de accidentes')
    active = fields.Boolean(string="Activo", help="activar o desactivar el registro", default=True)
    tipo_especialidades_id = fields.Many2one('tipo.especialidades', string='tipo especialidades', required=True, readonly=False, copy=False, help='Tipo de especialidad a realizar')

class tipos_alergias(models.Model):
    """Tabla referencial de tipos de alergias"""
    _name = 'tipos.alergias'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion del tipo de alergia')
    tipo_alergia = fields.Char(string='Tipo de Alergia', default='Tipo', size=20, traslate=True, readonly=False, required=False, copy=True, help='Indique el tipo de alergia')


class instituciones(models.Model):
    """Tabla Registro Maestro de Instituciones"""
    _inherit = 'res.company'
    #_rec_name = ''
    rif = fields.Char(string='RIF de la Institucion',default='RIF', traslate=True, readonly=False,  size=20, required=False, copy=True, help='RIF de la institucion')
    acronimo = fields.Char(string='Acronimo de la Institucion', default='Acronimo', size=20, traslate=True, readonly=False, required=False, copy=True, help='Acronimo de la Institucion')
    tipo_instituciones_id = fields.Many2one('tipos.instituciones', string='Tipo de Institucion', required=True, readonly=False, help='Tipo de Institucion')
    user_ids = fields.Many2many('res.users', 'instituciones_users_rel', 'cid', 'user_id', string='Accepted Users')
    

class tipos_pasantias(models.Model):
    """Tabla referencial de tipos de pasantias"""
    _name = 'tipos.pasantias'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion de tipo de pasantia')
    tipo_pasantia = fields.Char(string='Tipo de pasantia', default='Tipo', size=3, traslate=True, readonly=False, required=False, copy=True, help='Nombre el tipo de pasantia')

class pasantes(models.Model):
    """Tabla de Registro Maestro de Pasantes"""
    # _name = 'pasantes'
    _inherit = 'res.partner'
    #_rec_name = ''
    cedula = fields.Integer(string='Numero de cedula', default=0, size=20, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion del pasante')
    zurdo = fields.Selection([('si', 'SI'),('no', 'NO')],string='Es Zurdo?', default='no', store=True, readonly=False, copy=False, help='Es Zurdo?')
    alergias = fields.Selection([('si','SI'),('no','NO')], string='Es alergico?', default='no', store=True, readonly=False, copy=False, help='Es alergico?')
    tipo_alergia = fields.Many2one('tipos.alergias','Indique alergia', help='Tipos de alergias que posee')
    especialidad = fields.Many2one('tipo.especialidades', string='Tipo de Especialidad', required=True, readonly=False, help='Tipos de especialidades que posee')
    nivel_educativo = fields.Selection([('tm','TM'),('tsu','TSU'),('univ','UNIV')],string= 'Nivel de Educacion', default='tm', store=True, readonly=False, copy=False, help='Indique el nivel academico que posee')
    # channel_ids = fields.Many2many('mail.channel',  string='Canales')
    # visitor_ids = ''
    # meeting_ids = ''
    #razon_social_ids = fields.One2many('res.company','Empresa', string='Razon social de la Institucion',default='Razon social', traslate=True,  size=20, required='True', copy=True, help='Razon social de la Institucion')
    empresa_ids = fields.One2many('convenios', 'empresa_id', string="Empresa", readonly=True, required=True, copy=False, help='Empresa donde se ejecuta la pasantia')
    instructor = fields.Boolean("Instructor", default=False)
    
class tipo_especialidades(models.Model):
    """Tabla referencial de tipos de Especialidades"""
    _name = 'tipo.especialidades'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion del tipo de alergia')
    tipo_especialidades = fields.Char(string='Tipo de Especialidad', default='Tipo', size=20, traslate=True, readonly=False, required=False, copy=True, help='Nombre de la especialidad que posee')


class convenios(models.Model):
    """Tabla de Registro Maestro de Convenios"""
    _name = 'convenios'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo de Convenio', default='Convenio', size=10, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion del Convenio')
    empresa_id = fields.Many2one('res.partner', string='Empresa', required=True, readonly=False, help='Empresa con la que se celebra el convenio')
    fecha_inicio = fields.Date(string='Fecha inicio',  required=False, readonly=False, copy=False, help='Fecha de inicio de pasantia')
    fecha_final = fields.Date(string='Fecha Final',  required=False, readonly=False, copy=False, help='Fecha Final ')
    promotor_id = fields.Many2one('promotores', string='Promotor', required=True, readonly=False, help='Promotor que atiende la empresa')

    _sql_constraints = [('codigo_unid','UNIQUE(codigo)','El codigo debe ser unica!')]


class promotores(models.Model):
    """Tabla de Registro Maestro de Promotores"""
    _name = 'promotores'
    #_rec_name = ''
    cedula = fields.Char(string='Cedula', default='Cedula', size=10, traslate=True, readonly=False, required=False, copy=True, help='Cedula del promotor')
    nombre_promotor = fields.Char(string='Nombre del Promotor', default='Promotor', size=50, traslate=True, readonly=False, required=False, copy=True, help='Nombre del promotor')
    apellido_promotor = fields.Char(string='Apellido del promotor', default='Apellido', size=50, traslate=True, readonly=False, required=False, copy=True, help='Apellido del promotor')

class condicion_nofirmante(models.Model):
    """Tabla referencial de con dicion de no Firmantes"""
    _name = 'condicion.nofirmante'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion del tipo de alergia')
    condicion_nofirmante = fields.Char(string='Condicion de no firmante', default='Condicion de no firmante', size=3, traslate=True, readonly=False, required=False, copy=True, help='Condicion de no firmar de convenio')

class tipo_instituciones(models.Model):
    """Tabla referencial de tipos de Instituciones"""
    _name = 'tipo.instituciones'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion del tipo de alergia')
    tipo_instituciones = fields.Char(string='Tipo de Instituciones', default='Tipo', size=20, traslate=True, readonly=False, required=False, copy=True, help='Nombre de los tipos de Instituciones existente')

class beneficiarios(models.Model):
    """Tabla de Registro Maestro de Beneficiarios"""
    _name = 'beneficiarios'
    #_rec_name = ''
    beneficiario_id = fields.Many2one('pasantias', string='Beneficiarios', required=True, readonly=False, help='Beneficiario del pasante')
    nombre_beneficiario = fields.Char(string='Nombre del Beneficiario', default='Nombre', size=50, traslate=True, readonly=False, required=False, copy=True, help='Nombre del Beneficiario')
    apellido_beneficiario = fields.Char('Apellido del Beneficiario', default='Apellidos', size=50, traslate=True, readonly=False, required=False, copy=True, help='Apellido del Beneficiario')
    parentesco_beneficiario_id = fields.Many2one('parentescos', string='Parentesco del Beneficiario', required=True, readonly=False, help='Parentesco del Beneficiario')
    porcentaje = fields.Integer(string='Porcentaje', default=0,  required=True, readonly=False, copy=False, help='Porcentaje del Beneficiario')
    beneficiario_id = fields.Many2one('pasantias', string='Beneficiario', required=False, readonly=False, copy=False, help='Beneficiario de los aporte del seguro del pasante en caso de accidentes')

class parentescos(models.Model):
    """Tabla referencial de Parentesco"""
    _name = 'parentescos'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, traslate=True, readonly=False, required=False, copy=True, help='Codigo de identificacion del tipo de alergia')
    parentesco = fields.Char(string='Parentesco', size=120, required='True', traslate=True, readonly=False, copy=True, help='Tipo de parentesco')

class nivel_academico(models.Model):
    """Tabla de refer3encial de Niveles Academicos"""
    _name = 'nivel.academico'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, required='True', traslate=True, readonly=False, copy=True, help='Codigo de identificacion del nivel academico')
    nivel_academico = fields.Char(string='Nivel Educativo', size=120, required='True', traslate=True, readonly=False, copy=True, help='Descripcion corta del nivel educativo')

class condiciones_registro(models.Model):
    """Tabla referencial de Condiciones de Registro"""
    _name = 'condiciones.registro'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, required='True', traslate=True, readonly=False, copy=True, help='Codigo de identificacion de tipo de pasantia')
    condicion_registro = fields.Char(string='Condicion de Registro', default='Condicion de Registro', size=50, required='True', traslate=True, readonly=False, copy=True, help='Condicion deRegistro del pasante')

class turnos(models.Model):
    """Tabla referencial de turnos"""
    _name = 'turnos'
    #_rec_name = ''
    codigo = fields.Char(string='Codigo', default='Codigo', size=3, required='True', traslate=True, readonly=False, copy=True, help='Codigo de identificacion de turnos')
    turno = fields.Char(string='Turno', default='Turno', size=120, required='True', traslate=True, readonly=False, copy=True, help='Turno en la que cursa')