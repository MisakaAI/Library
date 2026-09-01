# TimeMachine

## Samba

```/etc/samba/smb.conf
[global]
    vfs objects = catia fruit streams_xattr
    min protocol = SMB3_11
    smb encrypt = required
    ea support = yes
    fruit:metadata = stream
    fruit:model = MacSamba
    fruit:posix_rename = yes
    fruit:veto_appledouble = no
    fruit:wipe_intentionally_left_blank_rfork = yes
    fruit:delete_empty_adfiles = yes
    fruit:aapl = yes

[TimeMachine]
    comment = Mac Mini Time Machine
    path = /data/TimeMachine
    writable = yes
    create mask = 0644
    directory mask = 0755
    browseable = yes
    guest ok = no
    valid users = misaka
    fruit:time machine = yes
    fruit:time machine max size = 500G
```
