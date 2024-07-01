# 幻兽帕鲁

```sh
docker run -d \
    --name palworld-server \
    -p 8211:8211/udp \
    -p 27015:27015/udp \
    -v ./palworld:/palworld/ \
    -e PUID=1000 \
    -e PGID=1000 \
    -e PORT=8211 \
    -e PLAYERS=16 \
    -e MULTITHREADING=true \
    -e RCON_ENABLED=true \
    -e RCON_PORT=25575 \
    -e TZ=UTC \
    -e ADMIN_PASSWORD="<ADMIN_PASSWORD>" \
    -e SERVER_PASSWORD="<SERVER_PASSWORD>" \
    -e PAL_EGG_DEFAULT_HATCHING_TIME=0.0001 \
    -e COMMUNITY=false \
    -e SERVER_NAME="<服务器名称>" \
    -e SERVER_DESCRIPTION="<服务器说明>" \
    -e ALLOW_CONNECT_PLATFORM="Steam" \
    -e PLAYER_STAMINA_DECREASE_RATE=0.5 \
    -e DEATH_PENALTY="None" \
    -e PAL_EGG_DEFAULT_HATCHING_TIME=0.25 \
    -e BASE_CAMP_MAX_NUM_IN_GUILD=10 \
    -e BASE_CAMP_WORKER_MAX_NUM=50 \
    --restart unless-stopped \
    --stop-timeout 30 \
    thijsvanloef/palworld-server-docker:latest
```

## 参数说明

```sh
# 耐力减少率
PLAYER_STAMINA_DECREASE_RATE=0.5
# 死亡掉落
DEATH_PENALTY="None"
# 蛋孵化时间
PAL_EGG_DEFAULT_HATCHING_TIME=0.25
# 工会最大基地数量
BASE_CAMP_MAX_NUM_IN_GUILD=10
# 最大工作帕鲁数量
BASE_CAMP_WORKER_MAX_NUM=50
```

## 配置

文件位置 `Pal/Saved/Config/LinuxServer/PalWorldSettings.ini`

```ini
; 该配置文件是默认服务器设置的示例。
; 对该文件的更改不会反映在服务器上。
; 要更改服务器设置，请修改 Pal/Saved/Config/WindowsServer/PalWorldSettings.ini。

[/Script/Pal.PalGameWorldSettings]

OptionSettings=(

; 难度None或Difficulty
Difficulty=None,

; 白天流逝速度
DayTimeSpeedRate=1.000000,

; 夜晚流逝速度
NightTimeSpeedRate=1.000000,

; 经验值倍率
ExpRate=1.000000,

; 捕捉概率倍率
PalCaptureRate=1.000000,

; 帕鲁出现数量倍率
PalSpawnNumRate=1.000000,

; 帕鲁攻击伤害倍率
PalDamageRateAttack=1.000000,

; 帕鲁承受伤害倍率
PalDamageRateDefense=1.000000,

; 玩家攻击伤害倍率
PlayerDamageRateAttack=1.000000,

; 玩家承受伤害倍率
PlayerDamageRateDefense=1.000000,

; 玩家饱食度降低倍率
PlayerStomachDecreaceRate=1.000000,

; 玩家耐力倍率
PlayerStaminaDecreaceRate=1.000000,

; 玩家生命值恢复倍率
PlayerAutoHPRegeneRate=1.000000,

; 玩家睡眠时生命恢复倍率
PlayerAutoHpRegeneRateInSleep=1.000000,

; 帕鲁饱食度降低倍率
PalStomachDecreaceRate=1.000000,

; 帕鲁耐力降低倍率
PalStaminaDecreaceRate=1.000000,

; 帕鲁生命值自然恢复倍率
PalAutoHPRegeneRate=1.000000,

; 帕鲁睡眠时生命恢复倍率
PalAutoHpRegeneRateInSleep=1.000000,

; 对建筑物伤害倍率
BuildObjectDamageRate=1.000000,

; 建筑物劣化速度倍率
BuildObjectDeteriorationDamageRate=1.000000,

; 可采集物品掉落倍率
CollectionDropRate=1.000000,

; 可采集物品生命值倍率
CollectionObjectHpRate=1.000000,

; 可采集物品生成速率
CollectionObjectRespawnSpeedRate=1.000000,

; 敌方掉落物品率
EnemyDropItemRate=1.000000,

; 死亡惩罚None不掉落Item只掉物品不掉装备ItemAndEquipment掉物品和装备All全都掉
DeathPenalty=All,

; 启用玩家对玩家伤害功能
bEnablePlayerToPlayerDamage=False,

; 火焰伤害
bEnableFriendlyFire=False,

; 否会发生袭击事件
bEnableInvaderEnemy=True,

; ？？
bActiveUNKO=False,

; 启用瞄准辅助手柄
bEnableAimAssistPad=True,

; 准星开启
bEnableAimAssistKeyboard=False,

; 掉落物品最大数量
DropItemMaxNum=3000,

; 掉落物品最大数量_UNKO
DropItemMaxNum_UNKO=100,

; 大本营最大数
BaseCampMaxNum=128,

; 大本营工人最多人数
BaseCampWorkerMaxNum=15,

; 掉落物品存在最大时长
DropItemAliveMaxHours=1.000000,

; 自动重置没有在线玩家的公会
bAutoResetGuildNoOnlinePlayers=False,

; 无在线玩家时自动重置生成时间
AutoResetGuildTimeNoOnlinePlayers=72.000000,

; 公会玩家最大数量
GuildPlayerMaxNum=20,

; 帕鲁蛋默认孵化时间
PalEggDefaultHatchingTime=72.000000,

; 工作速率
WorkSpeedRate=1.000000,

; 多人游戏
bIsMultiplay=False,

; PvP
bIsPvP=False,

; 可拾取其他公会的死亡掉落物
bCanPickupOtherGuildDeathPenaltyDrop=False,

; 启用不登录惩罚
bEnableNonLoginPenalty=True,

; 启用快速旅行
bEnableFastTravel=True,

; 通过地图选择起始位置
bIsStartLocationSelectByMap=True,

; 注销后玩家仍然存在
bExistPlayerAfterLogout=False,

; 启用防御其他公会玩家功能
bEnableDefenseOtherGuildPlayer=False,

; 合作玩家最大人数
CoopPlayerMaxNum=4,

; 服务器玩家最大人数
ServerPlayerMaxNum=32,

; 服务器名称
ServerName="Default Palworld Server",

; 服务器描述
ServerDescription="",

; 管理员密码
AdminPassword="",

; 服务器密码
ServerPassword="",

; 服务器端口
PublicPort=8211,

; 服务器ip
PublicIP="",

; 启用 RCON
RCONEnabled=False,

; RCON端口
RCONPort=25575,

; 地区
Region="",

; 使用授权
bUseAuth=True,

; 封禁用户URL
BanListURL="https://api.palworldgame.com/api/banlist.txt")
```

## 参考文献

- [palworld-server-docker](https://github.com/thijsvanloef/palworld-server-docker)
