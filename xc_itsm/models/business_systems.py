from odoo import models, fields


class BusinessSystems(models.Model):
    _name = 'business.systems'
    _description = '业务系统'

    system_name = fields.Char(string='系统名称', required=True)
    system_admin = fields.Char(string='系统管理员', required=True)
    server_ip = fields.Char(string='服务器ip', required=True)
    server_account = fields.Char(string='服务器账号', required=True)
    server_password = fields.Char(string='服务器密码', required=True)
    config_information = fields.Char(string='硬件配置信息')
    environment_and_version = fields.Char(string='部署系统环境与版本', required=True)
    deploy_way = fields.Char(string='部署方式', required=True)
    config_path = fields.Char(string='部署路径', required=True)
    middle_config_way = fields.Char(string='中间件部署方式')
    middle_config_path = fields.Char(string='中间件部署路径')
    middle_config_environment = fields.Char(string='中间件部署环境')
    linux_command = fields.Text(string='常用linux命令')
    report_sql = fields.Text(string='常用报表SQL')
    profile_backup = fields.Char(string='配置文件备份信息')
    third_docking = fields.Char(string='第三方对接方式')
    third_target_data = fields.Char(string='第三方目标系统地址')
    third_db_Information = fields.Char(string='第三方数据库信息')
    attachment = fields.Binary(string='附件')
