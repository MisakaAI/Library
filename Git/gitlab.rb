#可以访问GitLab的URL。
external_url 'GENERATED_EXTERNAL_URL'

## Roles for multi-instance GitLab
##redis角色    redis_sentinel_role redis_master_role redis_replica_role
##gitlab geo角色   geo_primary_role geo_secondary_role
##postgres角色   postgres_role
##控制台角色   consul_role
##应用角色   application_role
##监控角色   monitoring_role
# roles ['redis_sentinel_role', 'redis_master_role']


################################################################################
################################################################################
##                Configuration Settings for GitLab CE and EE                 ##
################################################################################
################################################################################

#配置ssh方式拉取代码的host
# gitlab_rails['gitlab_ssh_host'] = 'ssh.host_example.com'
# gitlab_rails['gitlab_ssh_user'] = ''
# gitlab_rails['time_zone'] = 'UTC'

#配置最大请求时间单位为秒
# gitlab_rails['max_request_duration_seconds'] = 57

#GitLab邮件服务器设置
# gitlab_rails['smtp_enable'] = true
# gitlab_rails['smtp_address'] = "smtp.server"
# gitlab_rails['smtp_port'] = 465
# gitlab_rails['smtp_user_name'] = "smtp user"
# gitlab_rails['smtp_password'] = "smtp password"
# gitlab_rails['smtp_domain'] = "example.com"
# gitlab_rails['smtp_authentication'] = "login"
# gitlab_rails['smtp_enable_starttls_auto'] = true
# gitlab_rails['smtp_tls'] = false
# gitlab_rails['smtp_pool'] = false

# SMTP openssl验证模式,可选值 'none', 'peer', 'client_once', 'fail_if_no_peer_cert'
# gitlab_rails['smtp_openssl_verify_mode'] = 'none'

## smtp ca证书路径和文件
# gitlab_rails['smtp_ca_path'] = "/etc/ssl/certs"
# gitlab_rails['smtp_ca_file'] = "/etc/ssl/certs/ca-certificates.crt"

## 邮件设置是否开启
# gitlab_rails['gitlab_email_enabled'] = true

## 修改邮件发送者相关信息
# gitlab_rails['gitlab_email_from'] = 'example@example.com'
# gitlab_rails['gitlab_email_display_name'] = 'Example'
# gitlab_rails['gitlab_email_reply_to'] = 'noreply@example.com'
# gitlab_rails['gitlab_email_subject_suffix'] = ''
# gitlab_rails['gitlab_email_smime_enabled'] = false
# gitlab_rails['gitlab_email_smime_key_file'] = '/etc/gitlab/ssl/gitlab_smime.key'
# gitlab_rails['gitlab_email_smime_cert_file'] = '/etc/gitlab/ssl/gitlab_smime.crt'
# gitlab_rails['gitlab_email_smime_ca_certs_file'] = '/etc/gitlab/ssl/gitlab_smime_cas.crt'

## GitLab用户权限，是否可以创建组，是否可以修改用户名
# gitlab_rails['gitlab_default_can_create_group'] = true
# gitlab_rails['gitlab_username_changing_enabled'] = true
## gitlab主题 `1`  Indigo,`2` Dark,`3` Light,`4` Blue,`5` Green,`6`,Light Indigo,`7`Light Blue,`8`,Light Green,`9` Red,`10` Light Red
# gitlab_rails['gitlab_default_theme'] = 2

##默认项目功能设置,issues,merge_requests,wiki,snippets,builds,container_registry
# gitlab_rails['gitlab_default_projects_features_issues'] = true
# gitlab_rails['gitlab_default_projects_features_merge_requests'] = true
# gitlab_rails['gitlab_default_projects_features_wiki'] = true
# gitlab_rails['gitlab_default_projects_features_snippets'] = true
# gitlab_rails['gitlab_default_projects_features_builds'] = true
# gitlab_rails['gitlab_default_projects_features_container_registry'] = true

## 自动关闭issue的模式设置
# gitlab_rails['gitlab_issue_closing_pattern'] = "\b((?:[Cc]los(?:e[sd]?|ing)|\b[Ff]ix(?:e[sd]|ing)?|\b[Rr]esolv(?:e[sd]?|ing)|\b[Ii]mplement(?:s|ed|ing)?)(:?) +(?:(?:issues? +)?%{issue_ref}(?:(?:, *| +and +)?)|([A-Z][A-Z0-9_]+-\d+))+)"

## 下载的时候创建的临时文件存放路径
# gitlab_rails['gitlab_repository_downloads_path'] = 'tmp/repositories'

### 全球通用头像地址
# gitlab_rails['gravatar_plain_url'] = 'http://www.gravatar.com/avatar/%{hash}?s=%{size}&d=identicon'
# gitlab_rails['gravatar_ssl_url'] = 'https://secure.gravatar.com/avatar/%{hash}?s=%{size}&d=identicon'

##辅助工作配置
##定时任务暂停ci_jobs
# gitlab_rails['stuck_ci_jobs_worker_cron'] = "0 0 * * *"
##定时任务过期构建artifacts
# gitlab_rails['expire_build_artifacts_worker_cron'] = "*/7 * * * *"
##定时任务环境自动停止
# gitlab_rails['environments_auto_stop_cron_worker_cron'] = "24 * * * *"
##定时任务pipeline定期执行
# gitlab_rails['pipeline_schedule_worker_cron'] = "19 * * * *"
##定时任务ci_archive痕迹
# gitlab_rails['ci_archive_traces_cron_worker_cron'] = "17 * * * *"
##定时任务检查仓库
# gitlab_rails['repository_check_worker_cron'] = "20 * * * *"
##定时任务管理员邮箱
# gitlab_rails['admin_email_worker_cron'] = "0 0 * * 0"
##定时任务个人access_token过期
# gitlab_rails['personal_access_tokens_expiring_worker_cron'] = "0 1 * * *"
##定时任务个人access_token过期通知
# gitlab_rails['personal_access_tokens_expired_notification_worker_cron'] = "0 2 * * *"
##定时任务仓库archive缓存
# gitlab_rails['repository_archive_cache_worker_cron'] = "0 * * * *"
##定时任务页面域名验证
# gitlab_rails['pages_domain_verification_cron_worker'] = "*/15 * * * *"
##定时任务页面域名ssl证书消除验证
# gitlab_rails['pages_domain_ssl_renewal_cron_worker'] = "*/10 * * * *"
##定时任务页面域名消除验证
# gitlab_rails['pages_domain_removal_cron_worker'] = "47 0 * * *"
##定时任务删除未被接受的成员邀请
# gitlab_rails['remove_unaccepted_member_invites_cron_worker'] = "10 15 * * *"
##定期合并外部差异
# gitlab_rails['schedule_migrate_external_diffs_worker_cron'] = "15 * * * *"
##CI平台指标更新
# gitlab_rails['ci_platform_metrics_update_cron_worker'] = '47 9 * * *'
##分析使用趋势计数作业触发器
# gitlab_rails['analytics_usage_trends_count_job_trigger_worker_cron'] = "50 23 */1 * *"
##会员邀请提醒邮件
# gitlab_rails['member_invitation_reminder_emails_worker_cron'] = "0 0 * * *"
##用户状态清理批处理
# gitlab_rails['user_status_cleanup_batch_worker_cron'] = "* * * * *"
##产品营销邮件命名空间
# gitlab_rails['namespaces_in_product_marketing_emails_worker_cron'] = "0 9 * * *"
##SSH秘钥过期通知
# gitlab_rails['ssh_keys_expired_notification_worker_cron'] = "0 2 * * *"
##SSH密钥即将过期通知
# gitlab_rails['ssh_keys_expiring_soon_notification_worker_cron'] = "0 1 * * *"

## Webhook超时时间单位秒
# gitlab_rails['webhook_timeout'] = 10


##GraphQL 请求超时时间单位秒
# gitlab_rails['graphql_timeout'] = 30

##添加反向代理的IP地址
# gitlab_rails['trusted_proxies'] = []

##启用Content-Security-Policy标头
# gitlab_rails['content_security_policy'] = {
#  'enabled' => false,
#  'report_only' => false,
#  # Each directive is a String (e.g. "'self'").
#  'directives' => {
#    'base_uri' => nil,
#    'child_src' => nil,
#    'connect_src' => nil,
#    'default_src' => nil,
#    'font_src' => nil,
#    'form_action' => nil,
#    'frame_ancestors' => nil,
#    'frame_src' => nil,
#    'img_src' => nil,
#    'manifest_src' => nil,
#    'media_src' => nil,
#    'object_src' => nil,
#    'script_src' => nil,
#    'style_src' => nil,
#    'worker_src' => nil,
#    'report_uri' => nil,
#  }
# }

##定制应该由Rails提供的“host”头应用程序。 默认情况下，都是允许的。
# gitlab_rails['allowed_hosts'] = []

##监控端点访问的IP白名单
# gitlab_rails['monitoring_whitelist'] = ['127.0.0.0/8', '::1/128']

##关闭服务器设置，停止健康检查，但是继续接受应用请求的时间，单位秒
# gitlab_rails['shutdown_blackout_seconds'] = 10

##是否允许用户评论issues或者合并请求是发送邮件通知
# gitlab_rails['incoming_email_enabled'] = true

##接受电子邮件地址
# gitlab_rails['incoming_email_address'] = "gitlab-incoming+%{key}@gmail.com"

##邮箱用户名
# gitlab_rails['incoming_email_email'] = "gitlab-incoming@gmail.com"

##邮箱密码
# gitlab_rails['incoming_email_password'] = "[REDACTED]"

##IMAP邮箱设置
# gitlab_rails['incoming_email_host'] = "imap.gmail.com"
# gitlab_rails['incoming_email_port'] = 993
# gitlab_rails['incoming_email_ssl'] = true
# gitlab_rails['incoming_email_start_tls'] = false

##收到的邮件存放地方，默认收件箱
# gitlab_rails['incoming_email_mailbox_name'] = "inbox"
##IDLE命令超时时间单位秒
# gitlab_rails['incoming_email_idle_timeout'] = 60
##接受邮件的log文件路径
# gitlab_rails['incoming_email_log_file'] = "/var/log/gitlab/mailroom/mail_room_json.log"
##当邮件在发送后被删除时，是否将其从邮箱中永久删除
# gitlab_rails['incoming_email_expunge_deleted'] = false

##收件箱选项
# gitlab_rails['incoming_email_inbox_method'] = 'microsoft_graph'
# gitlab_rails['incoming_email_inbox_options'] = {
#    'tenant_id': 'YOUR-TENANT-ID',
#    'client_id': 'YOUR-CLIENT-ID',
#    'client_secret': 'YOUR-CLIENT-SECRET',
#    'poll_interval': 60  # Optional
# }

## 邮箱崩溃日志的格式
# mailroom['exit_log_format'] = "plain"

##对象存储配置
# gitlab_rails['object_store']['enabled'] = false
# gitlab_rails['object_store']['connection'] = {}
# gitlab_rails['object_store']['storage_options'] = {}
# gitlab_rails['object_store']['proxy_download'] = false
# gitlab_rails['object_store']['objects']['artifacts']['bucket'] = nil
# gitlab_rails['object_store']['objects']['external_diffs']['bucket'] = nil
# gitlab_rails['object_store']['objects']['lfs']['bucket'] = nil
# gitlab_rails['object_store']['objects']['uploads']['bucket'] = nil
# gitlab_rails['object_store']['objects']['packages']['bucket'] = nil
# gitlab_rails['object_store']['objects']['dependency_proxy']['bucket'] = nil
# gitlab_rails['object_store']['objects']['terraform_state']['bucket'] = nil

##是否支持job的artifacts
# gitlab_rails['artifacts_enabled'] = true
##artifacts存放路径
# gitlab_rails['artifacts_path'] = "/var/opt/gitlab/gitlab-rails/shared/artifacts"
##artifacts对象存储
# gitlab_rails['artifacts_object_store_enabled'] = false
# gitlab_rails['artifacts_object_store_direct_upload'] = false
# gitlab_rails['artifacts_object_store_background_upload'] = true
# gitlab_rails['artifacts_object_store_proxy_download'] = false
# gitlab_rails['artifacts_object_store_remote_directory'] = "artifacts"
# gitlab_rails['artifacts_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'host' => 's3.amazonaws.com',
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }

##外部合并请求差异
# gitlab_rails['external_diffs_enabled'] = false
# gitlab_rails['external_diffs_when'] = nil
# gitlab_rails['external_diffs_storage_path'] = "/var/opt/gitlab/gitlab-rails/shared/external-diffs"
# gitlab_rails['external_diffs_object_store_enabled'] = false
# gitlab_rails['external_diffs_object_store_direct_upload'] = false
# gitlab_rails['external_diffs_object_store_background_upload'] = false
# gitlab_rails['external_diffs_object_store_proxy_download'] = false
# gitlab_rails['external_diffs_object_store_remote_directory'] = "external-diffs"
# gitlab_rails['external_diffs_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'host' => 's3.amazonaws.com',
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }

##Git LFS
# gitlab_rails['lfs_enabled'] = true
# gitlab_rails['lfs_storage_path'] = "/var/opt/gitlab/gitlab-rails/shared/lfs-objects"
# gitlab_rails['lfs_object_store_enabled'] = false
# gitlab_rails['lfs_object_store_direct_upload'] = false
# gitlab_rails['lfs_object_store_background_upload'] = true
# gitlab_rails['lfs_object_store_proxy_download'] = false
# gitlab_rails['lfs_object_store_remote_directory'] = "lfs-objects"
# gitlab_rails['lfs_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'host' => 's3.amazonaws.com',
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }

## GitLab上传设置
# gitlab_rails['uploads_directory'] = "/var/opt/gitlab/gitlab-rails/uploads"
# gitlab_rails['uploads_storage_path'] = "/opt/gitlab/embedded/service/gitlab-rails/public"
# gitlab_rails['uploads_base_dir'] = "uploads/-/system"
# gitlab_rails['uploads_object_store_enabled'] = false
# gitlab_rails['uploads_object_store_direct_upload'] = false
# gitlab_rails['uploads_object_store_background_upload'] = true
# gitlab_rails['uploads_object_store_proxy_download'] = false
# gitlab_rails['uploads_object_store_remote_directory'] = "uploads"
# gitlab_rails['uploads_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'host' => 's3.amazonaws.com',
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }

##服务编排Terraform状态设置
# gitlab_rails['terraform_state_enabled'] = true
# gitlab_rails['terraform_state_storage_path'] = "/var/opt/gitlab/gitlab-rails/shared/terraform_state"
# gitlab_rails['terraform_state_object_store_enabled'] = false
# gitlab_rails['terraform_state_object_store_remote_directory'] = "terraform"
# gitlab_rails['terraform_state_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'host' => 's3.amazonaws.com',
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }

##GitLab 页面对象存储
# gitlab_rails['pages_object_store_enabled'] = false
# gitlab_rails['pages_object_store_remote_directory'] = "pages"
# gitlab_rails['pages_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'host' => 's3.amazonaws.com',
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }
# gitlab_rails['pages_local_store_enabled'] = true
# gitlab_rails['pages_local_store_path'] = "/var/opt/gitlab/gitlab-rails/shared/pages"

##Impersonation 设置
# gitlab_rails['impersonation_enabled'] = true

##设置应用设置缓存过期时间单位秒
# gitlab_rails['application_settings_cache_seconds'] = 60

##是否使用ping
# gitlab_rails['usage_ping_enabled'] = true

##GitLab Mattermosthost
# gitlab_rails['mattermost_host'] = "https://mattermost.example.com"

## LDAP 设置
# gitlab_rails['ldap_enabled'] = false
# gitlab_rails['prevent_ldap_sign_in'] = false

# gitlab_rails['ldap_servers'] = YAML.load <<-'EOS'
#   main: # 'main' is the GitLab 'provider ID' of this LDAP server
#     label: 'LDAP'
#     host: '_your_ldap_server'
#     port: 389
#     uid: 'sAMAccountName'
#     bind_dn: '_the_full_dn_of_the_user_you_will_bind_with'
#     password: '_the_password_of_the_bind_user'
#     encryption: 'plain' # "start_tls" or "simple_tls" or "plain"
#     verify_certificates: true
#     smartcard_auth: false
#     active_directory: true
#     allow_username_or_email_login: false
#     lowercase_usernames: false
#     block_auto_created_users: false
#     base: ''
#     user_filter: ''
#     ## EE only
#     group_base: ''
#     admin_group: ''
#     sync_ssh_keys: false
#
#   secondary: # 'secondary' is the GitLab 'provider ID' of second LDAP server
#     label: 'LDAP'
#     host: '_your_ldap_server'
#     port: 389
#     uid: 'sAMAccountName'
#     bind_dn: '_the_full_dn_of_the_user_you_will_bind_with'
#     password: '_the_password_of_the_bind_user'
#     encryption: 'plain' # "start_tls" or "simple_tls" or "plain"
#     verify_certificates: true
#     smartcard_auth: false
#     active_directory: true
#     allow_username_or_email_login: false
#     lowercase_usernames: false
#     block_auto_created_users: false
#     base: ''
#     user_filter: ''
#     ## EE only
#     group_base: ''
#     admin_group: ''
#     sync_ssh_keys: false
# EOS

##智能卡身份验证设置
# gitlab_rails['smartcard_enabled'] = false
# gitlab_rails['smartcard_ca_file'] = "/etc/gitlab/ssl/CA.pem"
# gitlab_rails['smartcard_client_certificate_required_host'] = 'smartcard.gitlab.example.com'
# gitlab_rails['smartcard_client_certificate_required_port'] = 3444
# gitlab_rails['smartcard_required_for_git_access'] = false
# gitlab_rails['smartcard_san_extensions'] = false

##Omni身份验证设置
# gitlab_rails['omniauth_enabled'] = nil
# gitlab_rails['omniauth_allow_single_sign_on'] = ['saml']
# gitlab_rails['omniauth_sync_email_from_provider'] = 'saml'
# gitlab_rails['omniauth_sync_profile_from_provider'] = ['saml']
# gitlab_rails['omniauth_sync_profile_attributes'] = ['email']
# gitlab_rails['omniauth_auto_sign_in_with_provider'] = 'saml'
# gitlab_rails['omniauth_block_auto_created_users'] = true
# gitlab_rails['omniauth_auto_link_ldap_user'] = false
# gitlab_rails['omniauth_auto_link_saml_user'] = false
# gitlab_rails['omniauth_auto_link_user'] = ['saml']
# gitlab_rails['omniauth_external_providers'] = ['twitter', 'google_oauth2']
# gitlab_rails['omniauth_allow_bypass_two_factor'] = ['google_oauth2']
# gitlab_rails['omniauth_providers'] = [
#   {
#     "name" => "google_oauth2",
#     "app_id" => "YOUR APP ID",
#     "app_secret" => "YOUR APP SECRET",
#     "args" => { "access_type" => "offline", "approval_prompt" => "" }
#   }
# ]

##FortiAuthenticator身份验证设置
# gitlab_rails['forti_authenticator_enabled'] = false
# gitlab_rails['forti_authenticator_host'] = 'forti_authenticator.example.com'
# gitlab_rails['forti_authenticator_port'] = 443
# gitlab_rails['forti_authenticator_username'] = 'admin'
# gitlab_rails['forti_authenticator_access_token'] = 's3cr3t'

##FortiToken云认证设置
# gitlab_rails['forti_token_cloud_enabled'] = false
# gitlab_rails['forti_token_cloud_client_id'] = 'forti_token_cloud_client_id'
# gitlab_rails['forti_token_cloud_client_secret'] = 's3cr3t'

##备份设置
# gitlab_rails['manage_backup_path'] = true
# gitlab_rails['backup_path'] = "/var/opt/gitlab/backups"
# gitlab_rails['backup_gitaly_backup_path'] = "/opt/gitlab/embedded/bin/gitaly-backup"

###! Docs: https://docs.gitlab.com/ee/raketasks/backup_restore.html#backup-archive-permissions
# gitlab_rails['backup_archive_permissions'] = 0644

# gitlab_rails['backup_pg_schema'] = 'public'

##备份存储多久后可以被删除单位秒
# gitlab_rails['backup_keep_time'] = 604800

# gitlab_rails['backup_upload_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AKIAKIAKI',
#   'aws_secret_access_key' => 'secret123',
#   # # If IAM profile use is enabled, remove aws_access_key_id and aws_secret_access_key
#   'use_iam_profile' => false
# }
# gitlab_rails['backup_upload_remote_directory'] = 'my.s3.bucket'
# gitlab_rails['backup_multipart_chunk_size'] = 104857600


##使用Amazon s3管理的密钥开启AWS服务器端加密备份
# gitlab_rails['backup_encryption'] = 'AES256'
# gitlab_rails['backup_encryption_key'] = '<base64-encoded encryption key>'

##Amazon S3 备份存储级别'STANDARD', 'STANDARD_IA', and 'REDUCED_REDUNDANCY'
# gitlab_rails['backup_storage_class'] = 'STANDARD'

##可以不用备份的部分，用逗号隔开
#gitlab_rails['env'] = {
#    "SKIP" => "db,uploads,repositories,builds,artifacts,lfs,registry,pages"
#}

## Pseudonymizer 设置
# gitlab_rails['pseudonymizer_manifest'] = 'config/pseudonymizer.yml'
# gitlab_rails['pseudonymizer_upload_remote_directory'] = 'gitlab-elt'
# gitlab_rails['pseudonymizer_upload_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AKIAKIAKI',
#   'aws_secret_access_key' => 'secret123'
# }


## 设置不同的数据的存储路径，如果你想用一个单独的目录来存储git数据，那么这个目录不能包含符号链接
# git_data_dirs({
#   "default" => {
#     "path" => "/mnt/nfs-01/git-data"
#    }
# })

##Gitaly设置
# gitlab_rails['gitaly_token'] = 'secret token'

##存储gitlab应用上传的文件，例如构建的artifacts，LFS 对象
# gitlab_rails['shared_path'] = '/var/opt/gitlab/gitlab-rails/shared'

##用于存储加密的配置文件
# gitlab_rails['encrypted_settings_path'] = '/var/opt/gitlab/gitlab-rails/shared/encrypted_settings'

##等待文件系统挂载
# high_availability['mountpoint'] = ["/var/opt/gitlab/git-data", "/var/opt/gitlab/gitlab-rails/shared"]

##GitLab Shell 设置
# gitlab_rails['gitlab_shell_ssh_port'] = 22
# gitlab_rails['gitlab_shell_git_timeout'] = 800

##其他的自定义设置
# gitlab_rails['extra_google_analytics_id'] = '_your_tracking_id'
# gitlab_rails['extra_google_tag_manager_id'] = '_your_tracking_id'
# gitlab_rails['extra_matomo_url'] = '_your_matomo_url'
# gitlab_rails['extra_matomo_site_id'] = '_your_matomo_site_id'
# gitlab_rails['extra_matomo_disable_cookies'] = false

##! Docs: https://docs.gitlab.com/omnibus/settings/environment-variables.html
# gitlab_rails['env'] = {
#   'BUNDLE_GEMFILE' => "/opt/gitlab/embedded/service/gitlab-rails/Gemfile",
#   'PATH' => "/opt/gitlab/bin:/opt/gitlab/embedded/bin:/bin:/usr/bin"
# }

# gitlab_rails['rack_attack_git_basic_auth'] = {
#   'enabled' => false,
#   'ip_whitelist' => ["127.0.0.1"],
#   'maxretry' => 10,
#   'findtime' => 60,
#   'bantime' => 3600
# }

##gitlab-rails目录log日志目录。不建议修改这里的配置
# gitlab_rails['dir'] = "/var/opt/gitlab/gitlab-rails"
# gitlab_rails['log_directory'] = "/var/log/gitlab/gitlab-rails"


##更改默认管理员的密码和共享runner的token，尽在应用初始化的时候设置
# gitlab_rails['initial_root_password'] = "password"
# gitlab_rails['initial_shared_runners_registration_token'] = "token"

##是否将root密码应该在初始化期间打印到STDOUT
# gitlab_rails['display_initial_root_password'] = false

##是否将root密码写入文件 /etc/gitlab/initial_root_password
# gitlab_rails['store_initial_root_password'] = true

##将路径设置为在引导GitLab时要使用的初始许可证。仅在初始化生效，后期修改需要在UI上修改，在此修改无效
# gitlab_rails['initial_license_file'] = '/etc/gitlab/company.gitlab-license'

##启用或禁用自动数据库迁移
# gitlab_rails['auto_migrate'] = true

##rake缓存清除，这是加载大型gitlab项目的高级特性
# gitlab_rails['rake_cache_clear'] = true

##gitlab 数据库设置
# gitlab_rails['db_adapter'] = "postgresql"
# gitlab_rails['db_encoding'] = "unicode"
# gitlab_rails['db_collation'] = nil
# gitlab_rails['db_database'] = "gitlabhq_production"
# gitlab_rails['db_username'] = "gitlab"
# gitlab_rails['db_password'] = nil
# gitlab_rails['db_host'] = nil
# gitlab_rails['db_port'] = 5432
# gitlab_rails['db_socket'] = nil
# gitlab_rails['db_sslmode'] = nil
# gitlab_rails['db_sslcompression'] = 0
# gitlab_rails['db_sslrootcert'] = nil
# gitlab_rails['db_sslcert'] = nil
# gitlab_rails['db_sslkey'] = nil
# gitlab_rails['db_prepared_statements'] = false
# gitlab_rails['db_statements_limit'] = 1000
# gitlab_rails['db_connect_timeout'] = nil
# gitlab_rails['db_keepalives'] = nil
# gitlab_rails['db_keepalives_idle'] = nil
# gitlab_rails['db_keepalives_interval'] = nil
# gitlab_rails['db_keepalives_count'] = nil
# gitlab_rails['db_tcp_user_timeout'] = nil
# gitlab_rails['db_application_name'] = nil


##gitlab redis设置
# gitlab_rails['redis_host'] = "127.0.0.1"
# gitlab_rails['redis_port'] = 6379
# gitlab_rails['redis_ssl'] = false
# gitlab_rails['redis_password'] = nil
# gitlab_rails['redis_database'] = 0
# gitlab_rails['redis_enable_client'] = true

##redis本地unix socket
# gitlab_rails['redis_socket'] = "/var/opt/gitlab/redis/redis.socket"

##redis sentinel支持
# gitlab_rails['redis_sentinels'] = [
#   {'host' => '127.0.0.1', 'port' => 26379},
# ]

##单独的实例支持
# gitlab_rails['redis_cache_instance'] = nil
# gitlab_rails['redis_cache_sentinels'] = nil
# gitlab_rails['redis_queues_instance'] = nil
# gitlab_rails['redis_queues_sentinels'] = nil
# gitlab_rails['redis_shared_state_instance'] = nil
# gitlab_rails['redis_shared_state_sentinels'] = nil
# gitlab_rails['redis_trace_chunks_instance'] = nil
# gitlab_rails['redis_trace_chunks_sentinels'] = nil
# gitlab_rails['redis_actioncable_instance'] = nil
# gitlab_rails['redis_actioncable_sentinels'] = nil

################################################################################
## Container Registry settings
##! Docs: https://docs.gitlab.com/ee/administration/container_registry.html
################################################################################

##registry对外的url
##registry_external_url 'https://registry.example.com'

##gitlab对registry的支持
# gitlab_rails['registry_enabled'] = true
# gitlab_rails['registry_host'] = "registry.gitlab.example.com"
# gitlab_rails['registry_port'] = "5005"
# gitlab_rails['registry_path'] = "/var/opt/gitlab/gitlab-rails/shared/registry"

##它用于验证通知请求到GitLab应用程序，如果你使用外部的registry服务，只需要改这里，如果不是，他将被通知设置覆盖
# gitlab_rails['registry_notification_secret'] = nil

##无需更改，如果你不知道这些配置是干嘛的
# gitlab_rails['registry_api_url'] = "http://localhost:5000"
# gitlab_rails['registry_key_path'] = "/var/opt/gitlab/gitlab-rails/certificate.key"
# gitlab_rails['registry_issuer'] = "omnibus-gitlab-issuer"

##注册应用程序使用的设置
# registry['enable'] = true
# registry['username'] = "registry"
# registry['group'] = "registry"
# registry['uid'] = nil
# registry['gid'] = nil
# registry['dir'] = "/var/opt/gitlab/registry"
# registry['registry_http_addr'] = "localhost:5000"
# registry['debug_addr'] = "localhost:5001"
# registry['log_directory'] = "/var/log/gitlab/registry"
# registry['env_directory'] = "/opt/gitlab/etc/registry/env"
# registry['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }
# registry['log_level'] = "info"
# registry['log_formatter'] = "text"
# registry['rootcertbundle'] = "/var/opt/gitlab/registry/certificate.crt"
# registry['health_storagedriver_enabled'] = true
# registry['storage_delete_enabled'] = true
# registry['validation_enabled'] = false
# registry['autoredirect'] = false
# registry['compatibility_schema1_enabled'] = false

##注册后端存储
# registry['storage'] = {
#   's3' => {
#     'accesskey' => 's3-access-key',
#     'secretkey' => 's3-secret-key-for-access-key',
#     'bucket' => 'your-s3-bucket',
#     'region' => 'your-s3-region',
#     'regionendpoint' => 'your-s3-regionendpoint'
#   },
#   'redirect' => {
#     'disable' => false
#   }
# }

##注册通知
# registry['notifications'] = [
#   {
#     'name' => 'test_endpoint',
#     'url' => 'https://gitlab.example.com/notify2',
#     'timeout' => '500ms',
#     'threshold' => 5,
#     'backoff' => '1s',
#     'headers' => {
#       "Authorization" => ["AUTHORIZATION_EXAMPLE_TOKEN"]
#     }
#   }
# ]
##注册的默认配置
# registry['default_notifications_timeout'] = "500ms"
# registry['default_notifications_threshold'] = 5
# registry['default_notifications_backoff'] = "1s"
# registry['default_notifications_headers'] = {}

##错误报告和日志
# gitlab_rails['sentry_enabled'] = false
# gitlab_rails['sentry_dsn'] = 'https://<key>@sentry.io/<project>'
# gitlab_rails['sentry_clientside_dsn'] = 'https://<key>@sentry.io/<project>'
# gitlab_rails['sentry_environment'] = 'production'

##用于签名CI JOB JWT的RSA私钥
# gitlab_rails['ci_jwt_signing_key'] = nil # Will be generated if not set.


##Gitlab Workhorse设置
# gitlab_workhorse['enable'] = true
# gitlab_workhorse['ha'] = false
# gitlab_workhorse['alt_document_root'] = nil
# gitlab_workhorse['shutdown_timeout'] = nil
# gitlab_workhorse['listen_network'] = "unix"
# gitlab_workhorse['listen_umask'] = 000
# gitlab_workhorse['listen_addr'] = "/var/opt/gitlab/gitlab-workhorse/sockets/socket"
# gitlab_workhorse['auth_backend'] = "http://localhost:8080"

##启用Redis keywatcher，如果这个设置不存在，它默认为true
# gitlab_workhorse['workhorse_keywatcher'] = true

##空字符串是gitlab-workhorse选项解析器中的默认值
# gitlab_workhorse['auth_socket'] = "''"

##在命令行上放置一个空字符串
# gitlab_workhorse['pprof_listen_addr'] = "''"

# gitlab_workhorse['prometheus_listen_addr'] = "localhost:9229"

# gitlab_workhorse['dir'] = "/var/opt/gitlab/gitlab-workhorse"
# gitlab_workhorse['log_directory'] = "/var/log/gitlab/gitlab-workhorse"
# gitlab_workhorse['proxy_headers_timeout'] = "1m0s"

##限制并发API请求的数量，默认为0，这是无限的
# gitlab_workhorse['api_limit'] = 0

##限制允许排队的API请求的数量，默认为0禁用排队
# gitlab_workhorse['api_queue_limit'] = 0

##在此之后，如果请求在队列中停留的时间太长，我们将请求超时
# gitlab_workhorse['api_queue_duration'] = "30s"

##为运行程序请求作业的长轮询时间
# gitlab_workhorse['api_ci_long_polling_duration'] = "60s"

##传播X-Request-Id(如果可用)。 否则Workhorse将生成一个随机值。
# gitlab_workhorse['propagate_correlation_id'] = false

##日志格式:默认是json，也可以是text或者none.
# gitlab_workhorse['log_format'] = "json"

# gitlab_workhorse['env_directory'] = "/opt/gitlab/etc/gitlab-workhorse/env"
# gitlab_workhorse['env'] = {
#   'PATH' => "/opt/gitlab/bin:/opt/gitlab/embedded/bin:/bin:/usr/bin",
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }

##允许并发执行的最大标量进程数。
# gitlab_workhorse['image_scaler_max_procs'] = 4

##用于重新缩放图像的最大文件大小(以字节计)
# gitlab_workhorse['image_scaler_max_filesize'] = 250000

################################################################################
## GitLab User Settings
##! Modify default git user.
##! Docs: https://docs.gitlab.com/omnibus/settings/configuration.html#changing-the-name-of-the-git-user-group
################################################################################

# user['username'] = "git"
# user['group'] = "git"
# user['uid'] = nil
# user['gid'] = nil

##! The shell for the git user
# user['shell'] = "/bin/sh"

##! The home directory for the git user
# user['home'] = "/var/opt/gitlab"

# user['git_user_name'] = "GitLab"
# user['git_user_email'] = "gitlab@#{node['fqdn']}"


################################################################################
## GitLab Puma
##! Tweak puma settings. You should only use Unicorn or Puma, not both.
##! Docs: https://docs.gitlab.com/omnibus/settings/puma.html
################################################################################
##Puma是用于HTTP 1.1应用程序的多线程ruby服务器，要启用Puma，请确保禁用Unicorn
# puma['enable'] = true
# puma['ha'] = false
# puma['worker_timeout'] = 60
# puma['worker_processes'] = 2
# puma['min_threads'] = 4
# puma['max_threads'] = 4
# puma['listen'] = '127.0.0.1'
# puma['port'] = 8080
# puma['socket'] = '/var/opt/gitlab/gitlab-rails/sockets/gitlab.socket'
# puma['somaxconn'] = 1024
# puma['pidfile'] = '/opt/gitlab/var/puma/puma.pid'
# puma['state_path'] = '/opt/gitlab/var/puma/puma.state'

##不建议修改这个配置
# puma['log_directory'] = "/var/log/gitlab/puma"

## puma每个worker最大内存MB
# puma['per_worker_max_memory_mb'] = 1024

# puma['exporter_enabled'] = false
# puma['exporter_address'] = "127.0.0.1"
# puma['exporter_port'] = 8083

################################################################################
## GitLab Sidekiq
################################################################################
#sidekiq设置
# sidekiq['log_directory'] = "/var/log/gitlab/sidekiq"
# sidekiq['log_format'] = "json"
# sidekiq['shutdown_timeout'] = 4
# sidekiq['queue_selector'] = false
# sidekiq['interval'] = nil
# sidekiq['max_concurrency'] = 50
# sidekiq['min_concurrency'] = nil


##GitLab允许将作业路由到由数组确定的特定队列，设置路由规则
# sidekiq['routing_rules'] = []


##queue_groups数组中的每个条目表示一组必须由Sidekiq进程处理的队列。 多个队列可以用逗号分隔它们，' * '将处理所有队列
# sidekiq['queue_groups'] = ['*']

##如果启用了negate，那么Sidekiq将处理所有与queue_groups中的队列不匹配的队列
# sidekiq['negate'] = false

# sidekiq['metrics_enabled'] = true
# sidekiq['exporter_log_enabled'] = false
# sidekiq['listen_address'] = "localhost"
# sidekiq['listen_port'] = 8082

################################################################################
## gitlab-shell
################################################################################
##gitlab-shell配置
# gitlab_shell['audit_usernames'] = false
# gitlab_shell['log_level'] = 'INFO'
# gitlab_shell['log_format'] = 'json'
# gitlab_shell['http_settings'] = { user: 'username', password: 'password', ca_file: '/etc/ssl/cert.pem', ca_path: '/etc/pki/tls/certs', self_signed_cert: false}
# gitlab_shell['log_directory'] = "/var/log/gitlab/gitlab-shell/"
# gitlab_shell['custom_hooks_dir'] = "/opt/gitlab/embedded/service/gitlab-shell/hooks"

# gitlab_shell['auth_file'] = "/var/opt/gitlab/.ssh/authorized_keys"



# gitlab_shell['migration'] = { enabled: true, features: [] }
## gitlab trace log 文件啊
# gitlab_shell['git_trace_log_file'] = "/var/log/gitlab/gitlab-shell/gitlab-shell-git-trace.log"

## 这个路径不要改
# gitlab_shell['dir'] = "/var/opt/gitlab/gitlab-shell"

################################################################
## GitLab PostgreSQL
################################################################

##postgresql设置
# postgresql['enable'] = true
# postgresql['listen_address'] = nil
# postgresql['port'] = 5432


##仅在守护神启用时使用。 这是PostgreSQL响应其他的端口
# postgresql['connect_port'] = 5432

##建议1/4总内存RAM, 最大14GB
# postgresql['shared_buffers'] = "256MB"


# postgresql['ha'] = false
# postgresql['dir'] = "/var/opt/gitlab/postgresql"
# postgresql['log_directory'] = "/var/log/gitlab/postgresql"
# postgresql['log_destination'] = nil
# postgresql['logging_collector'] = nil
# postgresql['log_truncate_on_rotation'] = nil
# postgresql['log_rotation_age'] = nil
# postgresql['log_rotation_size'] = nil
# postgresql['username'] = "gitlab-psql"
# postgresql['group'] = "gitlab-psql"
##可以使用命令' gitlab-ctl pg-password-md5 gitlab '生成SQL_USER_PASSWORD_HASH '
# postgresql['sql_user_password'] = 'SQL_USER_PASSWORD_HASH'
# postgresql['uid'] = nil
# postgresql['gid'] = nil
# postgresql['shell'] = "/bin/sh"
# postgresql['home'] = "/var/opt/gitlab/postgresql"
# postgresql['user_path'] = "/opt/gitlab/embedded/bin:/opt/gitlab/bin:$PATH"
# postgresql['sql_user'] = "gitlab"
# postgresql['max_connections'] = 200
# postgresql['md5_auth_cidr_addresses'] = []
# postgresql['trust_auth_cidr_addresses'] = []
# postgresql['wal_buffers'] = "-1"
# postgresql['autovacuum_max_workers'] = "3"
# postgresql['autovacuum_freeze_max_age'] = "200000000"
# postgresql['log_statement'] = nil
# postgresql['track_activity_query_size'] = "1024"
# postgresql['shared_preload_libraries'] = nil
# postgresql['dynamic_shared_memory_type'] = nil
# postgresql['hot_standby'] = "off"
## SSL 设置
# postgresql['ssl'] = 'on'
# postgresql['hostssl'] = false
# postgresql['ssl_ciphers'] = 'HIGH:MEDIUM:+3DES:!aNULL:!SSLv3:!TLSv1'
# postgresql['ssl_cert_file'] = 'server.crt'
# postgresql['ssl_key_file'] = 'server.key'
# postgresql['ssl_ca_file'] = '/opt/gitlab/embedded/ssl/certs/cacert.pem'
# postgresql['ssl_crl_file'] = nil
# postgresql['cert_auth_addresses'] = {
#   'ADDRESS' => {
#     database: 'gitlabhq_production',
#     user: 'gitlab'
#   }
# }
##副本设置
# postgresql['wal_level'] = "hot_standby"
# postgresql['wal_log_hints'] = 'off'
# postgresql['max_wal_senders'] = 5
# postgresql['max_replication_slots'] = 0
# postgresql['max_locks_per_transaction'] = 128
# 备份设置
# postgresql['archive_mode'] = "off"
# postgresql['work_mem'] = "16MB"
# postgresql['maintenance_work_mem'] = "16MB"
# postgresql['checkpoint_timeout'] = "5min"
# postgresql['checkpoint_completion_target'] = 0.9
# postgresql['effective_io_concurrency'] = 1
# postgresql['checkpoint_warning'] = "30s"
# postgresql['effective_cache_size'] = "1MB"
# postgresql['shmmax'] =  17179869184 # or 4294967295
# postgresql['shmall'] =  4194304 # or 1048575
# postgresql['autovacuum'] = "on"
# postgresql['log_autovacuum_min_duration'] = "-1"
# postgresql['autovacuum_naptime'] = "1min"
# postgresql['autovacuum_vacuum_threshold'] = "50"
# postgresql['autovacuum_analyze_threshold'] = "50"
# postgresql['autovacuum_vacuum_scale_factor'] = "0.02"
# postgresql['autovacuum_analyze_scale_factor'] = "0.01"
# postgresql['autovacuum_vacuum_cost_delay'] = "20ms"
# postgresql['autovacuum_vacuum_cost_limit'] = "-1"
# postgresql['statement_timeout'] = "60000"
# postgresql['idle_in_transaction_session_timeout'] = "60000"
# postgresql['log_line_prefix'] = "%a"
# postgresql['max_worker_processes'] = 8
# postgresql['max_parallel_workers_per_gather'] = 0
# postgresql['log_lock_waits'] = 1
# postgresql['deadlock_timeout'] = '5s'
# postgresql['track_io_timing'] = 0
# postgresql['default_statistics_target'] = 1000
### 9.6后有效
# postgresql['min_wal_size'] = "80MB"
# postgresql['max_wal_size'] = "1GB"
# 备份设置
# postgresql['archive_command'] = nil
# postgresql['archive_timeout'] = "0"
##副本信息设置
# postgresql['sql_replication_user'] = "gitlab_replicator"
# postgresql['sql_replication_password'] = "md5 hash of postgresql password" # You can generate with `gitlab-ctl pg-password-md5 <dbuser>`
# postgresql['wal_keep_segments'] = 10
# postgresql['max_standby_archive_delay'] = "30s"
# postgresql['max_standby_streaming_delay'] = "30s"
# postgresql['synchronous_commit'] = on
# postgresql['synchronous_standby_names'] = ''
# postgresql['hot_standby_feedback'] = 'off'
# postgresql['random_page_cost'] = 2.0
# postgresql['log_temp_files'] = -1
# postgresql['log_checkpoints'] = 'off'
##添加自定义条目
# postgresql['custom_pg_hba_entries'] = {
#   APPLICATION: [ # APPLICATION should identify what the settings are used for
#     {
#       type: example,
#       database: example,
#       user: example,
#       cidr: example,
#       method: example,
#       option: example
#     }
#   ]
# }
##如果您禁用了绑定的PostgreSQL，但仍然想使用备份rake任务，请设置此参数
# postgresql['version'] = 10
################################################################################
## GitLab Redis
##! **Can be disabled if you are using your own Redis instance.**
##! Docs: https://docs.gitlab.com/omnibus/settings/redis.html
################################################################################
##gitlab redis设置
# redis['enable'] = true
# redis['ha'] = false
# redis['hz'] = 10
# redis['dir'] = "/var/opt/gitlab/redis"
# redis['log_directory'] = "/var/log/gitlab/redis"
# redis['username'] = "gitlab-redis"
# redis['group'] = "gitlab-redis"
# redis['maxclients'] = "10000"
# redis['maxmemory'] = "0"
# redis['maxmemory_policy'] = "noeviction"
# redis['maxmemory_samples'] = "5"
# redis['tcp_backlog'] = 511
# redis['tcp_timeout'] = "60"
# redis['tcp_keepalive'] = "300"
# redis['uid'] = nil
# redis['gid'] = nil
##禁用或混淆不必要的redis命令名
# redis['rename_commands'] = {
#   'KEYS': ''
#}
#
##配置此服务器的redis是主实例类型或副本实例类型，选择一个
# redis_master_role['enable'] = true
# redis_replica_role['enable'] = true
##Redis TCP支持(将禁用UNIX套接字传输)
# redis['bind'] = '0.0.0.0'
# redis['port'] = 6379
# redis['password'] = 'redis-password-goes-here'
## 是否为Master服务，默认是true
# redis['master'] = false # by default this is true
##副本和哨兵共享配置，两者都需要指向主Redis实例来获得复制和心跳监测
# redis['master_name'] = 'gitlab-redis'
# redis['master_ip'] = nil
# redis['master_port'] = 6379
##支持在Docker或NAT环境中运行redis副本
# redis['announce_ip'] = nil
# redis['announce_port'] = nil
##主节点master的密码
# redis['master_password'] = 'redis-password-goes-here'
##当您的副本无法赶上主副本时，请增加这些值
# redis['client_output_buffer_limit_normal'] = '0 0 0'
# redis['client_output_buffer_limit_replica'] = '256mb 64mb 60'
# redis['client_output_buffer_limit_pubsub'] = '32mb 8mb 60'
##redis快照的频率，[]为禁用，['']将覆盖前面的设置
# redis['save'] = [ '900 1', '300 10', '60 10000' ]
## redis懒惰的释放，默认都是false
# redis['lazyfree_lazy_eviction'] = true
# redis['lazyfree_lazy_expire'] = true
# redis['lazyfree_lazy_server_del'] = true
# redis['replica_lazy_flush'] = true
## redis线程数，默认不开启多线程
# redis['io_threads'] = 4
# redis['io_threads_do_reads'] = true
################################################################################
## GitLab Web server
##! Docs: https://docs.gitlab.com/omnibus/settings/nginx.html#using-a-non-bundled-web-server
################################################################################
##当捆绑nginx被禁用时，我们需要添加外部web服务器用户到gitlab webserver组中
# web_server['external_users'] = []
# web_server['username'] = 'gitlab-www'
# web_server['group'] = 'gitlab-www'
# web_server['uid'] = nil
# web_server['gid'] = nil
# web_server['shell'] = '/bin/false'
# web_server['home'] = '/var/opt/gitlab/nginx'
################################################################################
## GitLab NGINX
##! Docs: https://docs.gitlab.com/omnibus/settings/nginx.html
################################################################################
##gitlab nginx设置
# nginx['enable'] = true
# nginx['client_max_body_size'] = '250m'
# nginx['redirect_http_to_https'] = false
# nginx['redirect_http_to_https_port'] = 80
##默认情况下包含了大多数根CA证书
# nginx['ssl_client_certificate'] = "/etc/gitlab/ssl/ca.crt"
##启用/禁用双向SSL客户端身份验证
# nginx['ssl_verify_client'] = "off"
##如果ssl_verify_client on，表示客户端证书链中的验证深度
# nginx['ssl_verify_depth'] = "1"
# nginx['ssl_certificate'] = "/etc/gitlab/ssl/#{node['fqdn']}.crt"
# nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/#{node['fqdn']}.key"
# nginx['ssl_ciphers'] = "ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256"
# nginx['ssl_prefer_server_ciphers'] = "on"
##ssl 协议
# nginx['ssl_protocols'] = "TLSv1.2 TLSv1.3"
##ssl session缓存
# nginx['ssl_session_cache'] = "builtin:1000  shared:SSL:10m"
##ssl session 失效时间分钟
# nginx['ssl_session_timeout'] = "5m"
## dhparams.pem的路径
# nginx['ssl_dhparam'] = nil
# nginx['listen_addresses'] = ['*', '[::]']
##默认强制web浏览器总是使用HTTPS通信，hsts强制安全传输技术(Http Strict Transport Security)
##max age
# nginx['hsts_max_age'] = 31536000
##是否支持子域名
# nginx['hsts_include_subdomains'] = false
##默认情况下，在进行跨源请求时剥离路径信息
# nginx['referrer_policy'] = 'strict-origin-when-cross-origin'
##是否支持gzip
# nginx['gzip_enabled'] = true
##只有在使用反向代理时才重写,默认不写为80
# nginx['listen_port'] = nil
##仅当反向代理通过HTTP进行内部通信时才覆盖
# nginx['listen_https'] = nil
# nginx['custom_gitlab_server_config'] = "location ^~ /foo-namespace/bar-project/raw/ {\n deny all;\n}\n"
# nginx['custom_nginx_config'] = "include /etc/nginx/conf.d/example.conf;"
# nginx['proxy_read_timeout'] = 3600
# nginx['proxy_connect_timeout'] = 300
# nginx['proxy_set_headers'] = {
#  "Host" => "$http_host_with_default",
#  "X-Real-IP" => "$remote_addr",
#  "X-Forwarded-For" => "$proxy_add_x_forwarded_for",
#  "X-Forwarded-Proto" => "https",
#  "X-Forwarded-Ssl" => "on",
#  "Upgrade" => "$http_upgrade",
#  "Connection" => "$connection_upgrade"
# }
# nginx['proxy_cache_path'] = 'proxy_cache keys_zone=gitlab:10m max_size=1g levels=1:2'
# nginx['proxy_cache'] = 'gitlab'
# nginx['http2_enabled'] = true
# nginx['real_ip_trusted_addresses'] = []
# nginx['real_ip_header'] = nil
# nginx['real_ip_recursive'] = nil
# nginx['custom_error_pages'] = {
#   '404' => {
#     'title' => 'Example title',
#     'header' => 'Example header',
#     'message' => 'Example message'
#   }
# }
# nginx['dir'] = "/var/opt/gitlab/nginx"
# nginx['log_directory'] = "/var/log/gitlab/nginx"
# nginx['worker_processes'] = 4
# nginx['worker_connections'] = 10240
# nginx['log_format'] = '$remote_addr - $remote_user [$time_local] "$request_method $filtered_request_uri $server_protocol" $status $body_bytes_sent "$filtered_http_referer" "$http_user_agent" $gzip_ratio'
# nginx['sendfile'] = 'on'
# nginx['tcp_nopush'] = 'on'
# nginx['tcp_nodelay'] = 'on'
# nginx['hide_server_tokens'] = 'off'
# nginx['gzip_http_version'] = "1.0"
# nginx['gzip_comp_level'] = "2"
# nginx['gzip_proxied'] = "any"
# nginx['gzip_types'] = [ "text/plain", "text/css", "application/x-javascript", "text/xml", "application/xml", "application/xml+rss", "text/javascript", "application/json" ]
# nginx['keepalive_timeout'] = 65
# nginx['keepalive_time'] = '1h'
# nginx['cache_max_size'] = '5000m'
# nginx['server_names_hash_bucket_size'] = 64
##! These paths have proxy_request_buffering disabled
# nginx['request_buffering_off_path_regex'] = "/api/v\\d/jobs/\\d+/artifacts$|\\.git/git-receive-pack$|\\.git/gitlab-lfs/objects|\\.git/info/lfs/objects/batch$"
##Nginx 状态
# nginx['status'] = {
#  "enable" => true,
#  "listen_addresses" => ["127.0.0.1"],
#  "fqdn" => "dev.example.com",
#  "port" => 9999,
#  "vts_enable" => true,
#  "options" => {
#    "server_tokens" => "off", # Don't show the version of NGINX
#    "access_log" => "off", # Disable logs for stats
#    "allow" => "127.0.0.1", # Only allow access from localhost
#    "deny" => "all" # Deny access to anyone else
#  }
# }

################################################################################
## GitLab Logging
##! Docs: https://docs.gitlab.com/omnibus/settings/logs.html
################################################################################

## gitlab 日志管理
##在200 MB的日志数据之后进行循环
# logging['svlogd_size'] = 200 * 1024 * 1024
##保留30个循环的日志文件
# logging['svlogd_num'] = 30
##保留24小时
# logging['svlogd_timeout'] = 24 * 60 * 60
##压缩日志的格式gzip
# logging['svlogd_filter'] = "gzip"
##使用udp传输log信息
# logging['svlogd_udp'] = nil
##为log信息自定义前缀
# logging['svlogd_prefix'] = nil
##每天循环写日志
# logging['logrotate_frequency'] = "daily"
##当日志增长超过size字节时，甚至在指定的时间间隔(每日、每周、每月或每年)轮换日志
# logging['logrotate_maxsize'] = nil
##默认为log的大小循环写日志
# logging['logrotate_size'] = nil
##保留30个log
# logging['logrotate_rotate'] = 30
##日志压缩
# logging['logrotate_compress'] = "compress"
##log的方式，复制截断
# logging['logrotate_method'] = "copytruncate"
##默认没有postrotate命令
# logging['logrotate_postrotate'] = nil
##文件使用日期扩展名，如production.log-2016-03-09.gz
# logging['logrotate_dateformat'] = nil



##远程主机通过UDP发送日志消息
# logging['udp_log_shipping_host'] = nil


##覆盖通过UDP发送日志时使用的主机名，默认是系统的hostname
# logging['udp_log_shipping_hostname'] = nil

##通过UDP发送日志消息的远程端口
# logging['udp_log_shipping_port'] = 514

################################################################################
## Logrotate
##! Docs: https://docs.gitlab.com/omnibus/settings/logs.html#logrotate
##! You can disable built in logrotate feature.
################################################################################
##管理日志文件
# logrotate['enable'] = true
# logrotate['log_directory'] = "/var/log/gitlab/logrotate"

################################################################################
## Users and groups accounts
##! Disable management of users and groups accounts.
##! **Set only if creating accounts manually**
##! Docs: https://docs.gitlab.com/omnibus/settings/configuration.html#disable-user-and-group-account-management
################################################################################

##关闭用户和组帐号的管理。
# manage_accounts['enable'] = false

################################################################################
## Storage directories
##! Disable managing storage directories
##! Docs: https://docs.gitlab.com/omnibus/settings/configuration.html#disable-storage-directories-management
################################################################################


##仅当选择的目录是手动创建时设置，禁用管理存储目录
# manage_storage_directories['enable'] = false
# manage_storage_directories['manage_etc'] = false

################################################################################
## Runtime directory
##! Docs: https://docs.gitlab.com//omnibus/settings/configuration.html#configuring-runtime-directory
################################################################################

# runtime_dir '/run'

################################################################################
## Git
##! Advanced setting for configuring git system settings for omnibus-gitlab
##! internal git
################################################################################


##git设置
# omnibus_gitconfig['system'] = {
#  "pack" => ["threads = 1"],
#  "receive" => ["fsckObjects = true", "advertisePushOptions = true"],
#  "repack" => ["writeBitmaps = true"],
#  "transfer" => ["hideRefs=^refs/tmp/", "hideRefs=^refs/keep-around/", "hideRefs=^refs/remotes/"],
#  "core" => [
#    'alternateRefsCommand="exit 0 #"',
#    "fsyncObjectFiles = true"
#  ],
#  "fetch" => ["writeCommitGraph = true"]
# }

################################################################################
## GitLab Pages
##! Docs: https://docs.gitlab.com/ee/pages/administration.html
################################################################################

##定义以启用GitLab页面
# gitlab_pages['enable'] = false

##配置为在外部IP地址上公开GitLab页面，服务于HTTP
# gitlab_pages['external_http'] = []

##配置为在外部IP地址上公开GitLab页面，服务于HTTPS
# gitlab_pages['external_https'] = []

##配置为在外部IP地址上公开GitLab页面，通过PROXYv2提供HTTPS服务
# gitlab_pages['external_https_proxyv2'] = []

##使用外部IP时需要配置cert
# gitlab_pages['cert'] = "/etc/gitlab/ssl/#{Gitlab['gitlab_pages']['domain']}.crt"
# gitlab_pages['cert_key'] = "/etc/gitlab/ssl/#{Gitlab['gitlab_pages']['domain']}.key"

##配置为使用默认密码套件列表
# gitlab_pages['insecure_ciphers'] = false

##配置为在GitLab页面上启用运行状况检查端点
# gitlab_pages['status_uri'] = "/@status"

##调优GitLab Pages将处理的最大并发连接数。对于无限制的连接，默认为0。
# gitlab_pages['max_connections'] = 0


##将propagate_correlation_id设置为true允许在反向代理后面安装，设置请求头值X-Request-ID，该值将在请求链中传播。
# gitlab_pages['propagate_correlation_id'] = false

##配置为在GitLab Pages中使用JSON结构化日志
# gitlab_pages['log_format'] = "json"

##配置GitLab Pages的详细日志记录
# gitlab_pages['log_verbose'] = false

##哨兵的错误报告和日志
# gitlab_pages['sentry_enabled'] = false
# gitlab_pages['sentry_dsn'] = 'https://<key>@sentry.io/<project>'
# gitlab_pages['sentry_environment'] = 'production'

##监听由反向代理转发的请求
# gitlab_pages['listen_proxy'] = "localhost:8090"

# gitlab_pages['redirect_http'] = true
# gitlab_pages['use_http2'] = true
# gitlab_pages['dir'] = "/var/opt/gitlab/gitlab-pages"
# gitlab_pages['log_directory'] = "/var/log/gitlab/gitlab-pages"

# gitlab_pages['artifacts_server'] = true
# gitlab_pages['artifacts_server_url'] = nil # Defaults to external_url + '/api/v4'
# gitlab_pages['artifacts_server_timeout'] = 10

##不支持绑定挂载的环境应该将此参数设置为true。这与artifacts服务器不兼容
# gitlab_pages['inplace_chroot'] = false

##Prometheus度量Pages文档
# gitlab_pages['metrics_address'] = ":9235"

##最小TLS版本 ("tls1.2" or "tls1.3")
# gitlab_pages['tls_min_version'] = "tls1.2"

##! 最大TLS版本 ("tls1.2" or "tls1.3")
# gitlab_pages['tls_max_version'] = "tls1.3"

##页面访问控制
# gitlab_pages['access_control'] = false
# gitlab_pages['gitlab_id'] = nil # Automatically generated if not present
# gitlab_pages['gitlab_secret'] = nil # Generated if not present
# gitlab_pages['auth_redirect_uri'] = nil # Defaults to projects subdomain of pages_external_url and + '/auth'
# gitlab_pages['gitlab_server'] = nil # Defaults to external_url
# gitlab_pages['internal_gitlab_server'] = nil # Defaults to gitlab_server, can be changed to internal load balancer
# gitlab_pages['auth_secret'] = nil # Generated if not present
# gitlab_pages['auth_scope'] = nil # Defaults to api, can be changed to read_api to increase security

##GitLab API HTTP客户端连接超时时间单位秒
# gitlab_pages['gitlab_client_http_timeout'] = "10s"

##GitLab API JWT令牌过期时间
# gitlab_pages['gitlab_client_jwt_expiry'] = "30s"

##! Fallback to legacy storage
# gitlab_pages['use_legacy_storage'] = nil


##gitlab 缓存失效时间
# gitlab_pages['gitlab_cache_expiry'] = "600s"
##域配置设置为刷新的间隔(默认值:60秒)。
# gitlab_pages['gitlab_cache_refresh'] = "60s"
##过期项目从缓存中删除的时间间隔(默认:60秒)。
# gitlab_pages['gitlab_cache_cleanup'] = "60s"
##每个请求等待GitLab API响应的最大时间。
# gitlab_pages['gitlab_retrieval_timeout'] = "30s"
##在通过GitLab API重新尝试解析域的配置之前的等待间隔。
# gitlab_pages['gitlab_retrieval_interval'] = "1s"
##通过API重试解析域配置的最大次数
# gitlab_pages['gitlab_retrieval_retries'] = 3

##为整个实例定义自定义gitlab-pages HTTP头文件
# gitlab_pages['headers'] = []

##用于在Pages和GitLab之间进行身份验证的共享秘密
# gitlab_pages['api_secret_key'] = nil # Will be generated if not set. Base64 encoded and exactly 32 bytes long.


##archive缓存时间
# gitlab_pages['zip_cache_expiration'] = "60s"
##压缩归档缓存清理间隔。
# gitlab_pages['zip_cache_cleanup'] = "30s"
##如果在过期之前访问缓存存档，则刷新缓存存档的时间间隔。
# gitlab_pages['zip_cache_refresh'] = "30s"
##从文件系统或对象存储打开zip归档文件所花费的最大时间。
# gitlab_pages['zip_open_timeout'] = "30s"

##启用从磁盘而不是对象存储服务内容
# gitlab_pages['enable_disk'] = nil

# gitlab_pages['env_directory'] = "/opt/gitlab/etc/gitlab-pages/env"
# gitlab_pages['env'] = {
#   'SSL_CERT_DIR' => "#{node['package']['install-dir']}/embedded/ssl/certs/"
# }

################################################################################
## GitLab Pages NGINX
################################################################################

# 启用GitLab Pages NGINX
# pages_nginx['enable'] = true

# gitlab_rails['pages_path'] = "/var/opt/gitlab/gitlab-rails/shared/pages"


################################################################################
## GitLab CI
##! Docs: https://docs.gitlab.com/ee/ci/quick_start/README.html
################################################################################

# gitlab_ci['gitlab_ci_all_broken_builds'] = true
# gitlab_ci['gitlab_ci_add_pusher'] = true
# gitlab_ci['builds_directory'] = '/var/opt/gitlab/gitlab-ci/builds'



################################################################################
## GitLab Kubernetes Agent Server
##! Docs: https://gitlab.com/gitlab-org/cluster-integration/gitlab-agent/blob/master/README.md
################################################################################

# gitlab_rails['gitlab_kas_enabled'] = true
# gitlab_rails['gitlab_kas_external_url'] = ws://gitlab.example.com/-/kubernetes-agent
# gitlab_rails['gitlab_kas_internal_url'] = grpc://localhost:8153

##开启GitLab KAS
# gitlab_kas['enable'] = true

##设置 GitLab KAS 代理
# gitlab_kas['agent_configuration_poll_period'] = 20
# gitlab_kas['agent_gitops_poll_period'] = 20
# gitlab_kas['agent_gitops_project_info_cache_ttl'] = 300
# gitlab_kas['agent_gitops_project_info_cache_error_ttl'] = 60
# gitlab_kas['agent_info_cache_ttl'] = 300
# gitlab_kas['agent_info_cache_error_ttl'] = 60

##用于KAS和GitLab之间身份验证的共享秘密
# gitlab_kas['api_secret_key'] = nil # Will be generated if not set. Base64 encoded and exactly 32 bytes long.

##GitLab KAS 监听设置
# gitlab_kas['listen_address'] = 'localhost:8150'
# gitlab_kas['listen_network'] = 'tcp'
# gitlab_kas['listen_websocket'] = true
# gitlab_kas['internal_api_listen_network'] = 'tcp'
# gitlab_kas['internal_api_listen_address'] = 'localhost:8153'

##GitLab KAS的度量配置
# gitlab_kas['metrics_usage_reporting_period'] = 60

##GitLab KAS目录
# gitlab_kas['dir'] = '/var/opt/gitlab/gitlab-kas'
# gitlab_kas['log_directory'] = '/var/log/gitlab/gitlab-kas'
# gitlab_kas['env_directory'] = '/opt/gitlab/etc/gitlab-kas/env'


################################################################################
## GitLab Mattermost
##! Docs: https://docs.gitlab.com/omnibus/gitlab-mattermost
################################################################################

# mattermost_external_url 'http://mattermost.example.com'

# mattermost['enable'] = false
# mattermost['username'] = 'mattermost'
# mattermost['group'] = 'mattermost'
# mattermost['uid'] = nil
# mattermost['gid'] = nil
# mattermost['home'] = '/var/opt/gitlab/mattermost'
# mattermost['database_name'] = 'mattermost_production'
# mattermost['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }
# mattermost['service_address'] = "127.0.0.1"
# mattermost['service_port'] = "8065"
# mattermost['service_site_url'] = nil
# mattermost['service_allowed_untrusted_internal_connections'] = ""
# mattermost['service_enable_api_team_deletion'] = true
# mattermost['team_site_name'] = "GitLab Mattermost"
# mattermost['sql_driver_name'] = 'mysql'
# mattermost['sql_data_source'] = "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"
# mattermost['log_file_directory'] = '/var/log/gitlab/mattermost/'
# mattermost['gitlab_enable'] = false
# mattermost['gitlab_id'] = "12345656"
# mattermost['gitlab_secret'] = "123456789"
# mattermost['gitlab_scope'] = ""
# mattermost['gitlab_auth_endpoint'] = "http://gitlab.example.com/oauth/authorize"
# mattermost['gitlab_token_endpoint'] = "http://gitlab.example.com/oauth/token"
# mattermost['gitlab_user_api_endpoint'] = "http://gitlab.example.com/api/v4/user"
# mattermost['file_directory'] = "/var/opt/gitlab/mattermost/data"
# mattermost['plugin_directory'] = "/var/opt/gitlab/mattermost/plugins"
# mattermost['plugin_client_directory'] = "/var/opt/gitlab/mattermost/client-plugins"



################################################################################
## Mattermost NGINX
################################################################################

##所有在“GitLab Nginx”部分定义的设置也可以在这个“Mattermost NGINX”部分，使用'mattermost_nginx '键。
# mattermost_nginx['enable'] = false

# mattermost_nginx['custom_gitlab_mattermost_server_config'] = "location ^~ /foo-namespace/bar-project/raw/ {\n deny all;\n}\n"
# mattermost_nginx['proxy_set_headers'] = {
#   "Host" => "$http_host",
#   "X-Real-IP" => "$remote_addr",
#   "X-Forwarded-For" => "$proxy_add_x_forwarded_for",
#   "X-Frame-Options" => "SAMEORIGIN",
#   "X-Forwarded-Proto" => "https",
#   "X-Forwarded-Ssl" => "on",
#   "Upgrade" => "$http_upgrade",
#   "Connection" => "$connection_upgrade"
# }



################################################################################
## Registry NGINX
################################################################################

##所有在“GitLab Nginx”部分定义的设置也可以在注册NGINX部分，
##使用'registry_nginx'键。然而,这些设置应该显式设置。
##也就是说，设置为'nginx['some_setting']'不会被自动复制为registery_nginx ['some_setting']应该单独设置。
# registry_nginx['enable'] = false

# registry_nginx['proxy_set_headers'] = {
#  "Host" => "$http_host",
#  "X-Real-IP" => "$remote_addr",
#  "X-Forwarded-For" => "$proxy_add_x_forwarded_for",
#  "X-Forwarded-Proto" => "https",
#  "X-Forwarded-Ssl" => "on"
# }

##当使用与‘external_url’相同的域自动启用注册表时，它将在此端口上侦听
# registry_nginx['listen_port'] = 5050


################################################################################
## Prometheus
##! Docs: https://docs.gitlab.com/ee/administration/monitoring/prometheus/
################################################################################

##启用监视服务
# monitoring_role['enable'] = true

# prometheus['enable'] = true
# prometheus['monitor_kubernetes'] = true
# prometheus['username'] = 'gitlab-prometheus'
# prometheus['group'] = 'gitlab-prometheus'
# prometheus['uid'] = nil
# prometheus['gid'] = nil
# prometheus['shell'] = '/bin/sh'
# prometheus['home'] = '/var/opt/gitlab/prometheus'
# prometheus['log_directory'] = '/var/log/gitlab/prometheus'
# prometheus['rules_files'] = ['/var/opt/gitlab/prometheus/rules/*.rules']
# prometheus['scrape_interval'] = 15
# prometheus['scrape_timeout'] = 15
# prometheus['external_labels'] = { }
# prometheus['env_directory'] = '/opt/gitlab/etc/prometheus/env'
# prometheus['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }
#


##自定义scrape配置
# Example:
#
# prometheus['scrape_configs'] = [
#   {
#     'job_name': 'example',
#     'static_configs' => [
#       'targets' => ['hostname:port'],
#     ],
#   },
# ]
#

##自定义alertmanager 配置
# prometheus['alertmanagers'] = [
#   {
#     'static_configs' => [
#       {
#         'targets' => [
#           'hostname:port'
#         ]
#       }
#     ]
#   }
# ]
#

##自定义 Prometheus flags
# prometheus['flags'] = {
#   'storage.tsdb.path' => "/var/opt/gitlab/prometheus/data",
#   'storage.tsdb.retention.time' => "15d",
#   'config.file' => "/var/opt/gitlab/prometheus/prometheus.yml"
# }

##监听的地址
# prometheus['listen_address'] = 'localhost:9090'


##只有当Prometheus和Rails不在同一台服务器上时才需要。
##在多节点架构中，Prometheus将安装在监控节点上，而Rails将安装在Rails节点上。
##这个值应该是GitLab Rails(Puma/Unicorn, Sidekiq)节点可以使用Prometheus的地址。
# gitlab_rails['prometheus_address'] = 'your.prom:9090'



################################################################################
## Prometheus Alertmanager
################################################################################

# alertmanager['enable'] = true
# alertmanager['home'] = '/var/opt/gitlab/alertmanager'
# alertmanager['log_directory'] = '/var/log/gitlab/alertmanager'
# alertmanager['admin_email'] = 'admin@example.com'
# alertmanager['flags'] = {
#   'web.listen-address' => "localhost:9093",
#   'storage.path' => "/var/opt/gitlab/alertmanager/data",
#   'config.file' => "/var/opt/gitlab/alertmanager/alertmanager.yml"
# }
# alertmanager['env_directory'] = '/opt/gitlab/etc/alertmanager/env'
# alertmanager['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }

##! Advanced settings. Should be changed only if absolutely needed.
# alertmanager['listen_address'] = 'localhost:9093'
# alertmanager['global'] = {}



################################################################################
## Prometheus Node Exporter
##! Docs: https://docs.gitlab.com/ee/administration/monitoring/prometheus/node_exporter.html
################################################################################

# node_exporter['enable'] = true
# node_exporter['home'] = '/var/opt/gitlab/node-exporter'
# node_exporter['log_directory'] = '/var/log/gitlab/node-exporter'
# node_exporter['flags'] = {
#   'collector.textfile.directory' => "/var/opt/gitlab/node-exporter/textfile_collector"
# }
# node_exporter['env_directory'] = '/opt/gitlab/etc/node-exporter/env'
# node_exporter['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }


# node_exporter['listen_address'] = 'localhost:9100'

################################################################################
## Prometheus Redis exporter
##! Docs: https://docs.gitlab.com/ee/administration/monitoring/prometheus/redis_exporter.html
################################################################################

# redis_exporter['enable'] = true
# redis_exporter['log_directory'] = '/var/log/gitlab/redis-exporter'
# redis_exporter['flags'] = {
#   'redis.addr' => "unix:///var/opt/gitlab/redis/redis.socket",
# }
# redis_exporter['env_directory'] = '/opt/gitlab/etc/redis-exporter/env'
# redis_exporter['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }

# redis_exporter['listen_address'] = 'localhost:9121'



################################################################################
## Prometheus Postgres exporter
##! Docs: https://docs.gitlab.com/ee/administration/monitoring/prometheus/postgres_exporter.html
################################################################################

# postgres_exporter['enable'] = true
# postgres_exporter['home'] = '/var/opt/gitlab/postgres-exporter'
# postgres_exporter['log_directory'] = '/var/log/gitlab/postgres-exporter'
# postgres_exporter['flags'] = {}
# postgres_exporter['listen_address'] = 'localhost:9187'
# postgres_exporter['env_directory'] = '/opt/gitlab/etc/postgres-exporter/env'
# postgres_exporter['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }
# postgres_exporter['sslmode'] = nil
# postgres_exporter['per_table_stats'] = false



################################################################################
## Prometheus PgBouncer exporter (EE only)
##! Docs: https://docs.gitlab.com/ee/administration/monitoring/prometheus/pgbouncer_exporter.html
################################################################################

# pgbouncer_exporter['enable'] = false
# pgbouncer_exporter['log_directory'] = "/var/log/gitlab/pgbouncer-exporter"
# pgbouncer_exporter['listen_address'] = 'localhost:9188'
# pgbouncer_exporter['env_directory'] = '/opt/gitlab/etc/pgbouncer-exporter/env'
# pgbouncer_exporter['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }



################################################################################
## Prometheus Gitlab exporter
##! Docs: https://docs.gitlab.com/ee/administration/monitoring/prometheus/gitlab_exporter.html
################################################################################

# gitlab_exporter['enable'] = true
# gitlab_exporter['log_directory'] = "/var/log/gitlab/gitlab-exporter"
# gitlab_exporter['home'] = "/var/opt/gitlab/gitlab-exporter"

##! Advanced settings. Should be changed only if absolutely needed.
# gitlab_exporter['server_name'] = 'webrick'
# gitlab_exporter['listen_address'] = 'localhost'
# gitlab_exporter['listen_port'] = '9168'

##! Manage gitlab-exporter sidekiq probes. false by default when Sentinels are
##! found.
# gitlab_exporter['probe_sidekiq'] = true

# To completely disable prometheus, and all of it's exporters, set to false
# prometheus_monitoring['enable'] = true
################################################################################
## Grafana Dashboards
##! Docs: https://docs.gitlab.com/ee/administration/monitoring/prometheus/#prometheus-as-a-grafana-data-source
################################################################################
# grafana['enable'] = true
# grafana['log_directory'] = '/var/log/gitlab/grafana'
# grafana['home'] = '/var/opt/gitlab/grafana'
# grafana['admin_password'] = 'admin'
# grafana['allow_user_sign_up'] = false
# grafana['basic_auth_enabled'] = false
# grafana['disable_login_form'] = true
# grafana['gitlab_application_id'] = 'GITLAB_APPLICATION_ID'
# grafana['gitlab_secret'] = 'GITLAB_SECRET'
# grafana['env_directory'] = '/opt/gitlab/etc/grafana/env'
# grafana['allowed_groups'] = []
# grafana['gitlab_auth_sign_up'] = true
# grafana['env'] = {
#   'SSL_CERT_DIR' => "#{node['package']['install-dir']}/embedded/ssl/certs/"
# }
# grafana['metrics_enabled'] = false
# grafana['metrics_basic_auth_username'] = 'grafana_metrics' # default: nil
# grafana['metrics_basic_auth_password'] = 'please_set_a_unique_password' # default: nil
# grafana['alerting_enabled'] = false
##smtp设置
#
# grafana['smtp'] = {
#   'enabled' => true,
#   'host' => 'localhost:25',
#   'user' => nil,
#   'password' => nil,
#   'cert_file' => nil,
#   'key_file' => nil,
#   'skip_verify' => false,
#   'from_address' => 'admin@grafana.localhost',
#   'from_name' => 'Grafana',
#   'ehlo_identity' => 'dashboard.example.com',
#   'startTLS_policy' => nil
# }
## Grafana使用报告默认为gitlab_rails['usage_ping_enabled']
# grafana['reporting_enabled'] = true
# grafana['dashboards'] = [
#   {
#     'name' => 'GitLab Omnibus',
#     'orgId' => 1,
#     'folder' => 'GitLab Omnibus',
#     'type' => 'file',
#     'disableDeletion' => true,
#     'updateIntervalSeconds' => 600,
#     'options' => {
#       'path' => '/opt/gitlab/embedded/service/grafana-dashboards',
#     }
#   }
# ]
# grafana['datasources'] = [
#   {
#     'name' => 'GitLab Omnibus',
#     'type' => 'prometheus',
#     'access' => 'proxy',
#     'url' => 'http://localhost:9090'
#   }
# ]
# grafana['http_addr'] = 'localhost'
# grafana['http_port'] = 3000
################################################################################
## Gitaly
##! Docs:
################################################################################
# gitaly['enable'] = true
# gitaly['dir'] = "/var/opt/gitlab/gitaly"
# gitaly['log_directory'] = "/var/log/gitlab/gitaly"
# gitaly['bin_path'] = "/opt/gitlab/embedded/bin/gitaly"
# gitaly['env_directory'] = "/opt/gitlab/etc/gitaly/env"
# gitaly['env'] = {
#  'PATH' => "/opt/gitlab/bin:/opt/gitlab/embedded/bin:/bin:/usr/bin",
#  'HOME' => '/var/opt/gitlab',
#  'TZ' => ':/etc/localtime',
#  'PYTHONPATH' => "/opt/gitlab/embedded/lib/python3.7/site-packages",
#  'ICU_DATA' => "/opt/gitlab/embedded/share/icu/current",
#  'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/",
#  'WRAPPER_JSON_LOGGING' => true
# }
# gitaly['internal_socket_dir'] = "/var/opt/gitlab/gitaly"
# gitaly['socket_path'] = "/var/opt/gitlab/gitaly/gitaly.socket"
# gitaly['listen_addr'] = "localhost:8075"
# gitaly['tls_listen_addr'] = "localhost:9075"
# gitaly['certificate_path'] = "/var/opt/gitlab/gitaly/certificate.pem"
# gitaly['key_path'] = "/var/opt/gitlab/gitaly/key.pem"
# gitaly['prometheus_listen_addr'] = "localhost:9236"
# gitaly['logging_level'] = "warn"
# gitaly['logging_format'] = "json"
# gitaly['logging_sentry_dsn'] = "https://<key>:<secret>@sentry.io/<project>"
# gitaly['logging_ruby_sentry_dsn'] = "https://<key>:<secret>@sentry.io/<project>"
# gitaly['logging_sentry_environment'] = "production"
# gitaly['prometheus_grpc_latency_buckets'] = "[0.001, 0.005, 0.025, 0.1, 0.5, 1.0, 10.0, 30.0, 60.0, 300.0, 1500.0]"
# gitaly['auth_token'] = '<secret>'
# gitaly['auth_transitioning'] = false # When true, auth is logged to Prometheus but NOT enforced
# gitaly['graceful_restart_timeout'] = '1m' # Grace time for a gitaly process to finish ongoing requests
# gitaly['git_catfile_cache_size'] = 100 # Number of 'git cat-file' processes kept around for re-use
# gitaly['git_bin_path'] = "/opt/gitlab/embedded/bin/git" # A custom path for the 'git' executable
# gitaly['open_files_ulimit'] = 15000 # Maximum number of open files allowed for the gitaly process
# gitaly['ruby_max_rss'] = 300000000 # RSS threshold in bytes for triggering a gitaly-ruby restart
# gitaly['ruby_graceful_restart_timeout'] = '10m' # Grace time for a gitaly-ruby process to finish ongoing requests
# gitaly['ruby_restart_delay'] = '5m' # Period of sustained high RSS that needs to be observed before restarting gitaly-ruby
# gitaly['ruby_rugged_git_config_search_path'] = "/opt/gitlab/embedded/etc" # Location of system-wide gitconfig file
# gitaly['ruby_num_workers'] = 3 # Number of gitaly-ruby worker processes. Minimum 2, default 2.
# gitaly['concurrency'] = [
#   {
#     'rpc' => "/gitaly.SmartHTTPService/PostReceivePack",
#     'max_per_repo' => 20
#   }, {
#     'rpc' => "/gitaly.SSHService/SSHUploadPack",
#     'max_per_repo' => 5
#   }
# ]
#
# gitaly['daily_maintenance_start_hour'] = 22
# gitaly['daily_maintenance_start_minute'] = 30
# gitaly['daily_maintenance_duration'] = '30m'
# gitaly['daily_maintenance_storages'] = ["default"]
# gitaly['daily_maintenance_disabled'] = false
# gitaly['cgroups_count'] = 10
# gitaly['cgroups_mountpoint'] = '/sys/fs/cgroup'
# gitaly['cgroups_hierarchy_root'] = 'gitaly'
# gitaly['cgroups_memory_enabled'] = true
# gitaly['cgroups_memory_limit'] = 1048576
# gitaly['cgroups_cpu_enabled'] = true
# gitaly['cgroups_cpu_shares'] = 512
# gitaly['pack_objects_cache_enabled'] = true
# gitaly['pack_objects_cache_dir'] = '/var/opt/gitlab/git-data/repositories/+gitaly/PackObjectsCache'
# gitaly['pack_objects_cache_max_age'] = '5m'
################################################################################
## Praefect
##! Docs: https://gitlab.com/gitlab-org/gitaly/blob/master/doc/design_ha.md
################################################################################
# praefect['enable'] = false
# praefect['dir'] = "/var/opt/gitlab/praefect"
# praefect['log_directory'] = "/var/log/gitlab/praefect"
# praefect['env_directory'] = "/opt/gitlab/etc/praefect/env"
# praefect['env'] = {
#  'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/",
#  'GITALY_PID_FILE' => "/var/opt/gitlab/praefect/praefect.pid",
#  'WRAPPER_JSON_LOGGING' => true
# }
# praefect['wrapper_path'] = "/opt/gitlab/embedded/bin/gitaly-wrapper"
# praefect['failover_enabled'] = true
# praefect['auth_token'] = ""
# praefect['auth_transitioning'] = false
# praefect['listen_addr'] = "localhost:2305"
# praefect['tls_listen_addr'] = "localhost:3305"
# praefect['certificate_path'] = "/var/opt/gitlab/prafect/certificate.pem"
# praefect['key_path'] = "/var/opt/gitlab/prafect/key.pem"
# praefect['prometheus_listen_addr'] = "localhost:9652"
# praefect['prometheus_grpc_latency_buckets'] = "[0.001, 0.005, 0.025, 0.1, 0.5, 1.0, 10.0, 30.0, 60.0, 300.0, 1500.0]"
# praefect['logging_level'] = "warn"
# praefect['logging_format'] = "json"
# praefect['virtual_storages'] = {
#   'default' => {
#     'default_replication_factor' => 3,
#     'nodes' => {
#       'praefect-internal-0' => {
#         'address' => 'tcp://10.23.56.78:8075',
#         'token' => 'abc123'
#       },
#       'praefect-internal-1' => {
#         'address' => 'tcp://10.76.23.31:8075',
#         'token' => 'xyz456'
#       }
#     }
#   },
#   'alternative' => {
#     'nodes' => {
#       'praefect-internal-2' => {
#         'address' => 'tcp://10.34.1.16:8075',
#         'token' => 'abc321'
#       },
#       'praefect-internal-3' => {
#         'address' => 'tcp://10.23.18.6:8075',
#         'token' => 'xyz890'
#       }
#     }
#   }
# }
# praefect['sentry_dsn'] = "https://<key>:<secret>@sentry.io/<project>"
# praefect['sentry_environment'] = "production"
# praefect['auto_migrate'] = true
# praefect['database_host'] = 'postgres.external'
# praefect['database_port'] = 6432
# praefect['database_user'] = 'praefect'
# praefect['database_password'] = 'secret'
# praefect['database_dbname'] = 'praefect_production'
# praefect['database_sslmode'] = 'disable'
# praefect['database_sslcert'] = '/path/to/client-cert'
# praefect['database_sslkey'] = '/path/to/client-key'
# praefect['database_sslrootcert'] = '/path/to/rootcert'
# praefect['reconciliation_scheduling_interval'] = '5m'
# praefect['reconciliation_histogram_buckets'] = '[0.001, 0.005, 0.025, 0.1, 0.5, 1.0, 10.0]'
# praefect['database_direct_host'] = 'postgres.internal'
# praefect['database_direct_port'] = 5432
# praefect['database_direct_user'] = 'praefect'
# praefect['database_direct_password'] = 'secret'
# praefect['database_direct_dbname'] = 'praefect_production_direct'
# praefect['database_direct_sslmode'] = 'disable'
# praefect['database_direct_sslcert'] = '/path/to/client-cert'
# praefect['database_direct_sslkey'] = '/path/to/client-key'
# praefect['database_direct_sslrootcert'] = '/path/to/rootcert'
################################################################################
# Storage check
################################################################################
# storage_check['enable'] = false
# storage_check['target'] = 'unix:///var/opt/gitlab/gitlab-rails/sockets/gitlab.socket'
# storage_check['log_directory'] = '/var/log/gitlab/storage-check'
################################################################################
# Let's Encrypt integration
################################################################################
# letsencrypt['enable'] = nil
# letsencrypt['contact_emails'] = [] # This should be an array of email addresses to add as contacts
# letsencrypt['group'] = 'root'
# letsencrypt['key_size'] = 2048
# letsencrypt['owner'] = 'root'
# letsencrypt['wwwroot'] = '/var/opt/gitlab/nginx/www'
# See http://docs.gitlab.com/omnibus/settings/ssl.html#automatic-renewal for more on these sesttings
# letsencrypt['auto_renew'] = true
# letsencrypt['auto_renew_hour'] = 0
# letsencrypt['auto_renew_minute'] = nil # Should be a number or cron expression, if specified.
# letsencrypt['auto_renew_day_of_month'] = "*/4"
# letsencrypt['auto_renew_log_directory'] = '/var/log/gitlab/lets-encrypt'

##关闭初始化系统自动检测。 在非docker容器中跳过init检测。建议不要更改
# package['detect_init'] = true

##尝试修改内核参数。若要在相关文件系统为只读的容器中跳过此操作，请将该值设置为false。
# package['modify_kernel_parameters'] = true

##指定systemd单位可以创建的最大任务数
# package['systemd_tasks_max'] = 4915

##设置以配置GitLab的systemd单元的顺序。不要改
# package['systemd_after'] = 'multi-user.target'
# package['systemd_wanted_by'] = 'multi-user.target'



################################################################################
################################################################################
##                  Configuration Settings for GitLab EE only                 ##
################################################################################
################################################################################



################################################################################
## Auxiliary cron jobs applicable to GitLab EE only
################################################################################
##GitLab EE定时任务
# gitlab_rails['geo_file_download_dispatch_worker_cron'] = "*/10 * * * *"
# gitlab_rails['geo_repository_sync_worker_cron'] = "*/5 * * * *"
# gitlab_rails['geo_secondary_registry_consistency_worker'] = "* * * * *"
# gitlab_rails['geo_secondary_usage_data_cron_worker'] = "0 0 * * 0"
# gitlab_rails['geo_prune_event_log_worker_cron'] = "*/5 * * * *"
# gitlab_rails['geo_repository_verification_primary_batch_worker_cron'] = "*/5 * * * *"
# gitlab_rails['geo_repository_verification_secondary_scheduler_worker_cron'] = "*/5 * * * *"
# gitlab_rails['ldap_sync_worker_cron'] = "30 1 * * *"
# gitlab_rails['ldap_group_sync_worker_cron'] = "0 * * * *"
# gitlab_rails['historical_data_worker_cron'] = "0 12 * * *"
# gitlab_rails['pseudonymizer_worker_cron'] = "0 23 * * *"
# gitlab_rails['elastic_index_bulk_cron'] = "*/1 * * * *"
# gitlab_rails['analytics_devops_adoption_create_all_snapshots_worker_cron'] = "0 4 * * 0"



################################################################################
## Kerberos (EE Only)
##! Docs: https://docs.gitlab.com/ee/integration/kerberos.html#http-git-access
################################################################################

# gitlab_rails['kerberos_enabled'] = true
# gitlab_rails['kerberos_keytab'] = /etc/http.keytab
# gitlab_rails['kerberos_service_principal_name'] = HTTP/gitlab.example.com@EXAMPLE.COM
# gitlab_rails['kerberos_simple_ldap_linking_allowed_realms'] = ['example.com','kerberos.example.com']
# gitlab_rails['kerberos_use_dedicated_port'] = true
# gitlab_rails['kerberos_port'] = 8443
# gitlab_rails['kerberos_https'] = true



################################################################################
## Package repository
##! Docs: https://docs.gitlab.com/ee/administration/packages/
################################################################################

# gitlab_rails['packages_enabled'] = true
# gitlab_rails['packages_storage_path'] = "/var/opt/gitlab/gitlab-rails/shared/packages"
# gitlab_rails['packages_object_store_enabled'] = false
# gitlab_rails['packages_object_store_direct_upload'] = false
# gitlab_rails['packages_object_store_background_upload'] = true
# gitlab_rails['packages_object_store_proxy_download'] = false
# gitlab_rails['packages_object_store_remote_directory'] = "packages"
# gitlab_rails['packages_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'host' => 's3.amazonaws.com',
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }



################################################################################
## Dependency proxy
##! Docs: https://docs.gitlab.com/ee/administration/packages/dependency_proxy.html
################################################################################

# gitlab_rails['dependency_proxy_enabled'] = true
# gitlab_rails['dependency_proxy_storage_path'] = "/var/opt/gitlab/gitlab-rails/shared/dependency_proxy"
# gitlab_rails['dependency_proxy_object_store_enabled'] = false
# gitlab_rails['dependency_proxy_object_store_direct_upload'] = false
# gitlab_rails['dependency_proxy_object_store_background_upload'] = true
# gitlab_rails['dependency_proxy_object_store_proxy_download'] = false
# gitlab_rails['dependency_proxy_object_store_remote_directory'] = "dependency_proxy"
# gitlab_rails['dependency_proxy_object_store_connection'] = {
#   'provider' => 'AWS',
#   'region' => 'eu-west-1',
#   'aws_access_key_id' => 'AWS_ACCESS_KEY_ID',
#   'aws_secret_access_key' => 'AWS_SECRET_ACCESS_KEY',
#   # # The below options configure an S3 compatible host instead of AWS
#   # 'host' => 's3.amazonaws.com',
#   # 'aws_signature_version' => 4, # For creation of signed URLs. Set to 2 if provider does not support v4.
#   # 'endpoint' => 'https://s3.amazonaws.com', # default: nil - Useful for S3 compliant services such as DigitalOcean Spaces
#   # 'path_style' => false # Use 'host/bucket_name/object' instead of 'bucket_name.host/object'
# }



################################################################################
## GitLab Sentinel (EE Only)
##! Docs: http://docs.gitlab.com/ce/administration/high_availability/redis.html#high-availability-with-sentinel
################################################################################

##确保你配置了所有redis['master_*']键
##要启用Sentinel并禁用这台机器上的所有其他服务，请取消下面这行注释(如果你启用了Redis角色，它将保留它)。
# redis_sentinel_role['enable'] = true

# sentinel['enable'] = true

##绑定到所有接口，取消注释来指定一个IP，并绑定到一个单独的
# sentinel['bind'] = '0.0.0.0'

##取消更改默认端口的注释
# sentinel['port'] = 26379

##支持在Docker或NAT环境中运行哨兵
##在一个标准的情况下，哨兵将运行在相同的网络服务，所以相同的IP将宣布为Redis和哨兵
##只有在Sentinel需要宣布一个不同的IP服务时才定义这些值
# sentinel['announce_ip'] = nil # If not defined, its value will be taken from redis['announce_ip'] or nil if not present
# sentinel['announce_port'] = nil # If not defined, its value will be taken from sentinel['port'] or nil if redis['announce_ip'] not present

##法定人数必须反映投票哨兵的数量，它需要启动一个,数值不能大于哨兵数量
# sentinel['quorum'] = 1

##考虑在x毫秒后服务器停止响应。
# sentinel['down_after_milliseconds'] = 10000

##指定故障转移超时时间，以毫秒为单位。
# sentinel['failover_timeout'] = 60000



################################################################################
## Additional Database Settings (EE only)
##! Docs: https://docs.gitlab.com/ee/administration/database_load_balancing.html
################################################################################
# gitlab_rails['db_load_balancing'] = { 'hosts' => ['secondary1.example.com'] }



################################################################################
## GitLab Geo
##! Docs: https://docs.gitlab.com/ee/gitlab-geo
################################################################################

# 如果为空，则为external_url.
# gitlab_rails['geo_node_name'] = nil

# gitlab_rails['geo_registry_replication_enabled'] = true
# gitlab_rails['geo_registry_replication_primary_api_url'] = 'https://example.com:5050'



################################################################################
## GitLab Geo Secondary (EE only)
################################################################################
# geo_secondary['auto_migrate'] = true
# geo_secondary['db_adapter'] = "postgresql"
# geo_secondary['db_encoding'] = "unicode"
# geo_secondary['db_collation'] = nil
# geo_secondary['db_database'] = "gitlabhq_geo_production"
# geo_secondary['db_username'] = "gitlab_geo"
# geo_secondary['db_password'] = nil
# geo_secondary['db_host'] = "/var/opt/gitlab/geo-postgresql"
# geo_secondary['db_port'] = 5431
# geo_secondary['db_socket'] = nil
# geo_secondary['db_sslmode'] = nil
# geo_secondary['db_sslcompression'] = 0
# geo_secondary['db_sslrootcert'] = nil
# geo_secondary['db_sslca'] = nil
# geo_secondary['db_prepared_statements'] = false



################################################################################
## GitLab Geo Secondary Tracking Database (EE only)
################################################################################

# geo_postgresql['enable'] = false
# geo_postgresql['ha'] = false
# geo_postgresql['dir'] = '/var/opt/gitlab/geo-postgresql'
# geo_postgresql['pgbouncer_user'] = nil
# geo_postgresql['pgbouncer_user_password'] = nil
## 'SQL_USER_PASSWORD_HASH' 可以使用命令 'gitlab-ctl pg-password-md5 gitlab' 生成
# geo_postgresql['sql_user_password'] = 'SQL_USER_PASSWORD_HASH'



################################################################################
## Unleash
##! These settings are for GitLab internal use.
##! They are used to control feature flags during GitLab development.
##! Docs: https://docs.gitlab.com/ee/development/feature_flags
################################################################################

# gitlab_rails['feature_flags_unleash_enabled'] = false
# gitlab_rails['feature_flags_unleash_url'] = nil
# gitlab_rails['feature_flags_unleash_app_name'] = nil
# gitlab_rails['feature_flags_unleash_instance_id'] = nil



################################################################################
# Pgbouncer (EE only)
# See [GitLab PgBouncer documentation](http://docs.gitlab.com/omnibus/settings/database.html#enabling-pgbouncer-ee-only)
# See the [PgBouncer page](https://pgbouncer.github.io/config.html) for details
################################################################################

# pgbouncer['enable'] = false
# pgbouncer['log_directory'] = '/var/log/gitlab/pgbouncer'
# pgbouncer['data_directory'] = '/var/opt/gitlab/pgbouncer'
# pgbouncer['env_directory'] = '/opt/gitlab/etc/pgbouncer/env'
# pgbouncer['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }
# pgbouncer['listen_addr'] = '0.0.0.0'
# pgbouncer['listen_port'] = '6432'
# pgbouncer['pool_mode'] = 'transaction'
# pgbouncer['server_reset_query'] = 'DISCARD ALL'
# pgbouncer['application_name_add_host'] = '1'
# pgbouncer['max_client_conn'] = '2048'
# pgbouncer['default_pool_size'] = '100'
# pgbouncer['min_pool_size'] = '0'
# pgbouncer['reserve_pool_size'] = '5'
# pgbouncer['reserve_pool_timeout'] = '5.0'
# pgbouncer['server_round_robin'] = '0'
# pgbouncer['log_connections'] = '0'
# pgbouncer['server_idle_timeout'] = '30'
# pgbouncer['dns_max_ttl'] = '15.0'
# pgbouncer['dns_zone_check_period'] = '0'
# pgbouncer['dns_nxdomain_ttl'] = '15.0'
# pgbouncer['admin_users'] = %w(gitlab-psql postgres pgbouncer)
# pgbouncer['stats_users'] = %w(gitlab-psql postgres pgbouncer)
# pgbouncer['ignore_startup_parameters'] = 'extra_float_digits'
# pgbouncer['databases'] = {
#   DATABASE_NAME: {
#     host: HOSTNAME,
#     port: PORT
#     user: USERNAME,
#     password: PASSWORD
###! generate this with `echo -n '$password + $username' | md5sum`
#   }
#   ...
# }
# pgbouncer['logfile'] = nil
# pgbouncer['unix_socket_dir'] = nil
# pgbouncer['unix_socket_mode'] = '0777'
# pgbouncer['unix_socket_group'] = nil
# pgbouncer['auth_type'] = 'md5'
# pgbouncer['auth_hba_file'] = nil
# pgbouncer['auth_query'] = 'SELECT username, password FROM public.pg_shadow_lookup($1)'
# pgbouncer['users'] = {
#   {
#     name: USERNAME,
#     password: MD5_PASSWORD_HASH
#   }
# }
# postgresql['pgbouncer_user'] = nil
# postgresql['pgbouncer_user_password'] = nil
# pgbouncer['server_reset_query_always'] = 0
# pgbouncer['server_check_query'] = 'select 1'
# pgbouncer['server_check_delay'] = 30
# pgbouncer['max_db_connections'] = nil
# pgbouncer['max_user_connections'] = nil
# pgbouncer['syslog'] = 0
# pgbouncer['syslog_facility'] = 'daemon'
# pgbouncer['syslog_ident'] = 'pgbouncer'
# pgbouncer['log_disconnections'] = 1
# pgbouncer['log_pooler_errors'] = 1
# pgbouncer['stats_period'] = 60
# pgbouncer['verbose'] = 0
# pgbouncer['server_lifetime'] = 3600
# pgbouncer['server_connect_timeout'] = 15
# pgbouncer['server_login_retry'] = 15
# pgbouncer['query_timeout'] = 0
# pgbouncer['query_wait_timeout'] = 120
# pgbouncer['client_idle_timeout'] = 0
# pgbouncer['client_login_timeout'] = 60
# pgbouncer['autodb_idle_timeout'] = 3600
# pgbouncer['suspend_timeout'] = 10
# pgbouncer['idle_transaction_timeout'] = 0
# pgbouncer['pkt_buf'] = 4096
# pgbouncer['listen_backlog'] = 128
# pgbouncer['sbuf_loopcnt'] = 5
# pgbouncer['max_packet_size'] = 2147483647
# pgbouncer['tcp_defer_accept'] = 0
# pgbouncer['tcp_socket_buffer'] = 0
# pgbouncer['tcp_keepalive'] = 1
# pgbouncer['tcp_keepcnt'] = 0
# pgbouncer['tcp_keepidle'] = 0
# pgbouncer['tcp_keepintvl'] = 0
# pgbouncer['disable_pqexec'] = 0

## Pgbouncer client TLS options
# pgbouncer['client_tls_sslmode'] = 'disable'
# pgbouncer['client_tls_ca_file'] = nil
# pgbouncer['client_tls_key_file'] = nil
# pgbouncer['client_tls_cert_file'] = nil
# pgbouncer['client_tls_protocols'] = 'all'
# pgbouncer['client_tls_dheparams'] = 'auto'
# pgbouncer['client_tls_ecdhcurve'] = 'auto'
#
## Pgbouncer server  TLS options
# pgbouncer['server_tls_sslmode'] = 'disable'
# pgbouncer['server_tls_ca_file'] = nil
# pgbouncer['server_tls_key_file'] = nil
# pgbouncer['server_tls_cert_file'] = nil
# pgbouncer['server_tls_protocols'] = 'all'
# pgbouncer['server_tls_ciphers'] = 'fast'



################################################################################
# Patroni (EE only)
# NOTICE: Patroni is an experimental feature and subject to change.
################################################################################

# patroni['enable'] = false

# patroni['dir'] = '/var/opt/gitlab/patroni'
# patroni['ctl_command'] = '/opt/gitlab/embedded/bin/patronictl'

# patroni['loop_wait'] = 10
# patroni['ttl'] = 30
# patroni['retry_timeout'] = 10
# patroni['maximum_lag_on_failover'] = 1_048_576
# patroni['max_timelines_history'] = 0
# patroni['master_start_timeout'] = 300
# patroni['use_pg_rewind'] = true
# patroni['remove_data_directory_on_rewind_failure'] = false
# patroni['remove_data_directory_on_diverged_timelines'] = false
# patroni['use_slots'] = true
# patroni['replication_password'] = nil
# patroni['replication_slots'] = {}

##备用集群复制设置
# patroni['standby_cluster']['enable'] = false
# patroni['standby_cluster']['host'] = nil
# patroni['standby_cluster']['port'] = 5432
# patroni['standby_cluster']['primary_slot_name'] = nil

## Global/Universal 设置
# patroni['scope'] = 'gitlab-postgresql-ha'
# patroni['name'] = nil

## 日志 settings
# patroni['log_directory'] = '/var/log/gitlab/patroni'
# patroni['log_level'] = 'INFO'

## Consul specific 设置
# patroni['consul']['url'] = 'http://127.0.0.1:8500'
# patroni['consul']['service_check_interval'] = '10s'
# patroni['consul']['register_service'] = true
# patroni['consul']['checks'] = []

## PostgreSQL配置覆盖
# patroni['postgresql']['hot_standby'] = 'on'

##所有节点保持一致，使用PostgreSQL的默认值
# patroni['postgresql']['wal_level'] = 'replica'
# patroni['postgresql']['wal_log_hints'] = 'on'
# patroni['postgresql']['max_worker_processes'] = 8
# patroni['postgresql']['max_locks_per_transaction'] = 64
# patroni['postgresql']['max_connections'] = 200
# patroni['postgresql']['checkpoint_timeout'] = 30

## 这些设置可以在不同节点不同
##保留PostgreSQL的默认值。
# patroni['postgresql']['wal_keep_segments'] = 8
# patroni['postgresql']['max_wal_senders'] = 5
# patroni['postgresql']['max_replication_slots'] = 5

## 流复制的永久复制槽
# patroni['replication_slots'] = {
#   'geo_secondary' => { 'type' => 'physical' }
# }

## 绑定和监听的地址和端口。
# patroni['listen_address'] = nil
# patroni['port'] = '8008'

##通告到其他集群的守护神节点的地址
# patroni['connect_address'] = nil

##守护神节点的端口，默认为与patroni['port']相同。
# patroni['connect_port'] = '8008'

##用户名和密码用于基本身份验证对写命令
# patroni['username'] = nil
# patroni['password'] = nil



################################################################################
# Consul (EEP only)
################################################################################

# consul['enable'] = false
# consul['dir'] = '/var/opt/gitlab/consul'
# consul['username'] = 'gitlab-consul'
# consul['group'] = 'gitlab-consul'
# consul['config_file'] = '/var/opt/gitlab/consul/config.json'
# consul['config_dir'] = '/var/opt/gitlab/consul/config.d'
# consul['data_dir'] = '/var/opt/gitlab/consul/data'
# consul['log_directory'] = '/var/log/gitlab/consul'
# consul['env_directory'] = '/opt/gitlab/etc/consul/env'
# consul['env'] = {
#   'SSL_CERT_DIR' => "/opt/gitlab/embedded/ssl/certs/"
# }
# consul['monitoring_service_discovery'] = false
# consul['node_name'] = nil
# consul['script_directory'] = '/var/opt/gitlab/consul/scripts'
# consul['configuration'] = {
#   'client_addr' => nil,
#   'datacenter' => 'gitlab_consul',
#   'enable_script_checks' => true,
#   'server' => false
# }
# consul['services'] = []
# consul['service_config'] = {
#   'postgresql' => {
#     'service' => {
#       'name' => "postgresql",
#       'address' => '',
#       'port' => 5432,
#       'checks' => [
#         {
#           'script' => "/var/opt/gitlab/consul/scripts/check_postgresql",
#           'interval' => "10s"
#         }
#       ]
#     }
#   }
# }
# consul['watchers'] = {
#   'postgresql' => {
#     enable: false,
#     handler: 'failover_pgbouncer'
#   }
# }


################################################################################
# Service desk email settings (EEP only)
################################################################################

##允许用户通过发送电子邮件到创建新的服务台问题
# gitlab_rails['service_desk_email_enabled'] = false

##服务台邮箱设置
# gitlab_rails['service_desk_email_address'] = "contact_project+%{key}@gmail.com"

##服务台邮箱地址
# gitlab_rails['service_desk_email_email'] = "contact_project@gmail.com"

##服务台邮箱帐号密码
# gitlab_rails['service_desk_email_password'] = "[REDACTED]"

##服务台邮件将在那里结束的邮箱。通常“收件箱”。
# gitlab_rails['service_desk_email_mailbox_name'] = "inbox"
##IDLE命令超时时间。
# gitlab_rails['service_desk_email_idle_timeout'] = 60
##内部' mail_room ' JSON日志文件的文件
# gitlab_rails['service_desk_email_log_file'] = "/var/log/gitlab/mailroom/mail_room_json.log"

##服务台IMAP设置
# gitlab_rails['service_desk_email_host'] = "imap.gmail.com"
# gitlab_rails['service_desk_email_port'] = 993
# gitlab_rails['service_desk_email_ssl'] = true
# gitlab_rails['service_desk_email_start_tls'] = false