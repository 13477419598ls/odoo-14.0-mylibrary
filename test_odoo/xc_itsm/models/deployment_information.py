from odoo import models, fields

class DeploymentInformation(models.Model):
    _name = 'deployment.information'
    _description = '部署信息'

    server_ip = fields.Char(string='服务器ip', required=True)
    server_account = fields.Char(string='服务器账号', required=True)
    server_password = fields.Char(string='服务器密码', required=True)
    config_information = fields.Char(string='硬件配置信息')
    environment = fields.Char(string='部署系统环境', required=True)
    version = fields.Char(string='版本', required=True)
    deploy_way = fields.Char(string='部署方式', required=True)
    config_path = fields.Char(string='部署路径', required=True)
    middle_name = fields.Char(string='中间件名称')
    middle_config_way = fields.Char(string='中间件部署方式')
    middle_config_path = fields.Char(string='中间件部署路径')
    middle_config_environment = fields.Char(string='中间件部署环境')

    information = fields.Many2one('business.systems', string='部署信息')
