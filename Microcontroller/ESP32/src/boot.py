import esp

esp.osdebug(None)

try:
    import main

    # 配置 Wi-Fi 热点
    main.SSID = "ESP32-AP-DEV"
    main.PASSWORD = "12345678"
    # 运行
    main.run()
except Exception as e:
    print("Error in main:", e)
