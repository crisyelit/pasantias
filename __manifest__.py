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

{
    'name': 'Pasantias',
    'version': '0.1',
    'author': 'Ing. Jhuliana Delgado',
    'website': 'https://www.tucusitogroup.odoo.com',
    'category': 'Gestion',
    'sequence': 15,
    'summary': 'Gestión Integral de los Procesos de Pasantías',
    'description': """ Módulo para la Gestión Integral de los Procesos de Pasantías
        Este modulo permite registrar todo los estudiantes a nivel tecnico medio y Universitario 
    que necesitan realizar una pasantia para culminacion de su carrera, donde seran asignados 
    por medio de un contrato a una Empresa sea privada o publica a ejecutar su pasantia.

        Donde se apoya con Formularios para registro pasantes, institutos, empresas y contrato; 
    General reportes de statud de contrato, filtros de pasantes activos, facturas pagadas o pendientes, 
    Facturacion del contrato, como promotores a cargo del contrato. """,
    'depends': ['base'],
    'data': ['security/ir.model.access.csv', 'views/pasantias_view.xml', 'reports/reports.xml'],
    'demo': [ ],
    'css': [ ],
    'update_xml': [ ],
    'installable': True,
    'auto_install': False,
    'application': True,
}